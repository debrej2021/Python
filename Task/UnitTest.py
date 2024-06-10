import unittest
import json
import os
import shutil
from datetime import datetime
from unittest.mock import patch, MagicMock
from EnvironmentConfigVersionControl import Configuration, Environment, EnvironmentManager, Validator, VersionedConfig

class TestConfiguration(unittest.TestCase):
    def setUp(self):
        self.config_name = 'database'
        self.config_value = {'url': 'localhost', 'port': 5432}
        self.configuration = Configuration(self.config_name, self.config_value)

    def test_initial_configuration(self):
        self.assertEqual(self.configuration.get_config_value(), self.config_value)
        self.assertEqual(self.configuration.config_name, self.config_name)
        self.assertEqual(self.configuration.version, 1)
        self.assertTrue(isinstance(self.configuration.timestamp, datetime))

    def test_set_config_value(self):
        new_value = {'url': 'localhost', 'port': 5433}
        self.configuration.set_config_value(new_value)
        self.assertEqual(self.configuration.get_config_value(), new_value)
        self.assertEqual(self.configuration.version, 2)

    def test_validate_config(self):
        with self.assertRaises(ValueError):
            self.configuration.set_config_value({'url': 'localhost', 'port': 'invalid'})

class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.env_name = 'development'
        self.environment = Environment(self.env_name)

    def test_add_configuration(self):
        config_name = 'database'
        config_value = {'url': 'localhost', 'port': 5432}
        self.environment.add_configuration(config_name, config_value)
        self.assertIn(config_name, self.environment.configurations)
        self.assertEqual(self.environment.configurations[config_name].get_config_value(), config_value)

    def test_update_configuration(self):
        config_name = 'database'
        initial_value = {'url': 'localhost', 'port': 5432}
        new_value = {'url': 'localhost', 'port': 5433}
        self.environment.add_configuration(config_name, initial_value)
        self.environment.update_configuration(config_name, new_value)
        self.assertEqual(self.environment.configurations[config_name].get_config_value(), new_value)

    def test_delete_configuration(self):
        config_name = 'database'
        config_value = {'url': 'localhost', 'port': 5432}
        self.environment.add_configuration(config_name, config_value)
        self.environment.delete_configuration(config_name)
        self.assertNotIn(config_name, self.environment.configurations)

class TestEnvironmentManager(unittest.TestCase):
    def setUp(self):
        self.repo_path = 'test_repo'
        self.env_mgr = EnvironmentManager(repo_path=self.repo_path)
        self.env_mgr.add_environment('development')
        self.env_mgr.add_environment('production')

    def tearDown(self):
        if os.path.exists(self.repo_path):
            shutil.rmtree(self.repo_path)

    def test_add_environment(self):
        self.assertIn('development', self.env_mgr.environments)
        self.assertIn('production', self.env_mgr.environments)

    def test_remove_environment(self):
        self.env_mgr.remove_environment('development')
        self.assertNotIn('development', self.env_mgr.environments)

    def test_compare_configurations(self):
        self.env_mgr.environments['development'].add_configuration('database', {'url': 'localhost', 'port': 5432})
        self.env_mgr.environments['production'].add_configuration('database', {'url': 'prod.db.com', 'port': 5432})
        comparison = self.env_mgr.compare_configurations('development', 'production', 'database')
        self.assertIn('differences', comparison)
        self.assertIn('url', comparison['differences'])

    @patch('config_manager.Repo')
    def test_git_commit(self, mock_repo):
        mock_repo.return_value.git.add = MagicMock()
        mock_repo.return_value.index.commit = MagicMock()
        self.env_mgr.git_commit('Test commit')
        mock_repo.return_value.git.add.assert_called_once_with(A=True)
        mock_repo.return_value.index.commit.assert_called_once_with('Test commit')

    @patch('config_manager.Repo')
    def test_git_push(self, mock_repo):
        mock_remote = MagicMock()
        mock_repo.return_value.remote.return_value = mock_remote
        self.env_mgr.git_push('origin', 'main')
        mock_remote.push.assert_called_once_with('main')

    @patch('config_manager.Repo')
    def test_git_pull(self, mock_repo):
        mock_remote = MagicMock()
        mock_repo.return_value.remote.return_value = mock_remote
        self.env_mgr.git_pull('origin', 'main')
        mock_remote.pull.assert_called_once_with('main')

if __name__ == '__main__':
    unittest.main()
