import socket
def printmat(matrix):
    for row in matrix:
        for value in row:
            print value,
        print ""
    print ""


def pad(s):
    if len(s) % 9 == 0:
        return s
    for i in xrange((9 - (len(s) % 9))):
        s.append(0)
    return s


def genBlockMatrix(s):
    outm = [[[7 for x in xrange(3)] for x in xrange(3)] for x in xrange(len(s) / 9)]
    for matnum in xrange(0, len(s) / 9):
        for y in xrange(0, 3):
            for x in xrange(0, 3):
                outm[matnum][y][x] = s[(matnum * 9) + x + (y * 3)]
    return outm


def fixmatrix(matrixa, matrixb):
    out = [[0 for x in xrange(3)] for x in xrange(3)]
    for rn in xrange(3):
        for cn in xrange(3):
            out[cn][rn] = (int(matrixa[rn][cn]) | int(matrixb[cn][rn])) & ~(int(matrixa[rn][cn]) & int(matrixb[cn][rn]))
    return out


def chall(seed):
    IV = [c for c in '']

    blocks = genBlockMatrix(pad(IV + [ord(c) for c in seed]))

    res = [[0 for i in xrange(3)] for i in xrange(3)]
    for i in xrange(len(blocks)):
        res = fixmatrix(res, blocks[i])

    # print "SEED: " + str(seed)
    # printmat(res)
    return res

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

            data = craft(response)
            data += "\n"
            client.send(data)

        client.close()


def decodeAll(matrixa, matrixb):
    out = [[0 for x in xrange(3)] for x in xrange(3)]
    for rn in xrange(3):
        for cn in xrange(3):
            p =int( matrixa[rn][cn])
            q = int(matrixb[rn][cn])
            out[cn][rn] = p & ~(q & p) | (q & ~p)
    return out

def printstr (s):
    ar = []
    arr = []
    for row in s:
        for i in row:
            arr.append(str(i))
            ar.append("\\x"+ "{:02x}".format(i%256) )
    return ",".join(arr)


def craft(response):
    data = ""
    lines = response.splitlines()
    index = lines[0].index(": ")
    seed = lines[0][index:][2:]
    if len(seed) > 9:
        return data
    arr = []
    for ln in lines[1:]:
        arr.append([ int (i) for i in ln.split()] )
    pre = chall(seed)
    res = decodeAll(arr,pre)

    data = printstr(res)
    return  data


# func("vermatrix.pwn.democrat",4201)
a  ="""SEED: xKlNcpvhs
 422 1243 1245
175 629 324
658 807 1108
"""
func("vermatrix.pwn.democrat",4201)