### 安装依赖
pip install grpcio
pip install protobuf
pip install grpcio_tools

### 生成Python文件
 python3 -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ event.proto 
 
 
### desc
# python_out目录指定 xxxx_pb2.py的输出路径，我们指定为./ 当前路径
# grpc_python_out指定xxxx_pb2_grpc.py文件的输出路径,我们指定为./ 当前路径
# grpc_tools.protoc 这是我们的工具包，刚刚安装的
# -I参数指定协议文件的查找目录，我们都将它们设置为当前目录./
# compute.proto 我们的协议文件

ls
compute_pb2_grpc.py  compute_pb2.py  compute.proto
# compute.proto 协议文件
# compute_pb2.py 里面有消息序列化类
# compute_pb2_grpc.py 包含了服务器 Stub 类和客户端 Stub 类，以及待实现的服务 RPC 接口。
————————————————
版权声明：本文为CSDN博主「_Tsun」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/sunt2018/article/details/90176015
