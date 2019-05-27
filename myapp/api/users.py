from flask import json, jsonify
#from myapp.views import app
from flask_restful import Resource, Api, reqparse
import jwt
import datetime

users = [
    {
        'username': 'Hasifa',
        'email': 'hasfanansambu@gmail.com',
        'password': 12345
    },
    {
        'username': 'Nansambu',
        'email': 'hasfa04@gmail.com',
        'password': 11111
    },
    {
        'username': 'Carol',
        'email': 'carol@gmail.com',
        'password': 22222
    },
    {
        'username': 'Lydia',
        'email': 'lydia@gmail.com',
        'password': 33333
    },
]


class User:
    def create_user(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='Field is required')
        parser.add_argument('email', required=True, help='Field is required')
        parser.add_argument('password', required=True, help='Field is required')

        args = parser.parse_args()

        for user in users:
            if user["username"] in users:
                return 'Username already exists', 400

        user = {
            "username": args['username'],
            "email": args["email"],
            "password": args["password"]
        }
        users.append(user)
        return {'message': 'User successfully created'}, 201

    def login_user(self):
        for user in users:
            if user['username'] == 'Admin' and user['password'] == 'Admin':
                return{'message': 'You have successfully logged in as Admin'}, 201

            elif user['username'] is None:
                return {'message': 'No account found with such a name. Please create an account'}, 404

            elif user['username'] and user['password'] in users:
                return{'message': 'You have successfully been logged in!!!'}, 201
            else:
                return {'message': 'Invalid username or password!!'}, 401

    def update_user(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='Field is required')
        parser.add_argument('email', required=True, help='Field is required')
        parser.add_argument('password', required=True, help='Field is required')

        args = parser.parse_args()

        for user in users:
            if username == user["username"] in users:
                user["email"] = args["email"]
                user["password"] = args['password']
                return 'User successfully update', 200

        user = {
            "username": args['username'],
            "email": args["email"],
            "password": args["password"]
        }
        users.append(user)
        return {'message': 'User successfully updated'}, 201

    def delete_user(self,username):
        for user in users:
            if username == user['username'] in users:
                del user
                return 'User sucessfully deleted', 200

    def get_all_users(self):
        if users:
            return jsonify(users)
        else:
            return 'No users found!!!'




