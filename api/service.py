from flask import Flask, request
from flask_restful import Resource, Api
import processing
import resources


processor = processing.Process()
app = Flask(__name__)
api = Api(app)

api.add_resource(resources.Starter, "/start/", resource_class_kwargs={'process': processor})
api.add_resource(resources.Stopper, "/stop/", resource_class_kwargs={'process': processor})
api.add_resource(resources.Checker, "/alive/", resource_class_kwargs={'process': processor})

if __name__ == "__main__":
    app.run()
