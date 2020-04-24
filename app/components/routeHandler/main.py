from flask_restful import Resource
from ...utils import JsonResponse

class routeHandler(Resource, JsonResponse):
    def operation(self, route):
        try:
            print(route)
            """ url = request.path_info.split('/')

            for route in ROUTING:
                if route == url[2]:
                    client = grpcClient(ROUTING[route]['PROTO'], ROUTING[route]['PROTO_RPC'], ROUTING[route]['HOST'])
                    if request.method == 'GET':
                        response = client.get()
            
                    if request.method == 'POST':

                        form = ROUTING[route]['VALIDATOR'](request.data)

                        if not(form.is_valid()): self.throw400(form.errors)

                        response = client.save(**request.data)

                    return self.apiResponse(MessageToDict(response))"""
            return self.apiResponse(route)
        except:
            raise

    def get(self, route):
        try:
            return self.operation(route)
        except:
            raise

    def post(self, route):
        try:
            return self.operation(route)
        except:
            raise
