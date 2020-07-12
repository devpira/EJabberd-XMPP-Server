import grpc
from concurrent import futures
import os
import json
# import the generated classes
from src.grpc.libs.python import user_pb2
from src.grpc.libs.python import user_pb2_grpc


# import the business logic
from src.components.user_model import UserModel


class UserService(user_pb2_grpc.UserServicer):

    def isUserExists(self, request, context):
        username = request.username
        user_model = UserModel()
        response = user_pb2.isUserExistsResponse()
        response.result = user_model.is_user_exits(username)
        return response


def serve():
    max_workers = os.getenv('MAX_WORKERS', 10)
    app_port = os.getenv('APP_PORT', 8001)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers))

    user_pb2_grpc.add_UserServicer_to_server(UserService(), server)

    print("Starting server. Listening on port {0}.".format(app_port))
    server.add_insecure_port("[::]:{0}".format(app_port))
    server.start()
    server.wait_for_termination()
