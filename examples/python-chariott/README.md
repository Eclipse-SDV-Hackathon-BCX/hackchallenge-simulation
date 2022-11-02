# Interacting with Chariott using Python

This sample code reproduces the KV-Demo from Chariott using Python.
The objective is to simplify the creation of python applications that interact with Chariott



# Usage
- Create a Python virtual environment
- Import the dependencies from requirements.txt


# Generating the gRPC stubs

Applications interacting with Chariott use the runtime protobuf interface. 

Assuming that the chariott code is checked out in ~/repos/chariott, to re-generate the stubs use the following command:

```
python -m grpc_tools.protoc --proto_path ~/repos/chariott/proto --python_out=. --grpc_python_out=. ~/repos/chariott/proto/chariott/common/v1/common.proto

python -m grpc_tools.protoc --proto_path ~/repos/chariott/proto --python_out=. --grpc_python_out=. ~/repos/chariott/proto/chariott/runtime/v1/runtime.proto
```