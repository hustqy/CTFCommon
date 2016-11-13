def problem1():
    str = "KEK! TOP!! KEK!! TOP!! KEK!! TOP!! KEK! TOP!! KEK!!! TOP!! KEK!!!! TOP! KEK! TOP!! KEK!! TOP!!! KEK! TOP!!!! KEK! TOP!! KEK! TOP! KEK! TOP! KEK! TOP! KEK!!!! TOP!! KEK!!!!! TOP!! KEK! TOP!!!! KEK!! TOP!! KEK!!!!! TOP!! KEK! TOP!!!! KEK!! TOP!! KEK!!!!! TOP!! KEK! TOP!!!! KEK!! TOP!! KEK!!!!! TOP!! KEK! TOP!!!! KEK!! TOP!! KEK!!!!! TOP! KEK! TOP! KEK!!!!! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK!! TOP!! KEK!!! TOP! KEK! TOP!! KEK! TOP!! KEK! TOP! KEK! TOP! KEK! TOP!!!!! KEK! TOP!! KEK! TOP! KEK!!!!! TOP!! KEK! TOP! KEK!!! TOP! KEK! TOP! KEK! TOP!! KEK!!! TOP!! KEK!!! TOP! KEK! TOP!! KEK! TOP!!! KEK!! TOP! KEK!!! TOP!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK!!! TOP!! KEK!! TOP!!! KEK! TOP! KEK! TOP! KEK! TOP! KEK!! TOP!!! KEK!! TOP! KEK! TOP!!!!! KEK! TOP!!! KEK!! TOP! KEK!!! TOP!! KEK!!! TOP! KEK! TOP!! KEK!! TOP!!! KEK! TOP! KEK!! TOP! KEK!!!! TOP!!! KEK! TOP! KEK!!! TOP! KEK! TOP!!!!! KEK! TOP!! KEK! TOP!!! KEK!!! TOP!! KEK!!!!! TOP! KEK! TOP! KEK! TOP!!! KEK! TOP! KEK! TOP!!!!! KEK!! TOP!! KEK! TOP! KEK!!! TOP! KEK! TOP! KEK!! TOP! KEK!!! TOP!! KEK!! TOP!! KEK! TOP! KEK! TOP!!!!! KEK! TOP!!!! KEK!! TOP! KEK!! TOP!! KEK!!!!! TOP!!! KEK! TOP! KEK! TOP! KEK! TOP! KEK! TOP!!!!! KEK! TOP!! KEK! TOP! KEK!!!!! TOP!! KEK! TOP! KEK!!! TOP!!! KEK! TOP!! KEK!!! TOP!! KEK!!! TOP! KEK! TOP!! KEK! TOP!!! KEK!! TOP!! KEK!! TOP!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP!! KEK!! TOP!! KEK!! TOP!!! KEK! TOP! KEK! TOP! KEK! TOP!! KEK! TOP!!! KEK!! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK! TOP!!!!! KEK! TOP! KEK!! TOP! KEK! TOP!! KEK!! TOP!! KEK!! TOP!! KEK! TOP! KEK!! TOP! KEK! TOP!! KEK!! TOP! KEK!!!! TOP! KEK!! TOP! KEK!!!! TOP! KEK!! TOP! KEK!!!! TOP! KEK! TOP!!!!! KEK! TOP!"
    strs = str.split()

    DIC = {}
    a = [ ("KEK"+ "!"*i,'0'*i) for i in xrange(1,6)]
    b = [ ("TOP"+ "!"*i,'1'*i) for i in xrange(1,6)]

    for key,val in a :
        DIC[key] = val
    for key,val in b :
        DIC[key] = val
    res = []
    for i in strs:
        res.append(DIC[i])
    resul =  "".join(res)
    print resul
    out = []
    for i in xrange(0,len(resul)/8):
        out.append(chr(int(resul[i*8:i*8+8],2)))
    return  "".join(out)


print problem1()