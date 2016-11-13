import socket
import threading
import  time

import subprocess
def handle_client(client):
    while True:
        recvpack = client.recv(1024)
        print recvpack
        client.send("hello")
        time.sleep(0.1)

def func(target,port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    print "[*]listening on %s : %d" % (target, port)


    while True:
        client, addr = server.accept()
        print "[*]accept connection from %s: %d" % (addr[0], addr[1])
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


func("127.0.0.1",3999)