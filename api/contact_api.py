from api.base_api import BaseApi

class ContactApi(BaseApi):
    def add_friend(self,friend_user_id,remark=""):
        data={
            "friend_user_id":friend_user_id,
            "remark":remark
        }
    def friend_list(self):
        return self.get("/api/v1/contact/list")