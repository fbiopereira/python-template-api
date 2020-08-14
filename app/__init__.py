from flask import Flask, Blueprint
from flask_restplus import Api, Namespace
from config import config
<<<<<<< HEAD
=======
from .services import HealthApi, InfoApi
>>>>>>> 3a15b94a1b84ea0c9f8c71f5e443bee120f3835e
from app.custom_log import CustomLog
from app.helpers import get_service_version
import os
from prometheus_flask_exporter import PrometheusMetrics
from app.services import *
from app.services import support_namespace
from app.services.v1 import v1_namespace

config_name = os.environ.get('ENVIRONMENT')

log = CustomLog(get_service_version(), service_name=os.environ.get('SERVICE_NAME'), log_path=os.environ.get('LOG_PATH'))

flask_app = Flask(__name__)
metrics = PrometheusMetrics(flask_app)

flask_app.config.from_object(config[config_name])

flask_app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ['get', 'post']



api = Api(app=flask_app,  doc="/docs", version=get_service_version(),
          title="Python Template API", description="Template de projeto de API Flask <style>.models {display: none !important}</style>",
          validate=True, catch_all_404s=False)

api.add_namespace(support_namespace.support_namespace, path="/monit")
api.add_namespace(v1_namespace.v1_namespace, path="/api/v1")

<<<<<<< HEAD

=======
log = CustomLog(get_service_version(), service_name=os.environ.get('SERVICE_NAME'), log_path=os.environ.get('LOG_PATH'))
service_version = get_service_version()
api = Api(app, prefix="/api", doc="/docs/", title="Python Template API", description="Template de projeto de API Flask")


api.add_resource(HealthApi, '/healthcheck')
api.add_resource(InfoApi, '/info')
>>>>>>> 3a15b94a1b84ea0c9f8c71f5e443bee120f3835e
