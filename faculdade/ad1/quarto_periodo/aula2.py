rept = 0
def torre_hanoi(n):
    rept += 1
    if n > 1 :
        if rept == 1:
            t = 1
        else:
            t=2*t+1
            torre_hanoi(n-1)
    else:
        if n == 1 and rept > 1:
            return t
        elif n == 1 and rept == 1:
            return 1
        elif n == 0:
            return print('Digite um número maior que 0')

torre_hanoi(3)