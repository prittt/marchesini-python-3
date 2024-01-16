n = int(input('Dammi un numero intero: '))

i = 2
primo = True
while i < n:
    if n % i == 0:
        primo = False
        break;
    i += 1
   
if primo:
    print('Il numero', n, 'è primo')
else:
    print('Il numero', n, 'non è primo')
