#!/usr/bin/python3

from flask import Flask
from flask_restful import Resource, Api

app1 = Flask('')
api = Api(app1)


class Video(Resource):
    def get(self):
        return 'Hello World!'

api.add_resource(Video, '/')

if __name__ == '__main__':
    app1.run()
