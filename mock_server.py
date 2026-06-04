from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class LoginRequest(BaseModel):
    mobile: str
    password: str
    device_type: str


class ChatSendRequest(BaseModel):
    to_user_id: int
    msg_type: str
    content: str


class ChatSyncRequest(BaseModel):
    device_type: str
    last_msg_id: str = "msg_000000"


class TransferRequest(BaseModel):
    to_user_id: int
    amount: float
    remark: str = ""


@app.post("/api/v1/auth/login")
def login(data: LoginRequest):
    if not data.mobile:
        return {
            "code": 1001,
            "msg": "mobile is required",
            "data": {},
            "trace_id": "trace_login_001"
        }

    if data.password != "123456":
        return {
            "code": 1004,
            "msg": "password error",
            "data": {},
            "trace_id": "trace_login_002"
        }

    return {
        "code": 0,
        "msg": "success",
        "data": {
            "token": f"mock_token_{data.mobile}_{data.device_type}",
            "user_id": 1001,
            "nickname": "默往用户",
            "device_type": data.device_type
        },
        "trace_id": "trace_login_003"
    }


@app.get("/api/v1/user/profile")
def profile(authorization: Optional[str] = Header(default=None)):
    if not authorization:
        return {
            "code": 1002,
            "msg": "unauthorized",
            "data": {},
            "trace_id": "trace_profile_001"
        }

    return {
        "code": 0,
        "msg": "success",
        "data": {
            "user_id": 1001,
            "nickname": "默往用户",
            "mobile": "18250860000"
        },
        "trace_id": "trace_profile_002"
    }


@app.post("/api/v1/chat/send")
def send_message(data: ChatSendRequest, authorization: Optional[str] = Header(default=None)):
    if not authorization:
        return {
            "code": 1002,
            "msg": "unauthorized",
            "data": {},
            "trace_id": "trace_chat_001"
        }

    if not data.content:
        return {
            "code": 1012,
            "msg": "content is required",
            "data": {},
            "trace_id": "trace_chat_002"
        }

    return {
        "code": 0,
        "msg": "success",
        "data": {
            "msg_id": "msg_000001",
            "from_user_id": 1001,
            "to_user_id": data.to_user_id,
            "msg_type": data.msg_type,
            "content": data.content,
            "read_status": "unread"
        },
        "trace_id": "trace_chat_003"
    }


@app.post("/api/v1/chat/sync")
def sync_message(data: ChatSyncRequest, authorization: Optional[str] = Header(default=None)):
    if not authorization:
        return {
            "code": 1002,
            "msg": "unauthorized",
            "data": {},
            "trace_id": "trace_sync_001"
        }

    return {
        "code": 0,
        "msg": "success",
        "data": {
            "device_type": data.device_type,
            "message_list": [
                {
                    "msg_id": "msg_000001",
                    "from_user_id": 1001,
                    "to_user_id": 1002,
                    "content": "下班一起去吃烤鱼啊"
                }
            ],
            "last_msg_id": "msg_000001"
        },
        "trace_id": "trace_sync_002"
    }


@app.get("/api/v1/wallet/balance")
def balance(authorization: Optional[str] = Header(default=None)):
    if not authorization:
        return {
            "code": 1002,
            "msg": "unauthorized",
            "data": {},
            "trace_id": "trace_wallet_001"
        }

    return {
        "code": 0,
        "msg": "success",
        "data": {
            "balance": 1000.0
        },
        "trace_id": "trace_wallet_002"
    }


@app.post("/api/v1/wallet/transfer")
def transfer(data: TransferRequest, authorization: Optional[str] = Header(default=None)):
    if not authorization:
        return {
            "code": 1002,
            "msg": "unauthorized",
            "data": {},
            "trace_id": "trace_wallet_003"
        }

    if data.amount <= 0:
        return {
            "code": 1001,
            "msg": "转账金额非法",
            "data": {},
            "trace_id": "trace_wallet_004"
        }

    if data.amount > 1000:
        return {
            "code": 1008,
            "msg": "余额不足",
            "data": {},
            "trace_id": "trace_wallet_005"
        }

    return {
        "code": 0,
        "msg": "success",
        "data": {
            "transfer_id": "tr_000001",
            "amount": data.amount,
            "status": "success"
        },
        "trace_id": "trace_wallet_006"
    }