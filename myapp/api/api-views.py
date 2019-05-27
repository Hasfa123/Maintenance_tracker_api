from flask import jsonify, Flask
#from myapp import views
from requests import requests, Requests
from users import users, User
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to My Flask App'})

myUser = User()
myRequests = Requests()


class UserReg(Resource):
    def post(self):
        # Sign Up
        return myUser.create_user()


class UserLogin(Resource):
    def post(self):
        # Login user
        return myUser.login_user()

class AllUsers(Resource):
    def get(self):
        return myUser.get_all_users()

class UpdateUser(Resource):
    def put(self):
        return myUser.update_user()

class DeleteUser(Resource):
    def delete(self):
        return myUser.delete_user()

class AllRequests(Resource):
    # Create a request
    def post(self):
        return myRequests.create_request()

    def get(self):
        # Return all  requests'''
        return myRequests.get_all_requests()


class MyRequest(Resource):
    # get a specific request
    def get(self, request_id):
        return myRequests.get_request(request_id)

    # delete a specfic request
    def delete(self, request_id):
        return myRequests.delete_request(request_id)

    # update a specific request
    def put(self, request_id):
        return myRequests.update_request(request_id)

api.add_resource(UserReg, '/api/v1/auth/register')
api.add_resource(UserLogin, '/api/v1/auth/login')
api.add_resource(AllUsers, '/api/v1/users')
api.add_resource(UpdateUser, '/api/v1/users/<string:username>')
api.add_resource(DeleteUser, '/api/v1/users/<string:username>')
api.add_resource(AllRequests, '/api/v1/requests')
api.add_resource(MyRequest, '/api/v1/requests/<int:request_id>')


app.run(debug=True)

