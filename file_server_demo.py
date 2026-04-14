import socket

host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("Server listening on port:", port)
s.listen(1)
c, addr = s.accept()
print("Connected to:", addr)
fileName = c.recv(1024).decode()

try:
    with open(fileName, 'rb') as f:
        content = f.read()
        c.sendall(content)
except FileNotFoundError:
    c.send(b"File not found")
c.close()
s.close()