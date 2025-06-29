"""
Escreveremos nossa própria função que testa se um triângulo de 3 lados é um triângulo retângulo. 
Como não podemos controlar a ordem dos lados que o usuário nos dá (de tal forma que C é o comprimento mais longo), 
precisamos verificar manualmente se C é o comprimento mais longo (os comprimentos A e B podem estar em qualquer ordem). 
Caso contrário, nosso teorema de Pitágoras falhará. 
"""

def triangulo_retangulo(a, b, c):
    #Reatribuir valores variaveis para garantir que C seja o comprimento mais longo.
    if (max(a,b,c)) != c:
        #tmp armazena os valores anteriores de C, que não é o comprimento mais longo.
        tmp = c
        c = max(a, b, c)
        if a == c:
            a = tmp
        elif b == c:
            b = tmp

    #Verifica se o triângulo é retângulo.
    if (a**2 + b**2) == c**2:
       print("É um triângulo retângulo!")

       #Se o programa vê uma declarativa de retorno, ele não executa mais nada.
       return True
    print("Não é um triângulo retângulo!")
    return False

#Pedimos ao usuário que insira os comprimentos dos lados do triângulo.
a = int(input("Digite o comprimento do lado A: "))
b = int(input("Digite o comprimento do lado B: "))
c = int(input("Digite o comprimento do lado C: "))

#Chamamos a função triangulo_retangulo com os valores inseridos pelo usuário.
triangulo_retangulo(a, b, c)