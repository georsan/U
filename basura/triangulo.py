def izq():
    for i in range(9):
        
        for j in range(i):
            print(' ',end=' ')
        m=9-i

        for k in range(m):        
            print('*',end=' ')
       
        print()


def der():
    i=9
    while i>=0:
        
        for k in range(i):
            print(' ',end=' ')
        s=9-i
        for m in range(s):
            print('*',end=' ')
        print()    
        i=i-1

def izqs():
    for i in range(10):
        for j in range(i):
            print('*',end=' ')

        print(' ')

def derc():
    i=0
    while i<9:
        k=9-i
        for j in range(k):
            print('*',end=' ')
        i=i+1
        print(' ')


der()
print()
derc()

izqs()
print()
izq()
