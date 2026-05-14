from src.model import Model
from fastapi import FastAPI
import requests
import uvicorn


class Server:
    def __init__(self, model: Model, host: str = "0.0.0.0", port: int = 8000, name: str = "Medical Support Server"):

        self.app = FastAPI()
        self.model = model

        self.host = host
        self.localhost = "127.0.0.1"
        self.port = port
        self.name = name

        @self.app.get("/")
        def database(question: str, AIC: str):
            answer = self.model.ask(question, AIC)
            return {
                "response": answer
            }
        
    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port)

    def run_local(self):
        uvicorn.run(self.app, host=self.localhost, port=self.port)


    def __str__(self):
        return f"Server(name={self.name}, host={self.host}, localhost={self.localhost}, port={self.port})"