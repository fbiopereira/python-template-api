from flask import Flask
from flask_restplus import Api
from config import config
from .services import HealthApi, InfoApi
from app.custom_log import CustomLog
from app.helpers import get_service_version
import os


config_name = os.environ.get('ENVIRONMENT')

app = Flask(__name__)
app.config.from_object(config[config_name])

log = CustomLog(get_service_version(), service_name=os.environ.get('SERVICE_NAME'), log_path=os.environ.get('LOG_PATH'))
service_version = get_service_version()
api = Api(app, prefix="/api", doc="/docs/", title="Python Template API", description="Template de projeto de API Flask")


api.add_resource(HealthApi, '/healthcheck')
api.add_resource(InfoApi, '/info')
