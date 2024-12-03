import json

def load_config(file_path):
    """Load the JSON configuration from the given file path."""
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file {file_path} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in {file_path}.")
        return {}

if __name__ == "__main__":
    config = load_config('../config/firewall_rules.json')
    if config:
        print("Firewall configuration loaded successfully:")
        print(config)
