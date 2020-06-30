from ...utils import grpcClient
from ...protobuffers import user_pb2_grpc, user_pb2
from google.protobuf.json_format import MessageToDict


class userController():

    def __init__(self):
        self.userClient = grpcClient(user_pb2, user_pb2_grpc, 'localhost:5300')

    def get_method(self, **request):

        print(request)

        grpcData = MessageToDict(
            self.userClient.get(**request))

        return grpcData

    def post_method(self, **request):

        print(request)

        grpcData = MessageToDict(self.userClient.post(**request))

        return grpcData

    def put_method(self, **request):

        print(request)

        grpcData = MessageToDict(self.userClient.put(**request))

        return grpcData

    def delete_method(self, **request):

        print(request)

        grpcData = MessageToDict(self.userClient.delete(**request))

        return grpcData
    

