import grpc
from .jsonResponse import JsonResponse

class grpcClient(JsonResponse):

    def __init__(self, prot, protRPC, host):
        self.prototype = prot
        self.protoRPC = protRPC
        self.channel = grpc.insecure_channel(host)

    def post(self, **Data):

        try:

            print(Data)

            request = self.prototype.Data(**Data)

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.PostData(request)

            return response

        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throwException(status_code.name)
        except ValueError:
            self.throwException('value_error')

    def get(self):

        try:
            print('Make Request')
            request = self.prototype.Empty()
            
            print('Sending Request')
            stub = self.protoRPC.DataProcessorStub(self.channel)
            print('Make Stub')

            response = stub.GetData(request)
            print('Return Response')
            return response
        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throwException(status_code.name)
        except ValueError:

            self.throwException("value_error")

    def put(self, **Data):

        try:

            print(Data)

            request = self.prototype.Data(**Data)

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.PutData(request)

            return response

        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throwException(status_code.name)
        except ValueError:
            self.throwException('value_error')
    
    def delete(self, **Data):

        try:

            print(Data)

            request = self.prototype.Data(**Data)

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.DeleteData(request)

            return response

        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throwException(status_code.name)
        except ValueError:
            self.throwException('value_error')
