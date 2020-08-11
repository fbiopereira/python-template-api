from flask_restplus import Resource
import app


class HealthApi(Resource):

    def get(self):
        return "It's alive", 200
