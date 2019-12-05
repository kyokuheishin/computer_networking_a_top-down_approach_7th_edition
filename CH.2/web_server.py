from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
socket_port = 12000
serverSocket.bind(('',socket_port))
serverSocket.listen(1)

while True:
    print("ready to serve")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send a valid HTTP header
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.close()

    except IOError:
        header = " HTTP/1.1 404 Not Found"
        connectionSocket.send(header.encode())
        connectionSocket.close()