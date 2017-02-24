def gcd(a,b):
#    print('ram')
    r = a % b
    print(r)
    while ( r != 0):
#        print('partha')
        a = b
        b = r
        r = a % b
    print(b)
    
def main():
    print('x')
    gcd(24,16)
    
if (__name__ == '__main__'):
    main()


