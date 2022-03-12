# FlaskのConfigを提供する
import os

class DevelopmentConfig:
    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': os.environ.get("DEVELOPMENT_DB_USER"),
        'password': os.environ.get("DEVELOPMENT_DB_PASSWORD"),
        'host': os.environ.get("DEVELOPMENT_DB_HOST"),
        'db_name': os.environ.get("DEVELOPMENT_DB_NAME")
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig