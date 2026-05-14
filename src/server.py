from fastapi import FastAPI
import requests
import uvicorn

class Server:
    def __init__(self, databaseURL: str, databaseKey: str, host: str = "0.0.0.0", port: int = 8000, name: str = "Medical Support Bot"):

        self.app = FastAPI()
        self.databaseURL = databaseURL
        self.databaseKey = databaseKey
        self.host = host
        self.localhost = "127.0.0.1"
        self.port = port
        self.name = name

        @self.app.get("/")
        def database(question: str, AIC: str):
            response = requests.get(
                self.databaseURL, 
                headers={"xc-token": self.databaseKey}, 
            )
            data = response.json()

            for item in data["list"]:
                item_title = item["Title"]
                item_url1 = item["URL1"]
                item_url2 = item["URL2"]
                item_AIC = item["AIC"]

                if item_AIC == AIC:
                    context = {
                        "Title": item_title,
                        "URL1": item_url1,
                        "URL2": item_url2,
                        "AIC": item_AIC
                    }

            response = 'Retry later, bot with LLM is being trained.'
            # here i have to implement an llm to generate a response based on the question and 
            # the context. It should work by RAG (Retrieval-Augmented Generation) where the 
            # context is retrieved from the database URL1 e URL2 and then used to generate a 
            # response to the question.

            return {'answer': {
                'question': question,
                'response': response,
                'context': context
            }}
        
    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port)

    def run_local(self):
        uvicorn.run(self.app, host=self.localhost, port=self.port)

    def __str__(self):
        return f"Server(name={self.name}, host={self.host}, localhost={self.localhost}, port={self.port}, DatabaseURL={self.databaseURL})"