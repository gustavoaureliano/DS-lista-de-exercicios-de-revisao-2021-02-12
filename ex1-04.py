emprestimo = float(input('Valor do empréstimo: R$'))
taxa = float(input('Taxa de juros: '))
n = int(input('Duração do empréstimo: '))
vFinal = emprestimo * (1 + taxa / 100) ** n
print(vFinal)
