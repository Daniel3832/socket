import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print (s)

server = "pythonprogramming.net"
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

hello
