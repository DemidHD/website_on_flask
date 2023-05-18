import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///films.db')
    SECRET_KEY = os.getenv('SECRET_KEY', '3d6f45a5fc12445dbac2f59c3b6c7cb1')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
