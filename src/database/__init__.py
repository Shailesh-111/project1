from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from src.config import setting
db = SQLAlchemy()
engine = create_engine(setting.SQLALCHEMY_DATABASE_URI)
