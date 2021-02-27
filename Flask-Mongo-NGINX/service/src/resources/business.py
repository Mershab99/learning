from flask_restful import Resource


class Detail(Resource):
    @staticmethod
    def get():
        return {
            'test': True
        }


class Card(Resource):
    @staticmethod
    def get():
        return {
            'test': True
        }


class Create(Resource):
    @staticmethod
    def get():
        return {
            'test': True
        }


class Update(Resource):
    @staticmethod
    def get():
        return {
            'test': True
        }


class Delete(Resource):
    @staticmethod
    def get():
        return {
            'test': True
        }
