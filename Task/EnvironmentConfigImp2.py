import json
from datetime import datetime

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

    def export_configurations(self, file_path: str):
        data = {env_name: env.configurations for env_name, env in self.environments.items()}
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Configurations exported to {file_path}")

    def import_configurations(self, file_path: str):
        with open(file_path, 'r') as f:
            data = json.load(f)
            for env_name, configs in data.items():
                if env_name not in self.environments:
                    self.add_environment(env_name)
                for config_name, config_value in configs.items():
                    self.environments[env_name].add_configuration(config_name, config_value)
        print(f"Configurations imported from {file_path}")

# Example usage:
env_mgr = EnvironmentManager()
env_mgr.add_environment('development')
env_mgr.add_environment('production')

env_mgr.environments['development'].add_configuration('database', {'url': 'localhost', 'port': 5432})
env_mgr.environments['production'].add_configuration('database', {'url': 'prod.db.com', 'port': 5432})

# Export configurations to a file
env_mgr.export_configurations('configurations.json')

# Import configurations from a file
env_mgr.import_configurations('configurations.json')

# List environments to verify import
print("Environments list:", env_mgr.list_environments())
