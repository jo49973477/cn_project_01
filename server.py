import socket
import threading

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 8080
server_dict = {}

def process_data(data):
    data = data.split(',')
    cmd = data[0]
    send_data = ''
    
    if cmd == 'PUT':
        server_dict[data[1]] = data[2]
        send_data = 'Successed!'
        
    elif cmd == 'GET':
        send_data = server_dict[data[1]] if data[1] in server_dict else 'Not exist!'
        
    elif cmd == 'DELETE':
        if data[1] in server_dict:
            del server_dict[data[1]]
            send_data = 'Successed!'
        else:
            send_data = 'Not exist!'
    elif cmd == 'LIST':
        send_data = '\n'.join(['{},{}'.format(k,v) for k, v in server_dict.items()]) if server_dict else 'Not Exist'
    else:
        send_data = '400 Bad Request'
    
    return send_data

def handle_client(client_socket, client_address):
    
    print('{}에서 접속이 확인되었습니다.'.format(client_address))  # Print client connection confirmation message

    while True:
        data = client_socket.recv(1024).decode()  # Receive data from client
        if not data:
            break
        send_data = process_data(data)
        print(send_data)
        client_socket.send(send_data.encode())  # Send received data back to client

# Create a socket object, TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))  # Bind socket to host and port
server_socket.listen(5)  # Listen for incoming connections with a maximum backlog of 5
print('서버가 시작되었습니다.')  # Print server start message

while True:
    client_socket, client_address = server_socket.accept()  # Accept incoming client connection
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))  # Create a new thread to handle client
    thread.start()  # Start the thread to handle client communication

server_socket.close()  # Close the server socket