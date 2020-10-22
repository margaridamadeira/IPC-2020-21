# Programação em Python 


## Objetivos de aprendizagem

Nesta lição, veremos de forma mais abrangente, a linguagem Python.


1. Expressões com tipos de dados nativos simples, incluindo a indexação de strings
1. Interrogações e ciclo *while*
1. Funções nativas do python padrão


print('x = {0:d}; y = {1:d}'.format(x, y))

Mas o conteúdo não tem que ser sempre numérico. 

nome = 'Maria'
print(nome)

apelido = 'Silva'
apelido

### Expressões com tipos de dados nativos simples

Na semana passada tivemos a oportunidade de experimentar conhecer alguns tipos de dados nativos simples. Já tivemos a oportunidade de ver algumas expressões aritméticas elementares. Mas também é possível usar expressões para outras expressões, numéricas, cadeias de carateres ou lógicas.

#### Operações com *strings*

As cadeias de carateres (vulgo, *strings*) armazenam sequências alfanuméricas. Usamos:

    + para justaposição, isto é, concatenar
    * para repetição
    [pos] para indicar a posição do caracter a que nos referimos
    [pos1:pos2] para indicar a sequência que começa em *pos1* e vai até (não incluindo) *pos2*

##### Exemplos

nome = 'Maria'
apelido = 'Moura'
nome + ' ' + apelido 
print (nome, apelido)

nome_completo = nome + ' ' + apelido 
saudar = 'Bom dia,' + ' ' + nome_completo + '!'*3
print(saudar)

# Isto é muito importante, note que começa em 0
nome[0]

frase = 'Python é muito giro e interessante!'

frase[0:7]

frase[-1]

frase[-13:-1]

#### Operações com valores lógicos



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

## Programação em Python 
### I - Interrogações e ciclos


É do conhecimento geral que os computadores fazem aquilo para que foram programados. Mas representar "coisas", dar-lhes nomes, e operar com/sobre elas, usando expressões, não é suficiente.

As ações a desempenhar dependem das circunstâncias. Por isso, surgiram formas de definir o que vai ser, ou não, feito. Na base do controlo de execução estão a avaliação das circunstâncias pela interrogação de estados significativos e a decisão de prosseguir ou repetir.

Vejamos então, duas formas de controlar o fluxo de execução.

    - if
        Se <algo se verifica> <faça-se>
        Se <acabou o filme> <sair da sala>
    - while
        Enquanto <algo se verifica> <faça-se>
        Enquanto <o filme decorre> <silêncio>

        
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