import socket
from IPy import IP

FINAL_RANGE: int = 65536


def convert_to_ip(inp):
    try:
        IP(inp)
        return inp
    except ValueError:
        return socket.gethostbyname(inp)
    except:
        pass


def get_banner(s):
    return s.recv(1024)


def scan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        print('------------------------------------------')
        print(f"{port} Open")
        try:
            banner = get_banner(s)
            print('Banner Info ' + str(banner))
        except:
            pass
        print('------------------------------------------')
    except:
        print(f"{port} Closed")


temp=input("Enter Domain(xyz.mn)")
domain_ip = convert_to_ip(temp)
print("Target " + str(domain_ip) + " scanning started.")
for p in range(1, 65535):
    scan(domain_ip, p)
