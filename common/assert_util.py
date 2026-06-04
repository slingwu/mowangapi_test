def assert_common_response(response_json, expected_code=0,expected_msg=None):
    assert "code"in response_json
    assert "msg"in response_json
    assert response_json["code"]==expected_code
    if  expected_msg is not None:
        assert response_json["msg"]==expected_msg