import time
from socket import *
serverName= '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
message = "ping"

for i in range(0,10):
    print(str(i+1)+("#Ping: "))
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    start_time = time.time()
    try:
        modified_message, serverAddress = clientSocket.recvfrom(2048)
        print(modified_message.decode())
        print("RTT Time:" + str(time.time()-start_time))        
    except:
        print("Request timeout.")

clientSocket.close()