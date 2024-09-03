import socket

client_sock = socket.socket(socket.AF_INET, 
                            socket.SOCK_STREAM)
client_sock.connect( ("127.0.0.1", 1234) )

data = client_sock.recv(1024)
message = data.decode('utf-8')
print(message)

client_sock.close()