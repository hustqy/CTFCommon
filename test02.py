import  hashlib
import random

def zhalan(string):
    field=[]
    elen = len(string)
    for i in range(2,elen):
                if(elen%i==0):
                    field.append(i)

    for f in field:
        b = elen / f
        result = {x:'' for x in range(b)}
        for i in range(elen):
            a = i % b
            result.update({a:result[a] + string[i]})
        d = ''
        for i in range(b):
            d = d + result[i]
        print 'hell\t'+str(f)+'\t'+'res: '+d
def fin(required):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    size = len(seed)-1
    for i in xrange(999999):
        arr = []
        for j in xrange(6):
            arr.append(random.randint(0,size))
        res= "".join([seed[it] for it in arr])
        a = hashlib.md5(res)
        if a.hexdigest()[0:6] == required:
            print res
            break

def decode(lstr):
    res = ""
    for i in xrange(len(lstr)):
        if i %2== 1:
            continue
        tmp =  chr(int("0x"+lstr[i:i+2],base=16))
        res +=tmp
    print res
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
