somaPos = 0
contNeg = 0
for n in range(5):
    num = float(input('Número: '))
    if num > 0:
        somaPos += num
    elif num < 0:
        contNeg += 1
print(f'Soma números positivos: {somaPos}')
print(f'Contagem números negativos: {contNeg}')
