import pytest
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Calling a fixture to set up the api auth token
@pytest.fixture(scope='session', autouse=True)
def setup_api_auth(request, pytestconfig):
#    api_key = config['API']['api_key']
#    api_token = config['API']['api_token']
    api_key = pytestconfig.getoption('--api-key')
    api_token = pytestconfig.getoption('--api-token')

    # Authentification setup
    headers = {
        'Authorization': f'Bearer{api_token}',
        'X-API-Key': api_key,
    }
    request.config.cache.set('api_headers', headers, scope='session')

# Session setup
@pytest.hookimpl
def pytest_sessionstart(session):
    print("Test session is setting up")

@pytest.hookimpl
def pytest_sessionend(session):
    print("Test session is tearing down")