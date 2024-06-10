import argparse
import json
from datetime import datetime
from typing import Dict, List

class VersionedConfig:
    def __init__(self, content: dict, version: int):
        self.content = content
        self.version = version
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"Version {self.version} at {self.timestamp}"

class Configuration:
    def __init__(self, config_name: str, config_value: dict):
        self.config_name = config_name
        self.config_value = config_value
        self.version = 1
        self.timestamp = datetime.now()

    def get_config_value(self) -> dict:
        return self.config_value

    def set_config_value(self, new_value: dict):
        self.config_value = new_value
        self.version += 1
        self.timestamp = datetime.now()

class Environment:
    def __init__(self, name: str):
        self.name = name
        self.configurations = {}

    def add_configuration(self, config_name: str, content: dict):
        if config_name in self.configurations:
            print(f"Configuration {config_name} already exists. Use update_configuration to update it.")
        else:
            self.configurations[config_name] = content
            print(f"Configuration {config_name} added.")

    def update_configuration(self, config_name: str, content: dict):
        if config_name in self.configurations:
            self.configurations[config_name] = content
            print(f"Configuration {config_name} updated.")
        else:
            print(f"Configuration {config_name} does not exist. Use add_configuration to add it.")

    def delete_configuration(self, config_name: str):
        if config_name in self.configurations:
            del self.configurations[config_name]
            print(f"Configuration {config_name} deleted.")
        else:
            print(f"Configuration {config_name} does not exist.")

class EnvironmentManager:
    def __init__(self):
        self.environments = {}

    def add_environment(self, env_name: str):
        if env_name in self.environments:
            print(f"Environment {env_name} already exists.")
        else:
            self.environments[env_name] = Environment(env_name)
            print(f"Environment {env_name} added.")

    def remove_environment(self, env_name: str):
        if env_name in self.environments:
            del self.environments[env_name]
            print(f"Environment {env_name} removed.")
        else:
            print(f"Environment {env_name} does not exist.")

    def list_environments(self):
        return list(self.environments.keys())

    def compare_configurations(self, env1_name: str, env2_name: str, config_name: str) -> dict:
        if env1_name not in self.environments or env2_name not in self.environments:
            raise ValueError("One or both environments do not exist.")

        env1 = self.environments[env1_name]
        env2 = self.environments[env2_name]

        if config_name not in env1.configurations or config_name not in env2.configurations:
            raise ValueError("Configuration does not exist in one or both environments.")

        config1 = env1.configurations[config_name]
        config2 = env2.configurations[config_name]

        return {
            "env1_name": env1_name,
            "env1_config": config1,
            "env2_name": env2_name,
            "env2_config": config2,
            "differences": self._find_differences(config1, config2)
        }

    @staticmethod
    def _find_differences(config1: dict, config2: dict) -> dict:
        differences = {}
        keys = set(config1.keys()).union(set(config2.keys()))
        for key in keys:
            if config1.get(key) != config2.get(key):
                differences[key] = {"env1": config1.get(key), "env2": config2.get(key)}
        return differences

def main():
    env_mgr = EnvironmentManager()

    parser = argparse.ArgumentParser(description="Environment Manager CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Add environment command
    add_env_parser = subparsers.add_parser('add_env', help='Add a new environment')
    add_env_parser.add_argument('env_name', type=str, help='The name of the environment')

    # Remove environment command
    remove_env_parser = subparsers.add_parser('remove_env', help='Remove an environment')
    remove_env_parser.add_argument('env_name', type=str, help='The name of the environment')

    # List environments command
    list_envs_parser = subparsers.add_parser('list_envs', help='List all environments')

    # Add configuration command
    add_config_parser = subparsers.add_parser('add_config', help='Add a configuration to an environment')
    add_config_parser.add_argument('env_name', type=str, help='The name of the environment')
    add_config_parser.add_argument('config_name', type=str, help='The name of the configuration')
    add_config_parser.add_argument('config_value', type=str, help='The configuration value (JSON string)')

    # Update configuration command
    update_config_parser = subparsers.add_parser('update_config', help='Update a configuration in an environment')
    update_config_parser.add_argument('env_name', type=str, help='The name of the environment')
    update_config_parser.add_argument('config_name', type=str, help='The name of the configuration')
    update_config_parser.add_argument('config_value', type=str, help='The new configuration value (JSON string)')

    # Delete configuration command
    delete_config_parser = subparsers.add_parser('delete_config', help='Delete a configuration from an environment')
    delete_config_parser.add_argument('env_name', type=str, help='The name of the environment')
    delete_config_parser.add_argument('config_name', type=str, help='The name of the configuration')

    # Compare configurations command
    compare_configs_parser = subparsers.add_parser('compare_configs', help='Compare configurations between two environments')
    compare_configs_parser.add_argument('env1_name', type=str, help='The name of the first environment')
    compare_configs_parser.add_argument('env2_name', type=str, help='The name of the second environment')
    compare_configs_parser.add_argument('config_name', type=str, help='The name of the configuration to compare')

    args = parser.parse_args()

    if args.command == 'add_env':
        env_mgr.add_environment(args.env_name)
    elif args.command == 'remove_env':
        env_mgr.remove_environment(args.env_name)
    elif args.command == 'list_envs':
        environments = env_mgr.list_environments()
        print("Environments:", environments)
    elif args.command == 'add_config':
        config_value = json.loads(args.config_value)
        env_mgr.environments[args.env_name].add_configuration(args.config_name, config_value)
    elif args.command == 'update_config':
        config_value = json.loads(args.config_value)
        env_mgr.environments[args.env_name].update_configuration(args.config_name, config_value)
    elif args.command == 'delete_config':
        env_mgr.environments[args.env_name].delete_configuration(args.config_name)
    elif args.command == 'compare_configs':
        comparison = env_mgr.compare_configurations(args.env1_name, args.env2_name, args.config_name)
        print("Comparison:", comparison)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
