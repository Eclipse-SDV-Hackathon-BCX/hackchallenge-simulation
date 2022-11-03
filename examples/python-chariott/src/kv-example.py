import grpc
from datetime import datetime
import chariott.runtime.v1.runtime_pb2 as runtime_pb2
import chariott.common.v1.common_pb2 as pb2
import chariott.runtime.v1.runtime_pb2_grpc as runtime_pb2_grpc

# Open a channel to the server
channel = grpc.insecure_channel('127.0.0.1:4243')
stub = runtime_pb2_grpc.ChariottServiceStub(channel)


# Step 1: Lets do a key-value pair write to the store
# ---------------------------------------------------
# Create a FulfillRequest, set the intent to WriteIntent and add the key "date-time" and the value to the current time (as string)
request = runtime_pb2.FulfillRequest (
    namespace = "sdv.kvs",
    intent = pb2.Intent()
)

writeIntent=pb2.WriteIntent(key="date-time")
writeIntent.value.CopyFrom(pb2.Value(string=str(datetime.now())))

request.intent.write.CopyFrom(writeIntent)

print("Write Request: " + str(request))

# Make and print the request
response = stub.Fulfill(request)
print (response)


# Step 2: Lets do a read for date-time
# ------------------------------------
request = runtime_pb2.FulfillRequest (
    namespace = "sdv.kvs",
    intent = pb2.Intent()
)

# Fill the intent with the ReadIntent object.
request.intent.read.CopyFrom(pb2.ReadIntent(key="date-time"))
print("Read Request: " + str(request))

# Make and print the request
response = stub.Fulfill(request)
print (response)


# Step 3: Now it is time to discover the service end points
# ---------------------------------------------------------
request = runtime_pb2.FulfillRequest (
    namespace = "sdv.kvs",
    intent = pb2.Intent()
)

request.intent.discover.CopyFrom(pb2.DiscoverIntent())
print("Discover Request: " + str(request))

# Make and print the request
response = stub.Fulfill(request)
print (response)

# Step 4: Open a channel for receiving events
# -------------------------------------------

request = runtime_



# Close the channel
channel.close()