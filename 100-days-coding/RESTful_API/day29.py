#!/usr/bin/python3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask('name') 
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('qualifications', type=str, required=True)
parser.add_argument('level', type=int,  required=True)

employees = [
        {
    'name': 'Alice',
    'qualificarions': 'Master',
    'level': 6
    },
    {
        'name': 'Ken',
        'qualificarions': 'Bachelor',
        'level': 18
        }
    ]
class Names(Resource):
    def get(self, name_id):
        for employee in employees:
            if employee['name'] == name_id:
                return employee
        return f"No employee found with the '{name_id}'"
    def post(self, name_id):
        parser = args.parse_args()
        new_empl = {'name': args['name'],
                    'qualifications': args['qualifications'],
                    'level': args['level']
                    }
        employees['name_id'] = new_empl
        return {name_id: employees[name_id]}


api.add_resource(Names, '/<name_id>')
if __name__ == '__main__':
    app.run()
