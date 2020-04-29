from .protobuffers import user_grpc, user_pb2

ROUTING = {
    'users': {
        'PROTO': user_pb2,
        'PROTO_RPC': user_grpc,
        'HOST': 'localhost:5300' 
    }
}