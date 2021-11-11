from flask import Flask

from settings.config import Config

app = Flask('movies_service')
app.config.from_object(Config)

from app.api.v1.handlers.views import *

from flask_cors import CORS

CORS(app)
