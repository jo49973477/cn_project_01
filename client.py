import socket
import sys

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 8080

def data_getting():
    data = ''
    
    while True:
        command = input('명령의 종류를 정하시오(PUT, GET, DELETE, LIST): ')
        data = ''
        
        if command == 'PUT':
            textA = input('Key값: ')
            textB = input('value값: ')
            data = ','.join((command, textA, textB))
            break
        
        elif command == 'GET':
            textA = input('Key값: ')
            data = ','.join((command, textA))
            break
            
        elif command == 'DELETE':
            textA = input('Key값: ')
            data = ','.join((command, textA))
            break
            
        elif command == 'LIST':
            data = command
            break
        
        else:
            print("다시 입력하세요!")
            continue
        
    return data
        

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    # Connect to the server
    while True:
        
        client_socket.sendall(data_getting().encode())
        # Receive a response from the server
        data = client_socket.recv(1024)
        print('Received:', data.decode())
        
        y_n = input("연결을 계속 하시겠습니까?(Y/N): ")
        if y_n == 'Y':
            continue
        else:
            break
    client_socket.close()
        
    
        
