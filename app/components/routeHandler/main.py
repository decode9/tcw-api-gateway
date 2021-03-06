from flask import request
from flask_restful import Resource
from ...utils import JsonResponse, grpcClient
import json
from google.protobuf.json_format import MessageToDict


class routeHandler(Resource, JsonResponse):
    ROUTING = set()

    def operation(self, url, method):
        try:
            print('Enter Routing')

            #Se toman las rutas del sistema
            ROUTING = self.ROUTING

            #Inicializar la variable de authorization
            authorization = None

            #Si existe el header de Authorization lo asigna a la variable authorization
            if 'Authorization' in request.headers:
                authorization = request.headers['Authorization']

            print('VERIFY ROUTE')
            #VERIFICA RUTA
            if url in ROUTING:

                print('Start Client')
                #INICIA EL CLIENTE GRPC
                client = grpcClient(
                    ROUTING[url]['PROTO'], ROUTING[url]['PROTO_RPC'], ROUTING[url]['HOST']
                )

                print('Get Client')
                
                #VERIFICA EL METODO CORRESPONDIENTE
                if method == 'GET':
                    response = client.get(authorization=authorization)

                if method == 'POST':
                    #ASIGNA DATA DEL REQUEST
                    data = json.loads(request.data.decode())

                    #form = ROUTING[route]['VALIDATOR'](request.data)
                    # if not(form.is_valid()):
                    # self.throwException(form.errors)

                    response = client.post(**data)

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

    #METODO GET API
    def get(self, route):
        try:
            print('enter get function')
            return self.operation(route, 'GET')
        except:
            raise

    #METODO POST API
    def post(self, route):
        try:
            return self.operation(route, 'POST')
        except:
            raise

    #METODO PUT API
    def put(self, route):
        try:
            return self.operation(route, 'PUT')
        except:
            raise

    #METODO DELETE API
    def delete(self, route):
        try:
            return self.operation(route, 'DELETE')
        except:
            raise
