import time
import grpc
from concurrent import futures
from generated_files import helloworld_pb2
from generated_files import helloworld_pb2_grpc

class GreeterService(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        name = request.name
        response = helloworld_pb2.HelloResponse(message=f"Hello {name} >:O")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port('[::]:50051')
    
    # Start the server
    server.start()
    print("Server is running on port 50051...")
    
    try:
        # Keep the server running indefinitely
        while True:
            time.sleep(86400)  # Sleep for a day (in seconds)
    except KeyboardInterrupt:
        server.stop(0)  # Stop the server on KeyboardInterrupt


if __name__ == '__main__':
    serve()
