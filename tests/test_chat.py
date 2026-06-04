import os
import pytest
from api.chat_api import ChatApi
from common.assert_util import assert_common_response
from common.yaml_util import load_yaml



BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH=os.path.join(BASE_DIR,"data","chat_cases.yaml")
CHAT_CASE=load_yaml(DATA_PATH)

@pytest.mark.parametrize("case",CHAT_CASE,ids=[case["title"] for case in CHAT_CASE])
def test_send_message(case,base_url,auth_headers):
    api=ChatApi(base_url=base_url,headers=auth_headers)
    request_data=case["request"]
    expected_data=case["expected"]

    response=api.send_message(
        to_user_id=request_data["to_user_id"],
        msg_type=request_data["msg_type"],
        content=request_data["content"]
    )

    assert response.status_code==200
    resp_json=response.json()
    assert_common_response(resp_json,expected_data["code"],expected_data["msg"])

    if expected_data["code"]==0:
        assert "msg_id" in resp_json["data"]
        assert resp_json["data"]["content"]==request_data["content"]