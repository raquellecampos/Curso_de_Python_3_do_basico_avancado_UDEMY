nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso: '))
imc = peso / (altura * altura)

print(f'{nome} tem {altura:.2f} de altura,\npesa {peso} quilos e seu IMC é\n{imc:.2f}')