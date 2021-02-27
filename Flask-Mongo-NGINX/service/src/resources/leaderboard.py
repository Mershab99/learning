from flask_restful import Resource


class Get(Resource):
    @staticmethod
    def get():
        return {
            'test': True
        }
