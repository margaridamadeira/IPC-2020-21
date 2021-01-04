#!/usr/bin/env python
# coding: utf-8

# # Programação funcional

# ## Objetivos de aprendizagem
# 
# Vamos ver uma outra forma de abordar o desenho de um algoritmo, o paradigma funcional, nomeadamente:
# 
# + iteração
# + *filter*, *reduce*, *map*
# + funções lambda 

# ## Introdução
# 
# A programação funcional decompõe um problema num conjunto de funções. Idealmente as funções recebem dados e produzem resultados e não têm estados internos que possam afetar o comportamento da função.
# 
# Num programa funcional, os dados fluem pelas funções. Por ação de cada função, o domínio dá origem ao contradomínio. Há que ter atenção a possível efeitos colaterais, evitando que as estruturas sejam alteradas pela aplicação das funções, garantindo assim que o resultado depende única e exclusivamente da aplicação da função aos dados de entrada.

# ## Sequências e iteradores
# 
# Ao referirmos os tipos de dados falámos de sequências. As sequências básicas em Python são *list*, *tuple* e *range*. As *strings* são sequências imutáveis.
# 
# Numa sequência podemos referir um elemento pela sua posição relativa, que designamos *índice*. E podemos obter uma parte, segmentando, indicando o início e fim. 
# 

# In[1]:


lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print('Indexando a segunda posição, obtemos {}'.format(lista[1]))
print('Segmentando obtemos a segunda metade da lista :', lista[len(lista)//2:])


# Por uma lista ser um tipo iterável podemos usar a instrução *in* e apoiar o ciclo
# ```
# for elemento in lista:
# ```
# 
# Um iterador permite percorrer uma sequência, um elemento de cada vez, e sinaliza o fim de uma sequência pela exceção **StopIteration**. 
# 
# Python suporta a iteração sobre sequências. Conforme o tipo de dados em causa, a forma de criar um iterador poderá variar.

# ## Criação e uso de um iterador
# 
# A linguagem Python disponibiliza um conjunto de operações que permitem definir listas. Já usámos algumas dessas operações, como por exemplo *range*. 

# In[2]:


list(range(10))


# De facto, a operação *range* produz aquilo a que se chama um **iterador**, um conceito interessante na programação funcional. Um iterador representa um fluxo de dados, devolvendo um elemento de cada vez.
# 
# Criemos então um iterador *it* sobre a lista *c*:
# 

# In[3]:


c = [1, 3, 5, 8]
it = iter(c)
it


# Para obtermos cada elemento, usamos o *next*.

# In[4]:


next(it)


# In[5]:


next(it)


# In[6]:


next(it)


# In[7]:


next(it)


# Se tentarmos ir além do último elemento, surge a exceção *StopIteration*

# In[8]:


# Experimente, retirando o comentário da linha abaixo
# next(it)


# É de notar que, uma vez concluída a iteração, se necessitarmos de operar novamente sobre o fluxo de dados é necessário criar outro iterador.

# Para lidarmos com a exceção, num programa, usamos *try*-*except*. Vejamos este exemplo, desde o início, intercetando a exceção para que não haja um erro.

# In[9]:


c = [1, 3, 5, 8]
it = iter(c)

while True:
    try:
        print(next(it))
    except StopIteration:
        print('Acabou')
        break
print('Terminado!')


# In[ ]:





# ## Geradores
# 
# Numa construção *for* Python espera um objeto iterável.
# 
# E, estando definida uma ação (ou função), podemos aplicá-la a cada elemento. 
# 
# Não precisamos de definir uma função, podemos usar um gerador.
# 

# In[10]:


[x**2 for x in range(10)]


# In[11]:


c=[1, 3, 5, 8, 10, 15, 17]
[x**2 for x in c]


# In[12]:


[x**2 for x in c if x%2]


# In[13]:


[[x, y] for x in range(2) for y in range(2)]


# In[14]:


# Experimente, retirando o comentário da linha abaixo
# a, b = [int(x) for x in input().split()]


# ### Filter
# 
# Uma das aplicações comuns de iteradores é para aplicação de **filter**.
# 
# Até agora, se pretendessemos obter os números pares de uma lista, podíamos ter a seguinte implementação:

# In[15]:


def is_even(x):
    return (x % 2) == 0

lista = []
for elem in range(10):
    if is_even(elem):
        lista.append(elem)
        
print(lista)


# Embora esta construção por enquanto pareça estranha, podemos usar a iteração sobre listas para criar uma nova lista em que os elementos respeitam uma condição.

# In[16]:


def pares(w):
    return [y for y in w if y%2 == 0]

pares(range(10))


# A operação *pares* é um **filtro** porque seleciona alguns dos elementos da lista.

# Mas também podemos usar a seguinte implementação, talvez mais intuitiva:

# In[17]:


list(filter(is_even, range(10)))


# Com a aplicação de *filter* obtemos apenas os elementos para os quais a função *is_even* produziu True.

# ### Reduce
# 
# Outro exemplo da aplicação da programação funcional é **reduce**. 
# 
# Algumas funções do *Python*, como *sum*, *max* e *min*, recebem como argumento um objeto iterável.

# In[18]:


lista2 = list(range(5))
sum(lista2)


# In[19]:


max(lista2)


# In[20]:


min(lista2)


# As operações de **redução** produzem, a partir de uma sequência de valores, um único elemento.
# 
# Suponha que queremos o produto dos elementos da lista. 
# Para definirmos a nossa operação de redução, temos que importar *reduce* do módulo *functools*.
# 

# In[21]:


from functools import reduce


# In[22]:


def produto(x, y):
    return x*y

print(reduce(produto,range(1, 6)))


# ### Map
# 
# Outra exemplo do suporte que *Python* oferece para a programação funcional é **map**.
# 
# Neste caso, sobre um objeto iterável, aplica-se uma operação ou função.

# In[23]:


def cubo(x):
    return x*x*x

list(map(cubo, range(10)))


# ## Funções lambda 
# 
# A criação de uma função com uma única instrução pode ser evitada usando **lambda**.
# 
# 
# O formato é
# ```
# lambda argumentos: expressão
# ```
# 
# Vejamos então os exemplos anteriores, usando estas funções lambda.
# 

# In[24]:


# is_even
list(filter(lambda x: x%2==0, range(10)))


# In[25]:


from functools import reduce

# Note a diferença, reduce consome dois elementos para produzir um
print(reduce(lambda x, y: x*y, range(1,6)))


# In[26]:


list(map(lambda x: x*x*x, range(10)))


# ## Resumo
# 
# As operações de **filter** produzem uma sequência com os valores da sequência original onde a função de filtro foi avaliada como True.
# 
# As operações de **reduce** produzem um valor que resulta da aplicação da função de redução aos elementos da sequência.
# 
# As operações de **map** produzem uma sequência de valores pela aplicação da função a cada elemento do objeto iterável.
# 
# A expressão *lambda* permite criar

# ### Bibliografia
# 
# *Think Python: How to think like a computer scientist*: A. Downey, Green Tea Press, 2012
# http://greenteapress.com/thinkpython2/html/thinkpython2011.html#sec120
# 
# Sobre suporte ao paradigma funcional https://docs.python.org/3/howto/functional.html

# ### Exercícios exemplificativos
# 
# Sem usar ciclos for, implemente soluções para os seguintes casos:
# Considere que temos vários nomes
# 
# 1. Pretende-se retirar as partículas 'de' 'da' 'do'
# 1. Pretende-se garantir que todas as palavras começam por maiúscula.
# 
# 

# In[27]:


nome = 'ana maria da silva'


# In[28]:


nome_partido = nome.split()


# In[29]:


def nao_particula(palavra):
    return (palavra not in ['de', 'da', 'do'])


# In[30]:


nome_simples = list(filter(nao_particula, nome.split()))


# In[31]:


def maiuscula (palavra):
    return palavra.capitalize()


# In[32]:


nome_corrigido = list(map(maiuscula, nome_simples))


# In[33]:


print(nome)


# In[34]:


print(nome_corrigido)

