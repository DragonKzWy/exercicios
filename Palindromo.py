"""
Outro exemplo: determinar se a entrada do usuário é um palíndromo. 

Palíndromo: se uma palavra/sentença é soletrada da mesma maneira quando é invertida. 
  EX: racecar (carro de corrida)

Para este exemplo, vamos tornar isto de forma mais abrangente. 
Em vez de verificar se uma palavra é um palíndromo, vamos testar se uma frase é um palíndromo. 

A fim de escrever este programa, estabeleceremos algumas especificações:
  - Tratar as letras maiúsculas como minúsculas
  - Ignorar todos os espaços brancos e pontuações
  - Uma sentença/string vazia é considerada como um palíndromo. 
"""

"""
import string

def palindromo(str):
    # Converte a string para minúsculas, remove espaços e pontuações.
    exclude = set(string.punctuation + string.whitespace)
    str = ''.join(ch for ch in str if ch not in exclude)
    str = str.replace(" ", "").lower()

      # Verificar se a string é a mesma tanto em ordem invertida quanto na ordem original
    if str == str[::-1]:
        return True
    else:
        return False
    

    
# Solicitar ao usuário que introduza a sentença
def main():
  userSentence = input("Enter a sentence to be tested as a palindrome:")

  if (palindromo(userSentence)):
    print(userSentence + " é um palindromo!")
  else:
    print(userSentence + " NÃO é um palindromo!")

if __name__ == "__main__":
    main()

"""    

import string

def isPalindrome(str):
  exclude = set(string.punctuation)
  str = ''.join(ch for ch in str if ch not in exclude)
  str = str.replace(" ", "").lower()
  if str == str[::-1]:
    return str + " é um palindromo!"
  else:
    return str + " NÃO é um palindromo!"

def main():
  userSentence = input("Enter a sentence to be tested as a palindrome:")
  print(isPalindrome(userSentence))

if __name__ == "__main__":
    main()