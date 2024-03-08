from flask import Flask
from src.apis.end_point import user
from src.config import setting
from src.database import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = setting.SQLALCHEMY_DATABASE_URI
    # app.config.from_object(setting.SQLALCHEMY_DATABASE_URI)
    db.init_app(app)
    app.register_blueprint(user, url_prefix='/v1/user')
    return app
app = create_app()