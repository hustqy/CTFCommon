import socket

def func(target,port):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(( target,port))
        while True:
            recv_len = 1
            response = ""
            while recv_len:
                tmp = client.recv(4096)
                recv_len  = len(tmp)
                response += tmp
                if recv_len < 4096:
                    break
            print  response
            data = raw_input("")
            data += "\n"
            client.send(data)

        client.close()

func("123.206.6.58",80)

