import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Ime računala: {hostname}")
print(f"IP adresa: {ip_address}")