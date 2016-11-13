
import sys, random, time

flag = "flag{1_sw34r_1F_p30Pl3_4cTu4lLy_TrY_Th1s}"


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
    data = raw_input("")

    data = data.replace(' ', '').strip().split(',')

    if len(data) != 9:
        return False

    for i in xrange(len(IV)):
        if str(IV[i]) != str(data[i]):
            return False




# if chall():
#     print flag



def matrixand(matrixa, matrixb):
    out = [[0 for x in xrange(3)] for x in xrange(3)]
    for rn in xrange(3):
        for cn in xrange(3):
            out[cn][rn] = int(matrixa[rn][cn]) & int(matrixb[cn][rn])
    return out

def matrixsub(matrixa, matrixb):
    out = [[0 for x in xrange(3)] for x in xrange(3)]
    for rn in xrange(3):
        for cn in xrange(3):
            out[cn][rn] = int(matrixa[rn][cn]) & ~( int(matrixb[rn][cn]))
    return out

def matrixor(matrixa, matrixb):
    out = [[0 for x in xrange(3)] for x in xrange(3)]
    for rn in xrange(3):
        for cn in xrange(3):
            out[cn][rn] = int(matrixa[rn][cn]) | int(matrixb[rn][cn])
    return out


def decodeAll(matrixa, matrixb):
    out = [[0 for x in xrange(3)] for x in xrange(3)]
    for rn in xrange(3):
        for cn in xrange(3):
            p =int( matrixa[rn][cn])
            q = int(matrixb[rn][cn])
            out[cn][rn] = p & ~(q & p) | (q & ~p)
    return out


b = [
[66, 62 ,86],
[99 ,85 ,106],
[80 ,75, 110 ]
]
c = [[32, 72, 18],
[36, 61, 8],
[58, 110, 48]]


seed = "@LGR\%C<S"
seed00 = "LGR\%C<S"+ chr(0)
x = [
[64 ,76, 71 ],
[82, 92, 37 ],
[67, 60, 83 ]
]
x00 = [
[76, 71, 82 ],
[92, 37, 67 ],
[60, 83, 0 ]
]

y=[
[378 ,307, 575],
[944 ,256, 564],
[588, 816, 661]
]
seed2 ="If|y\"iw#O"
x2 = [
[60 ,74, 66 ],
[95, 35, 114 ],
[121, 70, 35]
]

y2 = [
[438, 373, 707],
[1040, 806, 514],
[1098, 542,172]

]
#
#
def printstr (s):
    ar = []
    arr = []
    for row in s:
        for i in row:
            arr.append(chr(i%256))
            ar.append("\\x"+ "{:02x}".format(i%256) )
    print "".join(arr)
    print "python -c \'print \""+ "".join(ar) + "\" \'"

final = "xKlNcpvhs"
f = """ 422 1243 1245
175 629 324
658 807 1108

"""
arr =[ int(i) for i in  f.split()]
hehe = [arr[i*3:i*3+3] for i in xrange(len(arr)/3)]

# for i in xrange(0,9):
#     srcx = chall(seed2[i:] +chr(0)*i)
#     print decodeAll( hehe,srcx)
for i in xrange(0,9):
    srcx = chall(final[i:] +chr(0)*i)
    printstr(decodeAll( hehe,srcx))