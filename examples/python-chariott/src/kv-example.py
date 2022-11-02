import grpc
import chariott.runtime.v1.runtime_pb2 as runtime_pb2
import chariott.common.v1.common_pb2 as common_pb2
import chariott.runtime.v1.runtime_pb2_grpc as runtime_pb2_grpc

# Open a channel to the server
channel = grpc.insecure_channel('127.0.0.1:4243')
stub = runtime_pb2_grpc.ChariottServiceStub(channel)


# Step 2: Lets do a read for date-time
# ------------------------------------
request = runtime_pb2.FulfillRequest (
    namespace = "sdv.kvs",
    intent = common_pb2.Intent()
)

# Fill the intent with the type
request.intent.read.CopyFrom(common_pb2.ReadIntent(key="date-time"))
print("Request: " + str(request))

# Make and print the request
response = stub.Fulfill(request)
print (response)



# Close the channel
channel.close()