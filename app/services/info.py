<<<<<<< HEAD
from flask_restplus import Resource, fields
=======
from flask_restplus import Resource
>>>>>>> 3a15b94a1b84ea0c9f8c71f5e443bee120f3835e
from app.helpers import check_exceptions, log_request, get_service_version, get_server_datetime
import app
from .support_namespace import support_namespace


output_model = support_namespace.model('Info', {
    'version': fields.String,
    'environment': fields.String,
    'get_server_datetime': fields.String,
    'environment_variables': fields.String
})


@support_namespace.route("/info")
@support_namespace.response(200, 'Informações da API')
class InfoApi(Resource):

    @support_namespace.marshal_with(output_model, as_list=True, code=200)
    def get(self):
        info_return = {
            "version": get_service_version(),
<<<<<<< HEAD
            "environment": app.flask_app.config['ENVIRONMENT'],
=======
            "environment": app.config['ENVIRONMENT'],
>>>>>>> 3a15b94a1b84ea0c9f8c71f5e443bee120f3835e
            "server_datetime": get_server_datetime(),
            "environment_variables": [
                    {"LOG_PATH": app.flask_app.config['LOG_PATH']},
                    {"SERVICE_NAME": app.flask_app.config['SERVICE_NAME']},
                    {"DEPENDENCY_API_A_URL": app.flask_app.config['DEPENDENCY_API_A_URL']},
                    {"DEPENDENCY_API_B_URL": app.flask_app.config['DEPENDENCY_API_B_URL']}
                ]
            }

        return info_return, 200



