from flask import Flask
from flask_restplus import Api
from config import config
from .services import HealthApi, InfoApi
from app.log import MscLog
from app.helpers import last_tag
import os


config_name = os.environ.get('ENVIRONMENT')

app = Flask(__name__)
app.config.from_object(config[config_name])

log = MscLog(last_tag(), service_name=os.environ.get('SERVICE_NAME'), log_path=os.environ.get('LOG_PATH'))

api = Api(app, prefix="/api")
api.add_resource(HealthApi, '/healthcheck')
api.add_resource(InfoApi, '/info')
