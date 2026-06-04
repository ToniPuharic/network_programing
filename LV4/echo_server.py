import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()

HOST = '0.0.0.0'
PORT = 65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"[ECHO SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()

        with conn:
            print(f"\n[{datetime.datetime.now()}]")
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode()

                print(f"Received: {message}")

                if message.lower() == "toni_puharic":
                    response = "Unos nije podržan."
                else:
                    response = message

                conn.sendall(response.encode())
