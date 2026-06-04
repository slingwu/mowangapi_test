import requests
from common.logger_util import get_logger

class HttpClient:
    def __init__(self,base_url,default_headers=None,timeout=10):
        self.base_url=base_url
        self.default_headers = default_headers or {}
        self.timeout=timeout
        self.logger=get_logger()
        self.session=requests.Session()

    def set_token(self,token):
        self.default_headers["Authorization"]=f"Bearer {token}"

    def update_headers(self,headers):
        if headers:
            self.default_headers.update(headers)

    def request(self,method,path,headers=None,**kwargs):
        url=f"{self.base_url}{path}"
        req_headers=self.default_headers.copy()
        if headers:
            req_headers.update(headers)
        self.logger.info(f"{method.upper()}{url}")
        self.logger.info(f"headers={req_headers}")

        if "params" in kwargs and kwargs["params"] is not None:
            self.logger.info(f"params={kwargs['params']}")
        if "json" in kwargs and kwargs["json"] is not None:
            self.logger.info(f"json={kwargs['json']}")

        response=self.session.request(
            method=method,
            url=url,
            headers=req_headers,
            timeout=self.timeout,
            **kwargs
        )

        self.logger.info(f"status_code={response.status_code}")
        self.logger.info(f"response={response.text}")
        return response

    def get(self,path,params=None,headers=None):
        return self.request("get",path,params=params,headers=headers)

    def post(self,path,json=None,headers=None):
        return self.request("post",path,json=json,headers=headers)
