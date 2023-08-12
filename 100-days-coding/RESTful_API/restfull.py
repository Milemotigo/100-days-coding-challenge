#!/usr/bin/python3

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

movies = {
        'movie1': {'title': 'in time'},
        'movie2': {'title': 'gang of lagos'}
        }
class Movie(Resource):
    def get(self, movie_id):
        movie = movies.get[movie_id]
        if movie:
            return movie[movie_id]
        return 'i love movies'

api.add_resource(Movie, '/<movie_id>')

if __name__ == '__main__':
    app.run(debug=True)
