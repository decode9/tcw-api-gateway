from ...utils import grpcClient
from ...protobuffers import user_pb2_grpc, user_pb2
from google.protobuf.json_format import MessageToDict


class userController(grpcClient):

    def __init__(self):
        self.prototype = user_pb2
        self.protoRPC = user_pb2_grpc
        self.host = 'localhost:5300'

    def get_method(self, **request):

        print(request)

        grpcData = MessageToDict(
            self.get(authorization=None))

        return grpcData

    def post_method(self, **request):

        print(request)

        grpcData = MessageToDict(self.post(**request))

        return grpcData
