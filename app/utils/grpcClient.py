import grpc
from .jsonResponse import JsonResponse

class grpcClient(JsonResponse):

    def __init__(self, prot, protRPC, host):
        self.prototype = prot
        self.protoRPC = protRPC
        self.channel = grpc.insecure_channel(host)

    def save(self, **Data):

        try:

            request = self.prototype.Data(**Data)

            stub = self.protoRPC.Stub(self.channel)

            response = stub.SaveData(request)

            return response

        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throwException(status_code.name)
        except ValueError:
            self.throwException('value_error')

    def get(self):

        try:

            request = self.prototype.Empty()
            stub = self.protoRPC.Stub(self.channel)
            response = stub.GetData(request)

            return response
        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throwException(status_code.name)
        except ValueError:

            self.throwException("value_error")
