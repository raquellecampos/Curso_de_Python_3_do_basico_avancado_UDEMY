# Valor menor ou maior

primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'O 1° valor {primeiro_valor} é MAIOR que o 2° valor {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'O 2° valor {segundo_valor} é MAIOR que o 1° valor {primeiro_valor}')
elif (primeiro_valor == segundo_valor) or (segundo_valor == primeiro_valor):
    print(f'Os valores são iguais :()')