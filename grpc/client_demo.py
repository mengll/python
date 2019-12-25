import grpc
import compute_pb2
import compute_pb2_grpc

_HOST = '127.0.0.1'
_PORT = '19999'


def main():
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = compute_pb2_grpc.ComputeStub(channel=channel)
        response = client.SayHello(compute_pb2.HelloRequest(helloworld="123456"))
    print("received: " + response.result)


if __name__ == '__main__':
    main()
————————————————
版权声明：本文为CSDN博主「_Tsun」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/sunt2018/article/details/90176015
