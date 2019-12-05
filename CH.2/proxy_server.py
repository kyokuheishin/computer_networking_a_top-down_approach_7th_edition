from socket import *

if len(sys.argv) <= 1:
    print('Usage: "python3 ProxyServer.py server_ip"')
    sys.exit(2)

tcpSerSock = socket(AF_INET,SOCK_STREAM)

socket_port = 12000

tcpSerSock.bind(('',socket_port))
tcpSerSock.listen(10)

while 1:
    print('Ready to serve')
    tcpCliSock, addr = tcpSerSock.accept()
    print("Received a connection from:", addr)
    message = tcpCliSock.recv(2048).decode()
    print(message)
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = False
    filetouse = "/" + filename
    print(filetouse)

    try:
        f = open(filetouse[1:],"r")
        outputdata = f.readlines()
        fileExist = True
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        tcpCliSock.send("Connection: close\r\n")
        tcpCliSock.send("Content-Length: %d\n\n") % len(outputdata)

        for i in range(len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())

        print("Read from cache")

    except IOError:
        if fileExist == False:

            c = socket(AF_INET,SOCK_STREAM)
            hostn = filename.replace("www.","",1)
            print(hostn)

            try:
                c.connect((hostn,80))
                c.sendall(message.encode())

                buff = c.recv(2048)

                tcpCliSock.sendall(buff)

                tmpF = open("./"+filename,"w")
                tmpF.writelines(buff.decode())
                tmpF.close()

            except:
                print("Illegal request")

    tcpCliSock.close()
    tcpSerSock.close()



