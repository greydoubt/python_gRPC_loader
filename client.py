import grpc
import numpy as np
import calculator_pb2
import calculator_pb2_grpc

def prepare_data_for_server(data):
    # Convert the data to a numpy array
    data_array = np.array(data)

    # Create a request message with the data
    request = calculator_pb2.Values(values=data_array)

    return request

def process_data_with_server(data):
    # Create a gRPC channel and stub
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Prepare the data for the server
    request = prepare_data_for_server(data)

    # Call the Add method on the server
    response = stub.Add(request)

    # Return the result
    return response.value

if __name__ == '__main__':
    # Example usage:
    data = [1, 2, 3, 4, 5]
    result = process_data_with_server(data)
    print(result)
