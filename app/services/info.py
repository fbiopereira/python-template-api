from flask_restplus import Resource
from app.helpers import check_exceptions, log_request, get_service_version, get_server_datetime
import app


class InfoApi(Resource):

    @log_request
    @check_exceptions
    def get(self):
        info_return = {
            "version": get_service_version(),
            "environment": app.config['ENVIRONMENT'],
            "server_datetime": get_server_datetime(),
            "environment_variables": [
            {"LOG_PATH": app.app.config['LOG_PATH']},
            {"SERVICE_NAME": app.app.config['SERVICE_NAME']},
            {"DEPENDENCY_API_A_URL": app.app.config['DEPENDENCY_API_A_URL']},
            {"DEPENDENCY_API_B_URL": app.app.config['DEPENDENCY_API_B_URL']}]
            }

        return info_return, 200



