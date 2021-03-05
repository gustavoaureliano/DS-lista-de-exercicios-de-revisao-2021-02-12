for f in range(50,150+1):
    c = 5/9 * (f - 32)
    print(f'{c:.1f}°C - {f}°F')

valores = dict()
lista = list()
for c in range(50,151):
    valores['celsius'] = (c-32)*5/9
    valores['fahrenheit'] = c
    lista.append(valores.copy())
for d in range(0,2):
    for t in lista:
        print(f'{t["fahrenheit"]}°F = {t["celsius"]:.2f}°C')
