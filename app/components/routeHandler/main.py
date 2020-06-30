from flask import request
from flask_restful import Resource
from ...utils import JsonResponse
import json



class routeHandler(Resource, JsonResponse):
    ROUTING = set()

    def operation(self, url, method):
        try:
            
            #Se toman las rutas del sistema
            ROUTING = self.ROUTING

            #Inicializar la variable de datos
            data = dict()

            #Si existe el header de Authorization lo asigna a la variable authorization
            if 'Authorization' in request.headers:
                data['authorization'] = request.headers['Authorization']
            
            #VERIFICA RUTA
            if url in ROUTING:

                #INICIA EL CLIENTE GRPC
                if request.data:
                    data['request'] = json.loads(request.data.decode())
                
                if method in ROUTING[url].keys():
                    response = ROUTING[url][method]['FUNCTION'](**data)
                    return self.apiResponse(response)

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
