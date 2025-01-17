import grpc
from generated_files.helloworld_pb2 import HelloRequest
from generated_files.helloworld_pb2_grpc import GreeterStub


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GreeterStub(channel)
        request = HelloRequest(name='Juan')
        response = stub.SayHello(request)
        print(f'Greeter client received: {response.message}')

if __name__ == '__main__':
    run()
