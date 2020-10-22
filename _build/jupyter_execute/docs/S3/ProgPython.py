# Programação em Python 


## Objetivos de aprendizagem

Nesta lição, veremos de forma mais abrangente, a linguagem Python.


1. Expressões com tipos de dados nativos simples, incluindo a indexação de strings
1. Interrogações e ciclo *while*


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

frase = 'Python é muito giro e interessante!'

# Isto é muito importante, note que começa em 0
frase[0]

frase[0:6]

Os índices negativos podem ser entendidos como *a contar do fim*

frase[-1]

frase[-13:-1]

#### Operações com valores lógicos

Os valores lógicos (de tipo *bool*) podem assumir os valores **False** e **True**. Usamos:

    == para a igualdade. E não confunda com = da atribuição
    != para a negação
    not() também para a negação
    or para conjunção
    and para a disjunção


##### Exemplos

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

# Experimente: faça variar os valores de a e b e a operação lógica
a = True; b = not a; a and b 

### Interrogações e ciclo *while*

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

Queremos apresentar uma mensagem a indicar se um número é maior, igual, ou menor que zero.

Vamos esboçar a solução e melhorando progressivamente.


A variável *num* representará o nosso número neste caso.

num = 4

Para começar, queremos a mensagem para indicar se o número é maior que zero 

if (num > 0):
    # a identação é importante
    print('{} é maior que zero'.format(num))

Agora que isso está, acrescentamos outro caso. E para testar esse caso, mudamos o valor de *num*

num = -2

if (num > 0):
    print('{} é maior que zero'.format(num))
else:
    print('{} não é maior que zero'.format(num))

Mas não ser maior que zero, não é suficiente. 

Agora precisávamos de outro teste para saber se é zero, ou menor que zero.

num = 0 

if (num > 0):
    print('{} é maior que zero'.format(num))
elif (num == 0):
    print('{} é igual a zero'.format(num))
else:
    print('{} é menor que zero'.format(num))

Vejamos outro exemplo: queremos saber se um número é par.

Ora um número par é divisível por 2, ou seja, o resto da divisão por dois é zero.

num = 6

if (num%2) == 0:
    # a identação é importante
    print(num, 'é par')

num = 5

if (num%2) == 0:
   print(num, 'é par')
else:
   print(num, 'não é par')

Por vezes, queremos tratar toda uma gama de elementos, mas não sabemos quantos são.
Sabemos, isso sim, em que condições queremos fazer esse "tratamento".

Por exemplo, queremos apresentar os elementos $a$ do intervalo $ [0, 5[ $ sabendo que $a \in N$

a = 0
while (a < 5):
    # a identação é importante
    print (a)
    a += 1 # O mesmo que a = a + 1


Se quisessemos os valores de $[0, 3]$ por ordem decrescente, podíamos fazer

a = 3
while (a >= 0):
    # a identação é importante
    print (a)
    a -= 1 # O mesmo que a = a - 1

Criando expressões com estes operadores e conseguindo moldar o nosso programa às circunstâncias, já conseguimos fazer muitas coisas.

Vejamos agora o cálculo do fatorial de um número.

Queremos calcular o fatorial de um número usando a expressão $n! = n * (n-1)!$, para  $n > 1$

def fatorial_r(n):
    """Calculo do fatorial de um número.
    n! = n * (n-1)! para n > 1
    """
    
    resultado = 1 # Elemento neutro da multiplicação 
    if (n>1):
        resultado = n * fatorial_r(n-1)
    
    return resultado
    


print(fatorial_r(5))

Queremos agora calcular o fatorial de um número usando a expressão $n! = n * (n-1) * ... * 2$, para  $n > 0$

def fatorial_i(n):
    """Calculo do fatorial de um número.
    n! = n * (n-1) * ... * 2
    """
    
    resultado = 1 # Elemento neutro da multiplicação 
    while (n>1):
        resultado *= n 
        n -= 1        
    
    return resultado

print(fatorial_i(5))