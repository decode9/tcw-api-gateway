# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import auth_pb2 as auth__pb2


class DataProcessorStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetData = channel.unary_unary(
                '/auth.DataProcessor/GetData',
                request_serializer=auth__pb2.Empty.SerializeToString,
                response_deserializer=auth__pb2.Empty.FromString,
                )
        self.PostData = channel.unary_unary(
                '/auth.DataProcessor/PostData',
                request_serializer=auth__pb2.Data.SerializeToString,
                response_deserializer=auth__pb2.DataResponse.FromString,
                )
        self.PutData = channel.unary_unary(
                '/auth.DataProcessor/PutData',
                request_serializer=auth__pb2.Data.SerializeToString,
                response_deserializer=auth__pb2.DataResponse.FromString,
                )
        self.DeleteData = channel.unary_unary(
                '/auth.DataProcessor/DeleteData',
                request_serializer=auth__pb2.Data.SerializeToString,
                response_deserializer=auth__pb2.Empty.FromString,
                )


class DataProcessorServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataProcessorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=auth__pb2.Empty.FromString,
                    response_serializer=auth__pb2.Empty.SerializeToString,
            ),
            'PostData': grpc.unary_unary_rpc_method_handler(
                    servicer.PostData,
                    request_deserializer=auth__pb2.Data.FromString,
                    response_serializer=auth__pb2.DataResponse.SerializeToString,
            ),
            'PutData': grpc.unary_unary_rpc_method_handler(
                    servicer.PutData,
                    request_deserializer=auth__pb2.Data.FromString,
                    response_serializer=auth__pb2.DataResponse.SerializeToString,
            ),
            'DeleteData': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteData,
                    request_deserializer=auth__pb2.Data.FromString,
                    response_serializer=auth__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.DataProcessor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataProcessor(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.DataProcessor/GetData',
            auth__pb2.Empty.SerializeToString,
            auth__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.DataProcessor/PostData',
            auth__pb2.Data.SerializeToString,
            auth__pb2.DataResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.DataProcessor/PutData',
            auth__pb2.Data.SerializeToString,
            auth__pb2.DataResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.DataProcessor/DeleteData',
            auth__pb2.Data.SerializeToString,
            auth__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)