import socket
s=socket.socket()
s.bind(('localhost',8000))
s.listen(5)
c,addr=s.accept()
address={"169.254.13.114":"cc:47:40:E2:A0:9E"};
while True:
    ip=c.recv(1024).decode()
    try:
        c.send(address[ip].encode())
    except keyError:
        c.send("Not Found".encode())
