import socket
import itertools
import time
target = "86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site"
port = 20000

MAGIC = "1234567890"

def craft():
    for i in itertools.permutations(MAGIC,6):
        data = "EKO{" + "".join(i)+"}"
        yield data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target, port))
for i in craft():
   
    response = sock.recv(1024)
    recv_len = len(response)
    print  "response", response
    sock.send(i)
