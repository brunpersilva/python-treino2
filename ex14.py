km = float(input('Quantos km o veiculo percorreu?'))
d = int(input('Quantos dias o veiculo foi utilizado?'))
a = float(km * 0.15 + (d * 60))
print('Seu veiculo alugado por {} dias e que andou {} km tem um aluguel de R${} reais'.format(d, km, a))
