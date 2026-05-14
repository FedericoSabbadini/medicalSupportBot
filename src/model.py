from src.loader import Loader
from src.llm import LLMmodel

class Model:
    def __init__(self, databaseURL: str, databaseKey: str, anthropic_api_key: str, name: str = "Medical Support LLM"):
        self.name = name
        self.databaseURL = databaseURL
        self.databaseKey = databaseKey
        self.anthropic_api_key = anthropic_api_key
        self.loader = Loader(databaseURL, databaseKey)
        self.llm = LLMmodel(databaseURL, model="claude-opus-4-6", api_key=anthropic_api_key)


    def ask(self, question: str, AIC: str):

        title, text_url1, text_url2 = self.loader.load(AIC) 
        answer = self.llm.answer(question, title, text_url1, text_url2) # type: ignore

        return answer


    def __str__(self):
        return f"Model(name={self.name}, databaseURL={self.databaseURL})"