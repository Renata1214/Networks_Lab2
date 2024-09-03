import socket

server_sock = socket.socket(socket.AF_INET, 
                            socket.SOCK_STREAM)
server_sock.bind( ("127.0.0.1", 1234) )
server_sock.listen(0)
conn, addr = server_sock.accept()

print("socket with IP address {} \
and port number {} connected".format(addr[0], addr[1]))

message = 'Hello client, I am the server!'
conn.send(message.encode('utf-8'))

conn.close()
server_sock.close()
