maior = 0
for n in range(25):
    num = float(input('número: '))
    if num > maior or n == 0:
        maior = num
print(maior)