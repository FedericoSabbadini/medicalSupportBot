from dotenv import load_dotenv
import os
from src.server import Server
from src.model import Model


if __name__ == "__main__":
    
    load_dotenv()
    key = os.getenv("DB_KEY")
    url = os.getenv("DB_URL")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    model = Model(url, key, anthropic_api_key) # type: ignore
    server = Server(model) # type: ignore
    server.run()

