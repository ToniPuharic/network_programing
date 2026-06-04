import socket

ip = "8.8.8.8"
hostname = socket.gethostbyaddr(ip)

print(f"Hostname: {hostname[0]}")