from flask_restful import Resource


class Map(Resource):
    @staticmethod
    def get():
        return {
            'test': True
        }
