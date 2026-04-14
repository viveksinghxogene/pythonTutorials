import socket

host="localhost"
port=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
connection,address=s.accept()
print('Connection from :',connection)
print('Address is at : ',address)
connection.send(b"Hello, How are you ?")
connection.send("Agin a hello from Vivek Singh".encode())


# this is the output that i am getting while hitting the server from the browser
#Connection from : <socket.socket fd=456, family=2, type=1, proto=0, laddr=('127.0.0.1', 4000), raddr=('127.0.0.1', 55098)>
# Address is at :  ('127.0.0.1', 55098)


#this message is printed when the conenciton is made from the program in python projects
# Connection from : <socket.socket fd=460, family=2, type=1, proto=0, laddr=('127.0.0.1', 4000), raddr=('127.0.0.1', 59962)>
# Address is at :  ('127.0.0.1', 59962)`