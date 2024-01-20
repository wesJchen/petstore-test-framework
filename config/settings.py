import yaml

"""
Setting up the auth url and token for API interface
"""

def load_config():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

"""
USAGE:
config = load_config()
AUTH_URL = config.get('authorization_url')
"""


