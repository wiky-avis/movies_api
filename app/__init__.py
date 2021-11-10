from flask import Flask

from app.config import Config

app = Flask('movies_service')
app.config.from_object(Config)

from app.views import *
