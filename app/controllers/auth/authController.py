from ...utils import grpcClient
from ...protobuffers import auth_pb2_grpc, auth_pb2, register_pb2_grpc, register_pb2
from google.protobuf.json_format import MessageToDict

class authController():

    def __init__(self):
        self.authClient = grpcClient(auth_pb2, auth_pb2_grpc, 'localhost:5320')
        self.registerClient = grpcClient(
            register_pb2, register_pb2_grpc, 'localhost:5320')

    def auth_method(self, **request):

        print(request)
        grpcData = MessageToDict(self.authClient.post(**request))

        return grpcData

    def register_method(self, **request):

        print(request)
        grpcData = MessageToDict(self.registerClient.post(**request))

        return grpcData
