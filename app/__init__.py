from flask import Flask

from settings.config import Config

app = Flask('movies_service')
app.config.from_object(Config)

from flask_cors import CORS

from app.api.v1.handlers.views import *

CORS(app)
