import  hashlib
import random

def caser(lstr):
    res = []
    for p in range(127):
        str1 = ''
        for i in lstr:
            temp = chr((ord(i)+p)%127)
            if 32<ord(temp)<127 :
                str1 = str1 + temp
                feel = 1
            else:
                feel = 0
                break
        if feel == 1:
            res.append(str1)
    return  res

def caser_print(s):
    for i in caser(s):
        print i

def Atbash(s):
    """
    ABCDEFGHIJKLM
    ZYXWVUTSRQPON
    :return:
    """
    A = "ABCDEFGHIJKLM"
    B = "ZYXWVUTSRQPON"
    dic = {}
    for i in xrange(13):
        dic[A[i]] = B[i ]
    for i in xrange(13):
        dic[B[i]] = A[i ]
    res = []
    for i in s :
        res.append(dic[i])

    return  "".join(res)
