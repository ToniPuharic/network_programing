import socket

ports = input("Unesi portove: ").split(",")

for port in ports:
    port = int(port.strip())
    try:
        service = socket.getservbyport(port)
    except:
        service = "Nepoznat"
    print(f"Port {port}: {service}")