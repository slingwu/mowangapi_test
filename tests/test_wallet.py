import os
import pytest
from api.wallet_api import WalletApi
from common.yaml_util import load_yaml
from common.assert_util import assert_common_response

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH=os.path.join(BASE_DIR,"data","wallet_cases.yaml")
WALLET_CASES=load_yaml(DATA_PATH)

@pytest.mark.parametrize("case",WALLET_CASES,ids=[case["title"] for case in WALLET_CASES])
def test_transfer(case,base_url,auth_headers):
    api=WalletApi(base_url=base_url,headers=auth_headers)
    request_data=case["request"]
    expected=case["expected"]

    response=api.transfer(
        to_user_id=request_data["to_user_id"],
        amount= request_data["amount"],
        remark=request_data["remark"]
    )

    assert response.status_code==200
    resp_json=response.json()
    assert_common_response(resp_json,expected["code"],expected["msg"])

    if expected["code"]==0:
        assert resp_json["data"]["amount"] == request_data["amount"]
        assert  resp_json["data"]["status"] == "success"
