import socket
import selectors
import sys

HOST = 'localhost'
PORT = 65433

sel = selectors.DefaultSelector()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.setblocking(False)

name = input("Unesite korisničko ime: ")
sock.sendall(name.encode())

print("Chat započet. Pišite poruke ili Ctrl+C za izlaz.")
print("> ", end="", flush=True)

sel.register(sock, selectors.EVENT_READ)
sel.register(sys.stdin, selectors.EVENT_READ)

while True:
    events = sel.select()

    for key, _ in events:
        if key.fileobj is sock:
            data = sock.recv(1024)

            if data:
                print(f"\n{data.decode()}")
                print("> ", end="", flush=True)
            else:
                print("\nVeza sa serverom je zatvorena.")
                sys.exit()

        else:
            msg = sys.stdin.readline().strip()

            if msg:
                sock.sendall(msg.encode())
                print("> ", end="", flush=True)
