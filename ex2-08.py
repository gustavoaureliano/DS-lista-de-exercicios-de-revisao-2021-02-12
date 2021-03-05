maior = 0
menor = 0
for n in range(6):
    num = float(input('número: '))
    if n == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'Menor: {menor}')
print(f'Maior: {maior}')