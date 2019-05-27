from flask import json, jsonify
#from myapp.views import app
from flask_restful import Resource, Api, reqparse
import jwt
import datetime
import random

requests = [
    {
        'request_id': 0,
        'username': 'Hasifa',
        'department': 'IT',
        'Request_type': 'Maintenance',
        'Date': '12/01/2019',
        'Description': 'The AC',
        'status': 'Approved'
    },
    {
        'request_id': 1,
        'username': 'Nansambu',
        'department': 'Accounts',
        'Request_type': 'Maintenance',
        'Date': '12/01/2019',
        'Description': 'The AC',
        'status': 'Declined'
    },
    {
        'request_id': 2,
        'username': 'Carol',
        'department': 'HR',
        'Request_type': 'Repairs',
        'Date': '12/01/2019',
        'Description': 'The AC',
        'status': ' '
    }
]


class Requests:
    def create_request(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='Field is required')
        parser.add_argument('department', required=True, help='Field is required')
        parser.add_argument('Request_type', required=True, help='Field is required')
        #parser.add_argument('Date', required=True, help='Field is required')
        parser.add_argument('Description', required=True, help='Field is required')

        args = parser.parse_args()

        new_request = {
            'username': args['username'],
            'department': args['department'],
            'Request_type': args['Request_type'],
            'Date': datetime.datetime.now(),
            'Description': args['Description'],
            #'status': args['status']
        }

        requests.append(new_request)
        return {'message': 'Your request has been sent successfully!!'}, 201

    def get_all_requests(self):
        if requests:
            return jsonify(requests)
        else:
            return {'message': 'No requests found!!'}, 404

    def get_request(self, request_id):
        for request in requests:
            if request_id == request["request_id"]:
                return request, 200
            else:
                return {'message': 'No request found!!'}, 404

    def delete_request(self, request_id):
        for request in requests:
            if request_id == request["request_id"]:
                del request
                return 'Request successfully deleted.', 200
            else:
                return {'message': 'No request found!!'}, 404

    def update_request(self, request_id):
        parser = reqparse.RequestParser()
        parser.add_argument('status', required=True, help='Field is required')

        args = parser.parse_args()

        for request in requests:
            if request_id == request["request_id"]:
                if request["status"] == '':
                    request["status"] = args["status"]
                    return 'Request successfully updated', 200
        requests.append(request)
        return {'message': 'Request status successfully updated'}, 201





