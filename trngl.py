def trngl(d):
    i = 1
    while i < d + 1 :
        for j in range(1,i + 1):
            print(j,end='')
        for j in range(i-1,0,-1):
            print(j,end='')
        print('',end='\n')
        i = i + 1
	




if __name__ == '__main__':
    n = int(input('Enter a string'))
    trngl(n)
	
