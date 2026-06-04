from api.base_api import BaseApi

class LoginApi(BaseApi):
    def login(self,mobile,password,device_type="android"):
        data={
            "mobile":mobile,
            "password":password,
            "device_type":device_type
        }
        return self.post("/api/v1/auth/login",json_data= data)

    def profile(self):
        return self.get("/api/v1/user/profile")