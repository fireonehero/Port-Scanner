import socket

def port_scanner(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((host, port))
            open_ports.append(port)
            sock.close()
        except:
            continue
    return open_ports

# Get user input
host = input("Enter the host to scan: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

open_ports = port_scanner(host, start_port, end_port)
print(f"Open ports on {host} are: {open_ports}")
