#def fatorial(a,show=0):
    #res = 1 
    #if show == True:
    #    for c in range(a,0,-1):
    #        print(f'{c}',end=' ')
    #        
    #        res *= c
    #    print('=',end=' ')
    #else:
    #    for c in range(a,0,-1):
    #        res *= c
    #return res

#print(f'{fatorial(5)}')
#help(fatorial)

def fatorial(n,show=False):
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=',end='')
        f*=c
    return f

print(fatorial(5,show=False))