import grpc
from .jsonResponse import JsonResponse

# Cliente GRPC


class grpcClient(JsonResponse):

    # INICIALIZADOR DEL CLIENTE
    def __init__(self, prot, protRPC, host):
        self.prototype = prot
        self.protoRPC = protRPC
        self.host = host

    # METODO POST GRPC
    def post(self, **Data):

        try:
            channel = grpc.insecure_channel(self.host)
            print(Data)

            # OBTENER DATOS GRPC
            request = self.prototype.Data(**Data)
            # INIALIZAR METADATA
            metadata = []

            # VALIDAR SI EXISTE AUTHORIZACION

            # if Data['authorization']:
            #   metadata.append(('access_token', Data['authorization']))

            # INICIALIZAR CANAL
            stub = self.protoRPC.DataProcessorStub(channel)

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
            channel = grpc.insecure_channel(self.host)

            request = self.prototype.Empty()
            metadata = []
            if data['authorization']:
                metadata.append(('access_token', data['authorization']))

            stub = self.protoRPC.DataProcessorStub(channel)

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
            channel = grpc.insecure_channel(self.host)

            print(Data)

            request = self.prototype.Data(**Data)
            metadata = []
            if data['authorization']:
                metadata.append(('access_token', data['authorization']))

            stub = self.protoRPC.DataProcessorStub(channel)

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
            channel = grpc.insecure_channel(self.host)

            print(Data)

            request = self.prototype.Data(**Data)
            metadata = []
            if data['authorization']:
                metadata.append(('access_token', data['authorization']))

            stub = self.protoRPC.DataProcessorStub(channel)

            response = stub.DeleteData(request=request, metadata=metadata)

            return response

        except grpc.RpcError as e:
            ex = e.details()
            print(ex)
            status_code = e.code()
            self.throwException(ex)
        except ValueError:
            self.throwException('value_error')
