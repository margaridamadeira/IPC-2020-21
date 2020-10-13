# Programação em Python 


## Objetivos de aprendizagem

Nesta lição, veremos de forma mais abrangente, a linguagem Python:

1. Atribuição a variáveis
1. Expressões
1. Interrogações e ciclos
1. Organizar
1. Usar



### A - Atribuições


A atribuição (em inglês, assignment) consiste em identificar um nome e associá-lo com um conteúdo usando o sinal de igual. 

Já vimos que usamos a atribuição para atribuir conteúdo a variáveis. Mas não é necessário fazer uma atribuição de cada vez.

x, y = 5, 2

#### Como podemos verificar se funcionou?

x

y

print (x)

E se quisermos trocar os conteúdos das variáveis podemos fazer

x, y = y, x

E agora? Qual o valor de x? E de y?

print('x =', x)
print('y =', y)

Mas o conteúdo não tem que ser sempre numérico. 

nome = 'Maria'
print(nome)

apelido = 'Silva'
apelido

Para além de tipos numéricos (inteiros, vírgula flutuante, complexos) e *strings*, sabemos que existem outros tipos de dados e dedicaremos uma aula a falar dos tipos de dados. Vejamos agora dois novos tipos.

# Podemos quardar valores lógicos (tipo boolean)
resultado = True 
resultado 

### E - Expressões

Na semana passada tivemos a oportunidade de experimentar o uso do Python como calculadora. Exprimentámos com o *Jupyter Notebook*, com a linha de comando da *Anaconda* (Anaconda *prompt*) e com o *Spyder*.

Como já tivemos a oportunidade de ver na aula prática, 
para além de expressões aritméticas elementares, é possível usar expressões para outras expressões, numéricas, cadeias de carateres ou lógicas.

#### Exemplos de expressões numéricas

2 + 2 

3 * 5 

1 / 2 

3\**2 

#### Relembremos

2 + 2

x = 2 ; 3 - x

3 * 5 

1 / 2

3**2

#### Exemplos de cadeias de carateres (strings)

nome + apelido 

nome + ' ' + apelido

print (nome, apelido) 

nome[0]

nome[0] + apelido[0] 

nome[0:2] + apelido[0:2]


#### Experimentemos

nome + apelido 

nome + ' ' + apelido

print (nome, apelido) 

# Isto é muito importante, note que começa em 0
nome[0]

nome[0] + apelido[0] 

nome[0:2] + apelido[0:1]

#### Exemplos de expressões lógicas

True 

False

True == True

True != True

True != False

True or False 

True and False 

not(True) 

not(False) 


##### Experimentemos

True 

False

True == True

not(True) 

True or False 

True and False 

#### Recordar os operadores lógicos

##### not (Negação)

| A | not A |
| - |  ----------|
| True|False|
| False|True|

##### and (e lógico)

| A | B | A and B |
| - | - | ----------|
| False | False| False|
| False|True| False |
| True | False | False|
| True | True | True |

##### or ( ou lógico)

| A | B | A or B |
| - | - | ----------|
| False | False | False |
| False | True | True |
| True | False | True|
| True | True | True |

# Faça variar os valores de a e b e a operação lógica
a = True; b = not a; a and b 

#### Ainda expressões

print (primos_ate_10)

print (primos_ate_10[0]) # Note que o primeiro elemento está na posição 0  
print (primos_ate_10[4]) # o último está na posição 4
print (primos_ate_10[-1]) # ou seja, na primeira posição a contar do fim

primos_ate_10 + primos_ate_10

primos_ate_10 * 3

## Programação em Python 
### I - Interrogações e ciclos


É do conhecimento geral que os computadores fazem aquilo para que foram programados. Mas representar "coisas", dar-lhes nomes, e operar com/sobre elas, usando expressões, não é suficiente.

As ações a desempenhar dependem das circunstâncias. Por isso, surgiram formas de definir o que vai ser, ou não, feito. Na base do controlo de execução estão a avaliação das circunstâncias pela interrogação de estados significativos e a decisão de prosseguir ou repetir.

    - if
        Se <algo se verifica> <faça-se>
        Se <acabou o filme> <sair da sala>
    - while
        Enquanto <algo se verifica> <faça-se>
        Enquanto <o filme decorre> <silêncio>
    - for
        Para <enumeração do elementos do conjunto> <faça-se>
        Para <as senhoras de um grupo> <entregar uma flor>
        
#### Exemplos

a = 6
if (a%2)==0:
    # a identação é importante
    print(a, 'é par')

a = 5
if (a%2)==0:
   print(a, 'é par')
else:
   print(a, 'não é par')

a = -4
if (a == 0):
    print('a é zero')
elif (a > 0):
    print ('a é positivo')
else:
    print('a é negativo')

a = 3
while (a >= 0):
    # a identação é importante
    print (a)
    a -= 1 # O mesmo que a = a - 1

a = 3
for num in range(a+1):
    # a identação é importante
    print(num)

a = 3
for num in range(a, -1, -1):
    print(num)

## Programação em Python 
### O - Organizar

Agora que já temos as ferramentas essenciais, precisamos de preparar a nossa solução computacional. Usamos as funções do Python e, quando não existirem, fazemos as funções necessárias. Várias funções podem ser reunidas para criar uma solução, o nosso programa.

Vamos começar com um programa _muito_ simples, tão simples que é desnecessário: quero somar dois números inteiros.
Na resolução deste problema:
+ precisamos saber quais são as parcelas (*input*) e
+ precisamos de adicionar as parcelas para obtermos a soma (*processamento*)
+ precisamos de apresentar uma mensagem com as parcelas e a soma resultante (*output*).

Temos pois que organizar a nossa solução na forma de um programa de forma que cumpra o seu objetivo mas com cada parte separada de forma a que possamos testar e, mais importante, possamos reutilizar noutros programas que venhamos a precisar.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Authors: Margarida Madeira e Moura
# Contacts: mmadeira@ualg.pt

# Exemplo inicial de um programa
def soma (x,y):
	""" Função que devolve a soma de dois números.

	Args:
	    x (int): uma parcela
	    y (int): outra parcela

	Returns:
	    int: a soma das duas parcelas

	Examples:
	    >>> soma (2, 3)
	    5
	    >>> soma (4, 5) 
	    9
	"""
	return x + y

def testar_soma():
    """ O teste da função soma:
    lê os dados, chama a função e escreve os resultados """
    x = int(input())
    y = int(input())
    
    result = soma(x, y)
    
    print ("A soma de",x,"com",y,"é",result)

# Se o nosso programa for chamado diretamente a partir da consola 
# é preciso indicar por onde se começa 
if __name__ == "__main__":
    testar_soma()
    print("Feito!")

## Programação em Python 
### U - Usar

Porque o nosso programa está definido com várias funções podemos dar-lhe vários usos.

Para além de o podermos ter no *notebook*, podemos guardá-lo num ficheiro de extensão .py e chamá-lo na *prompt*.
    > python P1B.py

Mas podemos também usar as funções que aqui definimos.

testar_soma()
# Compare com o resultado anterior. Porque é que é diferente?

a, b = 4, 5 # Podemos fazer mais do que uma atribuição
soma(a,b)   # Note que os argumentos a e b da função são diferentes 
            # dos parâmetros x e y