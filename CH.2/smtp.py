from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

mailserver = "smtp.163.com"

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect((mailserver,25))

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

command = 'HELO kyokuheishin\r\n'

clientSocket.send(command.encode())

recv = clientSocket.recv(1024).decode()
print(recv)

# LOGIN

command = 'AUTH LOGIN\r\n'

clientSocket.send(command.encode())

recv = clientSocket.recv(1024).decode()
print(recv)

username = input("Please input your username in base64 str.")+"\r\n"


clientSocket.send(username.encode())

recv = clientSocket.recv(1024).decode()
print(recv)

password = input("Please input your password in base64 str.")+"\r\n"

clientSocket.send(password.encode())

recv = clientSocket.recv(1024).decode()
print(recv)


# Send MAIL FROM

command = 'MAIL FROM: <kyokuheishin@163.com>\r\n'

clientSocket.send(command.encode())

recv = clientSocket.recv(1024).decode()
print(recv)


# Send RCPT TO

command = 'RCPT TO: <kyokuheishin@gmail.com>\r\n'

clientSocket.send(command.encode())

recv = clientSocket.recv(1024).decode()
print(recv)

# Send DATA

command = "DATA\r\n"

clientSocket.send(command.encode())

recv = clientSocket.recv(1024).decode()
print(recv)



message = 'from: kyokuheishin@163.com\r\n'
message += 'to: kyokuheishin@gmail.com\r\n'
message += 'subject: test_mail\r\n'
message += 'Content-Type: text/plain \t\n'
message += '\r\n' + msg
clientSocket.sendall(message.encode())





clientSocket.sendall(endmsg.encode())



recv = clientSocket.recv(1024).decode()
print(recv)

command = "QUIT\r\n"

clientSocket.send(command.encode())

recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.close()