
def add_n(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s

n = int(input('Dammi un numero intero: '))
s = add_n(n)
print('La somma dei numeri da 1 a', n, 'è', s)