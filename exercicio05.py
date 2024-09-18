nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')

resultado = float(nota1) + float(nota2) / 2

if resultado >= 7:
    print('Aprovado')
elif resultado < 7:
    print('Reprovado')
elif resultado >= 10:
    print('Aprovado com Distinção')