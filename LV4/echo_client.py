import socket

HOST = '127.0.0.1'
PORT = 65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print("[ECHO CLIENT] Connected.")

    while True:
        message = input("Unesi poruku (ili 'exit'): ")

        if message.lower() == 'exit':
            break

        s.sendall(message.encode())

        data = s.recv(1024)

        print(f"[ECHO CLIENT] Received: {data.decode()}")
