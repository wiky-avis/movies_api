import os

from envparse import Env


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = Env()

env.read_envfile(os.path.join(BASE_PATH, ".env"))


class Config:
    DEBUG = env.bool("DEBUG", default=False)
    SECRET_KEY = env.str("SECRET_KEY", default="secret_key")
    HOST = env.str("HOST", default="127.0.0.1")
    PORT = env.int("PORT", default=8000)
