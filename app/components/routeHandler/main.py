from flask import request
from flask_restful import Resource
from ...utils import JsonResponse, grpcClient
import json
from google.protobuf.json_format import MessageToDict


class routeHandler(Resource, JsonResponse):
    ROUTING = set()

    def operation(self, url, method):
        try:
            ROUTING = self.ROUTING

            for route in ROUTING:
                if route == url:

                    client = grpcClient(
                        ROUTING[route]['PROTO'], ROUTING[route]['PROTO_RPC'], ROUTING[route]['HOST']
                    )

                    if method == 'GET':
                        response = client.get()

                    if method == 'POST':

                        data = json.loads(request.data.decode())

                        #form = ROUTING[route]['VALIDATOR'](request.data)
                        # if not(form.is_valid()):
                        # self.throwException(form.errors)

                        response = client.save(**data)

                    if method == 'PUT':

                        data = json.loads(request.data.decode())

                        #form = ROUTING[route]['VALIDATOR'](request.data)
                        # if not(form.is_valid()):
                        # self.throwException(form.errors)

                        response = client.put(**data)

                    if method == 'DELETE':

                        data = json.loads(request.data.decode())

                        #form = ROUTING[route]['VALIDATOR'](request.data)
                        # if not(form.is_valid()):
                        # self.throwException(form.errors)

                        response = client.delete(**data)

                    return self.apiResponse(MessageToDict(response))

            return self.throwError('no exist')
        except:
            raise

    def get(self, route):
        try:
            return self.operation(route, 'GET')
        except:
            raise

    def post(self, route):
        try:
            return self.operation(route, 'POST')
        except:
            raise

    def put(self, route):
        try:
            return self.operation(route, 'PUT')
        except:
            raise

    def delete(self, route):
        try:
            return self.operation(route, 'DELETE')
        except:
            raise
