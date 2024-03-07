import os

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    os.system("uvicorn src.apis.end_point:user_route --reload --port 5000")
