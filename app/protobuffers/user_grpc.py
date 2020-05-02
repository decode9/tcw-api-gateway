import grpc
from . import user_pb2 as user_proto


class Stub(object):

    def __init__(self, channel):
        self.UpdateData = channel.unary_unary(
            '/User/UpdateData',
            request_serializer=user_proto.Data.SerializeToString,
            response_deserializer=user_proto.DataResponse.FromString,
        )

        self.DeleteData = channel.unary_unary(
            '/User/DeleteData',
            request_serializer=user_proto.Data.SerializeToString,
            response_deserializer=user_proto.DataResponse.FromString,
        )

        self.SaveData = channel.unary_unary(
            '/User/SaveData',
            request_serializer=user_proto.Data.SerializeToString,
            response_deserializer=user_proto.DataResponse.FromString,
        )

        self.GetData = channel.unary_unary(
            '/User/GetData',
            request_serializer=user_proto.Empty.SerializeToString,
            response_deserializer=user_proto.DataMultipleResponse.FromString,
        )

class UserService(object):

    def SaveData(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetData(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateData(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteData(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add_service_to_server(self, service, server):
        rpc_method_handlers = {
            'SaveData': grpc.unary_unary_rpc_method_handler(
                service.SaveData,
                request_deserializer=user_proto.Data.FromString,
                response_serializer=user_proto.DataResponse.SerializeToString
            ),
            'GetData': grpc.unary_unary_rpc_method_handler(
                service.GetData,
                request_deserializer=user_proto.Empty.FromString,
                response_serializer=user_proto.DataMultipleResponse.SerializeToString
            ),
            'UpdateData': grpc.unary_unary_rpc_method_handler(
                service.UpdateData,
                request_deserializer=user_proto.Data.FromString,
                response_serializer=user_proto.DataResponse.SerializeToString
            ),
            'DeleteData': grpc.unary_unary_rpc_method_handler(
                service.DeleteData,
                request_deserializer=user_proto.Data.FromString,
                response_serializer=user_proto.DataResponse.SerializeToString
            ),
        }

        generic_handler = grpc.method_handlers_generic_handler(
            'User', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler, ))
