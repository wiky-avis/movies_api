import os
from envparse import Env

env = Env()

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))


class Config:
    DEBUG = env.bool("DEBUG", default=False)
    SECRET_KEY = env.str("SECRET_KEY", default="secret_key")
    HOST = env.str("HOST", default="127.0.0.1")
    PORT = env.int("PORT", default=8000)
