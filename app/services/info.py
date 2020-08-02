from flask_restplus import Resource
from app.common import check_exceptions, last_tag, last_commit, last_commit_datetime, log_request
import app


class InfoApi(Resource):

    @log_request
    @check_exceptions
    def get(self):
        info_return = {
            "version": self.get_service_version(),
            "environment": app.app.config['ENVIRONMENT'],
            "commit_datetime": self.get_commit_datetime(),
            "server_datetime": self.get_server_datetime(),
            "environment_variables": [
                {"LOG_PATH": app.app.config['LOG_PATH']},
                {"SERVICE_NAME": app.app.config['SERVICE_NAME']},
                {"DEPENDENCY_API_A_URL": app.app.config['DEPENDENCY_API_A_URL']},
                {"DEPENDENCY_API_B_URL": app.app.config['DEPENDENCY_API_B_URL']}]
        }
        return info_return, 200

 def get_service_version(self):
        return last_commit() if app.config_name == 'development' else last_tag()

