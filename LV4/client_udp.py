import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = input("Unesi poruku: ")

    s.sendto(message.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)

    print(f"[UDP CLIENT] Received: {data.decode()}")
