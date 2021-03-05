n = int(input('Digite um número: '))
cont = 0
isPrimo = False
for num in range(1, n+1):
    if n % num == 0:
        cont += 1
    if cont > 2:
        break
if cont == 2:
    isPrimo = True
print('É primo!' if isPrimo else 'Não é primo!')
