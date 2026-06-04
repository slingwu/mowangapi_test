import os
import pytest
from api.login_api import LoginApi
from common.yaml_util import load_yaml
from common.assert_util import assert_common_response

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH=os.path.join(BASE_DIR,"data","login_cases.yaml")
LOGIN_CASES=load_yaml(DATA_PATH)

@pytest.mark.parametrize("case",LOGIN_CASES,ids=[case["title"] for case in LOGIN_CASES])
def test_login(case,base_url):
    api = LoginApi(base_url=base_url)
    request_data = case["request"]
    expected=case["expected"]

    response=api.login(
        mobile=request_data["mobile"],
        password=request_data["password"],
        device_type=request_data["device_type"]
    )
    assert response.status_code==200
    resp_json=response.json()
    assert_common_response(resp_json,expected["code"],expected["msg"])

    if expected["code"]==0:
        assert "token" in resp_json["data"]
        assert "user_id" in resp_json["data"]