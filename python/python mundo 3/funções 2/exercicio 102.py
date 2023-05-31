def fatorial(a,show=0):
    """
    a = O valor fo fatorial
    show = Você tem a opção de deixar False or True, sendo que False é para não permitir que apareça os multiplos do resultado em fatorial. 

    """
    res = 1 
    if show == True:
        for c in range(a,0,-1):
            print(f'{c}',end=' ')
            
            res *= c
        print('=',end=' ')
    else:
        for c in range(a,0,-1):
            res *= c
    return res

print(f'{fatorial(5,False)}')