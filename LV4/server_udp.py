import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = '0.0.0.0'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[UDP SERVER] Listening on {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode()

        print(f"[UDP SERVER] Received from {addr}: {message}")

        response = f"Poruka primljena: {message}"
        s.sendto(response.encode(), addr)
