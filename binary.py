import os
def convert( a ):
    #binary = raw_input('a')
    decimal=0
    for i in range(len(str(a))):
     #   print(a)
        power=len(str(a))-(i+1)
        decimal += int(str(a)[i])*(2**power)

    return decimal


#Main()

#a = int(input('enter a binary number'))
    #a: 11001
 

#convert(a)



