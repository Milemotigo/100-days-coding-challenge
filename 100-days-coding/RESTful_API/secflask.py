#!/usr/bin/python

from flask_restful import Resource, Api
from flask import Flask
app = Flask('requestapi')
api = Api(app)

class Home(Resource):
    def get(self):
        return {'message': 'Welcome to the Home Page'}

    def post(self):
        data = request.get_json()
        # Process the data received in the POST request
        return {'message': 'Data received successfully'}

# Later, in your Flask application, you can add this resource to an API instance.
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run()
