from src.grpc.client import grpc_client


stub = grpc_client('192.168.99.100')

from src.grpc.libs.python.user_pb2_grpc import user__pb2

request = user__pb2.isUserExistsRequest()
request.username = "billy2"

response = stub.isUserExists(request)
print(response)




