print('Digite sua idade:')
idade = int(input())

if idade < 18:
    print('Você é menor de idade!')
elif idade == 18:
    print('Você tem 18 anos!')
else:
    print('Você é maior de idade!')