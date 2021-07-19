from flask_restful import Resource


class Starter(Resource):
    def __init__(self, **kwargs):
        self.process = kwargs['process']

    def get(self):
        return self.process.begin()
