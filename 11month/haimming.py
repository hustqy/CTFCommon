import sys

import struct
def func (path):
    fd = open("output","wb")
    with open(path ,'rb') as f:
        data = f.read()
        assert len(data) %15 ==0
        for i in xrange(0,len(data),15):
            tmp = struct.unpack_from('15B', data,i)
            # print ""
            res = deal(tmp)
            res.reverse()
            for d in res:
                fd.write(struct.pack('B', d))
    fd.close()

def deal( cur):
    arr = [ "{:08b}".format(i) for i in cur]
    res = []
    for j in xrange(8):
        tmp = [ arr[i][j] for i in xrange(15)]
        res.append("".join(tmp) )
    r = []
    for s in res:
        r.append( hamming(s))
    out = []
    for j in xrange(11):
        t = "".join([ r[i][j] for i in xrange(8)])
        out.append(int(t,2))
    return out

def hamming(s):

    s = list(s)
    r0 = int(s[0])
    r1 = int(s[1])
    r2 = int(s[3])
    r3 = int(s[7])

    I1 = int(s[2])
    I2 = int(s[4])
    I3 = int(s[5])
    I4 = int(s[6])
    I5 = int(s[8])
    I6 = int(s[9])
    I7 = int(s[10])
    I8 = int(s[11])
    I9 = int(s[12])
    I10 = int(s[13])
    I11 = int(s[14])
    # I1 =  s[2]
    # I2 =  s[4]
    # I3 =  s[5]
    # I4 =  s[6]
    # I5 =  s[8]
    # I6 =  s[9]
    # I7 =  s[10]
    # I8 =  s[11]
    # I9 =  s[12]
    # I10 = s[13]
    # I11 = s[14]
    s3 = r3 ^ I11 ^ I10^ I9^ I8^ I7^ I6^ I5
    s2 = r2 ^ I11^ I10^ I9^ I8^ I4^ I3 ^ I2
    s1 = r1 ^I11 ^ I10 ^ I7 ^I6 ^ I4 ^ I3 ^ I1
    s0 = r0 ^ I11 ^ I9 ^  I7 ^I5 ^ I4 ^ I2 ^ I1

    n = int((str(s3) + str(s2) + str(s1) + str(s0) ),2 )
    if n != 0 and  n != 8 and n!=4 and n!=2 and n!=1:
        s[n-1] = str(int(s[n-1])^1)


    I1 =  s[2]
    I2 =  s[4]
    I3 =  s[5]
    I4 =  s[6]
    I5 =  s[8]
    I6 =  s[9]
    I7 =  s[10]
    I8 =  s[11]
    I9 =  s[12]
    I10 = s[13]
    I11 = s[14]
    return "".join(I11 + I10+ I9+ I8+ I7+ I6+ I5+ I4+ I3+ I2+ I1)



func("F:\CTF\juniors\image_with_flag_defect.jpg.hamming")