import os
import sys
import pytest
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0,BASE_DIR)



from api.login_api import LoginApi
from common.http_client import HttpClient
from common.yaml_util import load_yaml



CONFIG_PATH=os.path.join(BASE_DIR,"config","config.yaml")

@pytest.fixture(scope="session")
def config_data():
    return load_yaml(CONFIG_PATH)

@pytest.fixture(scope="session")
def base_url(config_data):
    return config_data["base_url"]

@pytest.fixture(scope="session")
def default_headers(config_data):
    return config_data["default_headers"].copy()

@pytest.fixture(scope="session")
def login_token(base_url,config_data):
    sender=config_data["test_user"]["sender"]
    login_api=LoginApi(base_url=base_url)

    response=login_api.login(
        mobile=sender["mobile"],
        password=sender["password"],
        device_type="android"
    )
    assert response.status_code==200,response.text
    resp_json=response.json()
    assert resp_json["code"]==0,resp_json
    assert "token" in resp_json["data"],resp_json
    return resp_json["data"]["token"]

@pytest.fixture(scope="session")
def auth_client(base_url,default_headers,login_token):
    client=HttpClient(base_url=base_url,default_headers=default_headers)
    client.set_token(login_token)
    client.update_headers({"X-Device-Type":"android"})
    return client

@pytest.fixture(scope="session")
def auth_headers(config_data,login_token):
    headers=config_data["default_headers"].copy()
    headers["Authorization"]=f"Bearer {login_token}"
    headers["X-Device-Type"]="android"
    return headers

@pytest.fixture(scope="session")
def chat_api(base_url,auth_client):
    from api.chat_api import ChatApi
    return ChatApi(base_url=base_url,client=auth_client)

