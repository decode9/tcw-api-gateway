from .protobuffers import user_pb2_grpc, user_pb2, countries_pb2_grpc, countries_pb2, auth_pb2, auth_pb2_grpc, register_pb2, register_pb2_grpc #IMPORTACION DE PROTOCOL BUFFERS

ROUTING = {
    'users': { #NOMBRE DE LA RUTA
        'PROTO': user_pb2, #ASIGNACION DE PROTO BUFFER
        'PROTO_RPC': user_pb2_grpc, #ASIGNACION DE PROTO BUFFER GRPC
        'HOST': 'localhost:5300' #UBICACION DE RED DEL MICROSERVICIO
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
