# FlaskのConfigを提供する
import os

class DevelopmentConfig:
    # Flask
    DEBUG = True

    # SQLAlchemy
    # アクセス(接続)するDBのURIを記載する。
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': os.environ.get("DB_USER"),
        'password': os.environ.get("DB_PASSWORD"),
        'host': os.environ.get("DB_HOST"),
        'db_name': os.environ.get("DB_NAME")
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig