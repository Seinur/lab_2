import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
print ("Введите текст")
text = input();
#sock.send(text.encode('utf-8'))
##string = 'hello, world!'
##sock.send(string.encode('utf-8'))

while True:
    sock.send(text.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode("utf-8"))


sock.close()

