a = int(input("часы:"))
b = int(input("минуты"))
c = int(input("разница"))

if(a+c>24):
            d = (a+c)%24
else :
            d = a+c
if(a+c<0):
    d = 24 + (a+c)
if(d<0 and b<10):
    print('0'+str(d)+':'+'0'+str(b))
if(d<0 and b>10):
        print('0'+str(d)+':'+str(b))
if(d>10 and b<10):
    print(str(d)+':'+'0'+str(b))
if(d>24 and b <10):
    if(d>10):
       print(str(d%24)+':'+'0'+str(b))
if(d<10):
           print('0'+str(d%24)+':'+'0'+str(b))
elif(d>10 and b>10):
    print(str(d)+':'+str(b))