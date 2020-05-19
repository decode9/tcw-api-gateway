from .protobuffers import user_pb2_grpc, user_pb2, countries_pb2_grpc, countries_pb2, auth_pb2, auth_pb2_grpc, register_pb2, register_pb2_grpc

ROUTING = {
    'users': {
        'PROTO': user_pb2,
        'PROTO_RPC': user_pb2_grpc,
        'HOST': 'localhost:5300'
    },
    'countries': {
        'PROTO': countries_pb2,
        'PROTO_RPC': countries_pb2_grpc,
        'HOST': 'localhost:5400'
    },
    'auth': {
        'PROTO': auth_pb2,
        'PROTO_RPC': auth_pb2_grpc,
        'HOST': 'localhost:5320'
    },
    'register': {
        'PROTO': register_pb2,
        'PROTO_RPC': register_pb2_grpc,
        'HOST': 'localhost:5320'
    }
}
