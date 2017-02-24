import os
from binary import convert
file=open('test.txt','r')
for l in file :
    #print(l)
    l = l.strip()
    print(convert(l))
    #print (convert(l))
