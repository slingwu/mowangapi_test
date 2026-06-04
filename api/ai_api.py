from api.base_api import BaseApi

class AiApi(BaseApi):
    def chat(self,question):
        return self.post("/api/v1/ai/chat",json_data={"question":question})