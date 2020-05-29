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
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError:
            self.throwException('value_error')

    def get(self, **data):

        try:

            request = self.prototype.Empty()
            metadata = []
            if data['authorization']:
                metadata.append(('access_token', data['authorization']))

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.GetData(request=request, metadata=metadata)

            return response
        except grpc.RpcError as e:
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError as e:
            print(e)
            self.throwException("value_error")

    def put(self, **Data):

        try:

            print(Data)

            request = self.prototype.Data(**Data)

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.PutData(request)

            return response

        except grpc.RpcError as e:
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
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
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError:
            self.throwException('value_error')
