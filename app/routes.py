# IMPORTACION DE PROTOCOL BUFFERS
#from .protobuffers import countries_pb2_grpc, countries_pb2, auth_pb2, auth_pb2_grpc, register_pb2, register_pb2_grpc
from .controllers import userController

ROUTING = {
    'user': {
        'GET':{
            'FUNCTION': userController().get_method
        },
        'POST':{
            'FUNCTION': userController().post_method
        }
    }
    #'users': {  # NOMBRE DE LA RUTA
    #    'PROTO': user_pb2,  # ASIGNACION DE PROTO BUFFER
    #    'PROTO_RPC': user_pb2_grpc,  # ASIGNACION DE PROTO BUFFER GRPC
    #    'HOST': 'localhost:5300'  # UBICACION DE RED DEL MICROSERVICIO
    #},
    # 'countries': {
    #    'PROTO': countries_pb2,
    #    'PROTO_RPC': countries_pb2_grpc,
    #    'HOST': 'localhost:5400'
    # },
    # 'auth': {
    #    'PROTO': auth_pb2,
    #    'PROTO_RPC': auth_pb2_grpc,
    #    'HOST': 'localhost:5320'
    # },
    # 'register': {
    #    'PROTO': register_pb2,
    #    'PROTO_RPC': register_pb2_grpc,
    #    'HOST': 'localhost:5320'
    # }
}
