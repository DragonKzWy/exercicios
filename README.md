# Validador de Dígitos (0-9) em Python

Este projeto é um exercício de programação em Python que demonstra como implementar uma estrutura de decisão múltipla semelhante ao `switch-case` utilizando apenas condicionais `if`, `elif` e `else`. O programa solicita que o usuário digite um número entre 0 e 9 e, em seguida, exibe uma mensagem confirmando o número digitado ou uma mensagem de erro caso o valor esteja fora do intervalo esperado.

## Como Funciona

O código realiza as seguintes etapas:

1. Solicita ao usuário que digite um número inteiro entre 0 e 9
2. Utiliza uma estrutura de condicionais (`if`, `elif`, `else`) para verificar o valor inserido
3. Para cada dígito válido (0-9), exibe uma mensagem de confirmação específica
4. Para qualquer valor fora deste intervalo, exibe uma mensagem de erro

## Objetivos de Aprendizado

Este projeto foi desenvolvido como exercício inicial para praticar:
- Uso básico de estruturas condicionais em Python
- Validação de entrada do usuário
- Simulação de comportamento `switch-case` com `if/elif/else`
- Formatação de saída no terminal
- Boas práticas de organização de código simples

## Como Executar o Projeto

Para executar o projeto em sua máquina:

1. Certifique-se que você tem Python instalado (versão 3.6 ou superior)
2. Copie o código abaixo para um arquivo com extensão `.py` (ex: `validador-digitos.py`)
3. Abra o terminal na pasta onde salvou o arquivo
4. Execute o comando: `python validador-digitos.py`
5. Siga as instruções exibidas no terminal

```python
num = int(input('Digite um numero entre 0 e 9.\n'))

if num == 0:
    print('Numero 0')
elif num == 1:
    print('Numero 1')
elif num == 2:
    print('Numero 2')
elif num == 3:
    print('Numero 3')
elif num == 4:
    print('Numero 4')
elif num == 5:
    print('Numero 5')
elif num == 6:
    print('Numero 6')
elif num == 7:
    print('Numero 7')
elif num == 8:
    print('Numero 8')
elif num == 9:
    print('Numero 9')    
else:
    print('ERROR! Caractere inválido!')
```

## Exemplos de Funcionamento

**Caso de entrada válida:**
```
Digite um numero entre 0 e 9.
7
Numero 7
```

**Caso de entrada inválida:**
```
Digite um numero entre 0 e 9.
12
ERROR! Caractere inválido!
```

## Próximos Passos e Melhorias

Este projeto pode ser expandido de várias formas:
- Adicionar tratamento de erros para entradas não numéricas
- Implementar a mesma funcionalidade usando dicionários
- Converter o código em uma função reutilizável
- Adicionar testes automatizados
- Criar uma interface gráfica simples

## Sobre o Autor

Este projeto foi desenvolvido como parte da minha jornada de aprendizado em Python. Mesmo sendo um exercício simples, ele demonstra a aplicação prática de conceitos fundamentais da linguagem.

## Licença

Este projeto está disponível sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
