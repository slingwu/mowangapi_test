import os
import pytest
from api.chat_api import ChatApi
from common.assert_util import assert_common_response
from common.yaml_util import load_yaml

DASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH=os.path.join(DASE_DIR,"data","sync_cases.yaml")
SYNC_CASES=load_yaml(DATA_PATH)

@pytest.mark.parametrize("case",SYNC_CASES,ids=[case["title"] for case in SYNC_CASES])
def test_sync(case,base_url,auth_headers):
    api=ChatApi(base_url=base_url,headers=auth_headers)
    request_data=case["request"]
    expected=case["expected"]

    response = api.sync_message(
        device_type=request_data["device_type"],
        last_msg_id=request_data.get("last_msg_id","msg_0000000")
    )

    assert response.status_code==200
    resp_json=response.json()
    assert_common_response(resp_json,expected["code"],expected["msg"])

    if expected["code"]==0:
        assert "message_list" in resp_json["data"]
        assert "last_msg_id" in resp_json["data"]