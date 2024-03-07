import os
from dotenv import load_dotenv

load_dotenv()

class Config():

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    # debug: bool = os.environ.get("DEBUG")

config = Config()