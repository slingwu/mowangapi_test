from common.http_client import HttpClient

class BaseApi:
    def __init__(self,base_url,headers=None,client=None):
        if client is not None:
            self.client=client
        else:
            self.client=HttpClient(base_url=base_url,default_headers=headers or {})

    def set_token(self,token):
        self.client.set_token(token)

    def post(self,path,json_data=None,headers=None):
        return self.client.post(path,json=json_data,headers=headers)

    def get(self,path,params=None,headers=None):
        return  self.client.get(path,params=params,headers=headers)