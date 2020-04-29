from flask_restful import Resource
from ...utils import JsonResponse, grpcClient
from google.protobuf.json_format import MessageToDict


class routeHandler(Resource, JsonResponse):
    ROUTING = set()

    def operation(self, url, method):
        try:
            ROUTING = self.ROUTING

            for route in ROUTING:
                print(route)
                if route == url:
                    client = grpcClient(
                        ROUTING[route]['PROTO'], ROUTING[route]['PROTO_RPC'], ROUTING[route]['HOST']
                    )
                    if method == 'GET':
                        response = client.get()

                    if method == 'POST':

                        #   form = ROUTING[route]['VALIDATOR'](request.data)
                        #   if not(form.is_valid()):
                        #   self.throwException(form.errors)

                        response = client.save(**request.data)

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
