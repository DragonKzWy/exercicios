"""
EXERCÍCIO: implemente o exemplo de switch case acima usando as condições "if/else"

Prompt: para cada dígito entre 0-9, o programa imprimirá uma confirmação 
para o valor inserido ou irá imprimir "invalid inputs" para todos os outros números.
"""

num = int(input('Digite um numero entre 0 e 9.\n'))

if num == 0:
    print ('Numero 0')
elif num == 1:
    print ('Numero 1')
elif num == 2:
    print ('Numero 2')
elif num == 3:
    print ('Numero 3')
elif num == 4:
    print ('Numero 4')
elif num == 5:
    print ('Numero 5')
elif num == 6:
    print ('Numero 6')
elif num == 7:
    print ('Numero 7')
elif num == 8:
    print ('Numero 8')
elif num == 9:
    print ('Numero 9')    
else:
     print('ERROR! Caractere inválido!')                   