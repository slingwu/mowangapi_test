from api.base_api import BaseApi

class ChatApi(BaseApi):
    def send_message(self,to_user_id,msg_type,content):
        data={
            "to_user_id":to_user_id,
            "msg_type":msg_type,
            "content":content
        }
        return self.post("/api/v1/chat/send",json_data= data)

    # def history(self,peer_user_id):
    #     return self.get("/api/v1/chat/history",params={"peer_user_id":peer_user_id})

    def read_message(self,msg_id):
        return self.post("/api/v1/chat/read",json_data={"msg_id":msg_id})

    def unread_count(self):
        return self.get("/api/v1/chat/unread/count")

    def sync_message(self,device_type,last_msg_id="msg_0000000"):
        data={
            "device_type":device_type,
            "last_msg_id":last_msg_id
        }
        return self.post("/api/v1/chat/sync",json_data=data)