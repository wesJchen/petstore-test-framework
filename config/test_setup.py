from config import load_config

def setup():
    config = load_config()
    authorization_url = config.get('authorization_url')

    #Performs the setup for connecting to the authorization url

