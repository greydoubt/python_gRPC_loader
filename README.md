# python_gRPC_loader

This code defines a gRPC servicer class that implements the Add method, which takes an array of values and returns their sum as a Result message. The serve function starts the gRPC server and waits for requests to come in.

client.py defines a prepare_data_for_server function that takes a batch of data and converts it to a NumPy array, which is then used to create a request message for the gRPC server. It also defines a process_data_with_server function that creates a gRPC channel and stub, prepares the data for the server using the prepare_data_for_server function, and then calls the Add method on the server to process the data.

To use this client, you can call the process_data_with_server function with a batch of data to be processed by the gRPC server. The result will be the sum of the values in the batch.

    Use the docker build command to build the Docker image:

*docker build -t my-grpc-app .*

    Use the docker run command to start a container from the image:

*docker run -p 50051:50051 my-grpc-app*

    Test the gRPC server by sending requests from the included gRPC client. 
