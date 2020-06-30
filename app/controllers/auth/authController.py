from ...utils import grpcClient
from ...protobuffers import user_pb2_grpc, user_pb2
from google.protobuf.json_format import MessageToDict


class userController(grpcClient):

    def __init__(self):
        self.proto = user_pb2
        self.protoRPC = user_pb2_grpc
        self.host = 'localhost:5300'

    def get_method(request**):

        grpcData = MessageToDict(
            self.get(authorization=request['authorization']))

        return grpcData
