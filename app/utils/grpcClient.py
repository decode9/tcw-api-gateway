import grpc
from .jsonResponse import JsonResponse

# Cliente GRPC

class grpcClient(JsonResponse):

    # INICIALIZADOR DEL CLIENTE
    def __init__(self, prot, protRPC, host):
        self.prototype = prot
        self.protoRPC = protRPC
        self.channel = grpc.insecure_channel(host)

    # METODO POST GRPC
    def post(self, **Data):

        try:
            print(Data)

            # OBTENER DATOS GRPC
            
            # INIALIZAR METADATA
            metadata = []

            # VALIDAR SI EXISTE AUTHORIZACION
            
            if 'authorization' in Data.keys():
                if Data['authorization']:
                    metadata.append(('access_token', Data['authorization']))
                del Data['authorization']

            request = self.prototype.Data(**Data['request'])

            # INICIALIZAR CANAL
            stub = self.protoRPC.DataProcessorStub(self.channel)

            # CONSULTA GRPC Y OBTENCION DE RESPUESTA
            response = stub.PostData(request=request, metadata=metadata)

            return response

        except grpc.RpcError as e:
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError:
            self.throwException('value_error')

    # METODO GET GRPC
    def get(self, **data):

        try:

            request = self.prototype.Empty()
            metadata = []
            if 'authorization' in data.keys():
                if data['authorization']:
                    metadata.append(('access_token', data['authorization']))
                del data['authorization']

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.GetData(request=request, metadata=metadata)

            return response
        except grpc.RpcError as e:
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError as e:
            print(e)
            self.throwException("value_error")

    # METODO PUT GRPC
    def put(self, **Data):

        try:

            print(Data)

            
            metadata = []
            if 'authorization' in Data.keys():
                if Data['authorization']:
                    metadata.append(('access_token', Data['authorization']))
                del Data['authorization']

            request = self.prototype.Data(**Data['request'])

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.PutData(request=request, metadata=metadata)

            return response

        except grpc.RpcError as e:
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError:
            self.throwException('value_error')

    # METODO DELETE GRPC
    def delete(self, **Data):

        try:

            print(Data)

            
            metadata = []
            if 'authorization' in Data.keys():
                if Data['authorization']:
                    metadata.append(('access_token', Data['authorization']))
                del Data['authorization']

            request = self.prototype.Data(**Data['request'])

            stub = self.protoRPC.DataProcessorStub(self.channel)

            response = stub.DeleteData(request=request, metadata=metadata)

            return response

        except grpc.RpcError as e:
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError:
            self.throwException('value_error')
