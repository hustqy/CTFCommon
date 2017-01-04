
str = "4(-\"K%%+3D!8C6-%5;9;=X-(/"

a =  [ ord(i) for i in str]
print a

for j in xrange(50,100):
    k = 0
    str = []
    for i in xrange(25):
        # if k == j-25 if j > 25 else 25-j:
        #     k=0
        t =( a[i] ^ (j + i )) -1
        k += 1
        str.append( chr( t %256 ) )
    print "".join(str)