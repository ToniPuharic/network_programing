import socket
import sys

socket.setdefaulttimeout(0.5)

if len(sys.argv) != 3:
    print("Upotreba: python3 port_scanner.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} na hostu {host} je OTVOREN")
else:
    print(f"Port {port} na hostu {host} je ZATVOREN ili NEDOSTUPAN")

sock.close()
