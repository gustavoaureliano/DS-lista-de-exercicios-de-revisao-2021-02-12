candidatos = [[0,0],[0,0],[0,0],[0,0]]
nulo = [0,0]
branco = [0,0]
total = 0
while True:
    while True:
        voto = input('Voto: ')
        if voto.isnumeric():
            voto = int(voto)
            if 0 <= voto <= 6:
                break
        print("Valor inválido!")
    if voto == 0:
        break
    elif 1 <= voto <= 4:
        candidatos[voto-1][0] += 1
    elif voto == 5:
        nulo[0] += 1
    elif voto == 6:
        branco[0] += 1
    else:
        print("Algo de errado não está certo!")
    total += 1
if total != 0:
    for candidato in candidatos:
        candidato[1] = candidato[0]/total*100
    branco[1] = branco[0]/total*100
    nulo[1] = nulo[0]/total*100
print(f'Candidato 1: {candidatos[0][0]} - {candidatos[0][1]:.1f}%')
print(f'Candidato 2: {candidatos[1][0]} - {candidatos[1][1]:.1f}%')
print(f'Candidato 3: {candidatos[2][0]} - {candidatos[2][1]:.1f}%')
print(f'Candidato 4: {candidatos[3][0]} - {candidatos[3][1]:.1f}%')
print(f'Nulos:       {nulo[0]} - {nulo[1]:.1f}%')
print(f'Brancos:     {branco[0]} - {branco[1]:.1f}%')
print(f'total:       {total}')
