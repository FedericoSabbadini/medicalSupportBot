from dotenv import load_dotenv
import os
from src.server import Server


if __name__ == "__main__":
    
    load_dotenv()
    key = os.getenv("DB_KEY")
    url = os.getenv("DB_URL")

    server = Server(url, key) # type: ignore
    server.run()