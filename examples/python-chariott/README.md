# Interacting with Chariott using Python

This sample code reproduces the [Key-Value Store Application](https://github.com/eclipse/chariott/blob/main/examples/applications/kv-app/README.md) demo from Chariott using Python.
The objective is to simplify the creation of python applications that interact with Chariott.



# Usage
- Create a [Python virtual environment](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a%20Python%20environment%20such,is%20installed%20as%20part%20of%20your%20operating%20system.)
- Import the dependencies from requirements.txt to your virtual environment

You can also use anaconda to setup your environment.

# Generating the gRPC stubs

Applications interacting with Chariott use the runtime protobuf interface. 

Assuming that the chariott code is checked out in ~/repos/chariott, to re-generate the stubs use the following command:

``` bash
python -m grpc_tools.protoc --proto_path ~/repos/chariott/proto --python_out=. --grpc_python_out=. ~/repos/chariott/proto/chariott/common/v1/common.proto

python -m grpc_tools.protoc --proto_path ~/repos/chariott/proto --python_out=. --grpc_python_out=. ~/repos/chariott/proto/chariott/runtime/v1/runtime.proto
```

This will create a folder structure under ./chariott that contains the generated code.

To use, import the following modules:

``` python
import grpc
import chariott.common.v1.common_pb2 as pb2
import chariott.runtime.v1.runtime_pb2 as runtime_pb2
import chariott.runtime.v1.runtime_pb2_grpc as runtime_pb2_grpc
```

Then create your client using

``` python
# Open a channel to the server
channel = grpc.insecure_channel('127.0.0.1:4243')
```

# Reference

- The [protocol buffers python basics](https://developers.google.com/protocol-buffers/docs/pythontutorial) contains an introduction to using protocol buffers with Python.
- The [protocol buffers python reference](https://developers.google.com/protocol-buffers/docs/reference/python-generated) provides an overview on how to create and assign different datatypes
- The (grpc Python reference)[https://grpc.io/docs/languages/python/] provides an introduction to using gRPC in Python