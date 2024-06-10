import Environment
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

# Example usage:
env_mgr = EnvironmentManager()
env_mgr.add_environment('development')
env_mgr.add_environment('production')

env_mgr.environments['development'].add_configuration('database', {'url': 'localhost', 'port': 5432})
env_mgr.environments['production'].add_configuration('database', {'url': 'prod.db.com', 'port': 5432})

print("Environments list:", env_mgr.list_environments())

# Compare configurations
comparison = env_mgr.compare_configurations('development', 'production', 'database')
print("Configuration comparison:", comparison)

# Remove an environment
env_mgr.remove_environment('development')
print("Environments list after removal:", env_mgr.list_environments())
