from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage

class LLMmodel:
    def __init__(self, url:str, model: str = "claude-3-opus-20241201", api_key: str = "your-anthropic-api-key"):
        self.llm = ChatAnthropic(model=model, api_key=api_key, temperature=0.7) # type: ignore

    def answer(self, question: str, title: str, file_1: str, file_2: str):
        messages = [
            SystemMessage(content=f"You are a helpful assistant in medical domain that answers questions based EXCLUSIVELY on the provided context, to answer customers questions about {title}."),
            SystemMessage(content=f"###Context: Illustrative Sheet --- {file_1}###"),
            SystemMessage(content=f"###Context: Product Features --- {file_2}###"),
            HumanMessage(content=question + " If the answer is not present in the context, say that you don't know and that you can't answer the question. Do not try to answer the question if you don't have the information in the context. ANSWER IN A CONCISE AND CORRECT MANNER.")
        ]

        response = self.llm.invoke(messages) # type: ignore

        return response.content