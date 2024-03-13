import socket
s=socket.socket()
s.connect(('localhost',8000))
while True:
    ip=input("Enter logical Address:")
    s.send(ip.encode())
    print("MAC address",s.recv(1024).decode())
