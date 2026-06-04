from api.base_api import BaseApi

class WalletApi(BaseApi):
    def balance(self):
        return self.get("/api/v1/wallet/balance")
    def transfer(self,to_user_id,amount,remark=""):
        data={
            "to_user_id":to_user_id,
            "amount":amount,
            "remark":remark
        }
        return self.post("/api/v1/wallet/transfer",json_data=data)

    def send_redpacket(self,to_user_id,amount,greeting=""):
        data={
            "to_user_id":to_user_id,
            "amount":amount,
            "greeting":greeting
        }
        return self.post("/api/v1/wallet/send_redpacket",json_data=data)

    def receive_redpacket(self,redpacket_id):
        return self.post("/api/v1/wallet/receive_redpacket",json_data={"redpacket_id":redpacket_id})