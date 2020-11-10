#!/usr/bin/env python
# coding: utf-8

# # Programação em Python - parte 4

# 
# 
# ## Objetivos de aprendizagem
# 
# Já vimos alguns tipos de dados. Vamos agora conhecer mais alguns tipos de dados, nomeadamente:
# 
# + tuplos
# + conjuntos
# + dicionários

# ## Tuplos, conjuntos e dicionários
# 
# ### Enquadramento
# 
# Já sabemos que se o valor que está associado a um objeto é sempre o mesmo, o tipo diz-se *imutável*; se existirem métodos para alterar o valor associado a um objeto então o tipo diz-se *mutável*.
# 
# E sabemos que as strings e as listas têm algumas operações em comum, como indexação e corte. As strings são imutáveis e as listas são mutáveis.
# As strings e as listas (e range) são tipos de sequências. 

# ### Tuplos
# 
# Os tuplos, tal como as listas, são um tipo de dados composto usado para agrupar outros valores. Este tipo de dados é também designado iterável ou sequencial. 
# 
# Um tuplo pode ser escrito como uma sequência de valores separados por vírgula e contidos entre parênteses **curvos**. E o tuplo é um tipo **imutável**.

# Por exemplo, 

# In[1]:


t = 1, 2, 3, 4, 5;
t


# In[2]:


t[2]


# Se tentasse mudar um dos elementos fazendo 
# 
#     t[2] = 5
#     
# produziria erro. Isto acontece porque *t* é um tuplo

# In[3]:


type(t)


# Já vimos  uma utilização muito conveniente dos tuplos, na troca do conteúdo das variáveis.

# In[4]:


x = 5
y = 10
y,x = x,y
print('x =',x,'e y =', y)


# E não foi preciso uma variável auxiliar. 
# Se se pretender que uma função devolva dois (ou mais) valores, podemos usar tuplos como fizemos na função *maior_onde* da aula passada, aqui repetida.

# In[5]:


# A minha lista de teste
tt_lista = [2, 5, 7, 1, 4, -16]


# In[6]:


# A minha função que devolve dois valores
def maior_onde(t):
    """Função que devolve o maior valor de uma lista e o seu índice."""
    v = list.copy(t)
    v.sort()
    maior = v[-1]
    onde = t.index(maior)
    return maior, onde


# In[7]:


# ao aplicar a função à minha lista de teste, crio um tuplo
maior_onde(tt_lista)
    


# In[8]:


x, y = maior_onde(tt_lista)
print ('x =', x ,' y =', y)


# Para dois valores, podemos atribuir os elementos do tuplo a variáveis. Mas podemos lidar diretamente com o tuplo desta forma

# In[9]:


resultado = maior_onde(tt_lista)
type(resultado)


# In[10]:


print('O maior elemento é o {0:d} e está na posição {1:d}'.format(resultado[0], resultado[1]))


# Para criar um tuplo, basta-me uma vírgula ou parênteses curvos

# In[11]:


ex1_tuplo = 8,
ex2_tuplo = ()


# In[12]:


type(ex1_tuplo)


# Podemos saber quantos elementos temos num tuplo

# In[13]:


len(resultado), len(ex1_tuplo), len(ex2_tuplo)


# ### Conjuntos
# 
# Python também inclui um tipo de dados para conjuntos. Um conjunto em Python é entendido como uma coleção não ordenada sem elementos duplicados. Tipicamente os conjuntos são usados para verificar pertença, eliminar elementos repetidos, sendo também usados para apoiar operações matemáticas como união, interseção e diferença.  
# 

# In[14]:


# Inicialização com enumeração
vogais = {'a', 'e', 'i', 'o', 'u'}
semi_vogais = {'w', 'y'} # em inglês


# In[15]:


# Forma alternativa de inicialização 
letras = {chr(i) for i in range(97,97+26)}
print(letras, sep=' ')


# In[16]:


consoantes = set() # Inicialização de um conjunto vazio, desnecessário no caso presente
consoantes = letras - vogais - semi_vogais
print(consoantes)


# #### Operações sobre conjuntos

# In[17]:


# Criar um conjunto vazio
numeros = set()
# Verificar o tipo
type(numeros)


# In[18]:


numeros_ate_50 = {x for x in range(50)}

pares_ate_50 = {x for x in numeros_ate_50 if (x%2 == 0) }

multiplos_3_ate_50 = {x for x in numeros_ate_50 if (x%3 == 0) }

multiplos_5_ate_50 = {x for x in numeros_ate_50 if (x%5 == 0) }

multiplos_7_ate_50 = {x for x in numeros_ate_50 if (x%7 == 0) }


# In[19]:


# Multiplos de 5 que não são pares
multiplos_5_ate_50 - pares_ate_50                  # a e não b


# In[20]:


# Reunião
multiplos = pares_ate_50 | multiplos_3_ate_50 |             multiplos_5_ate_50 | multiplos_7_ate_50


# In[21]:


primeiros_primos = numeros_ate_50 - multiplos
print(primeiros_primos, sep = ' ')


# In[22]:


# As letras comuns
a = set('bioengenharia')
b = set('matemática')
a & b                              # a e b


# In[23]:


# as letras que existindo numa palavra não existem na outra
a ^ b                              # a ou exclusivo b


# ### Dicionários
# 
# A melhor forma de entender os dicionários é talvez como um conjunto não ordenado de pares chave:valor ( *key: value*). 
# Notacionalmente, usam-se chavetas para representar dicionários.
# 
# A chave pode ser de qualquer tipo imutável, como strings ou inteiros. O valor pode ser de qualquer tipo.
# 
# Para sabermos se uma chave existe no dicionário, usamos **in**.
# 

# In[24]:


telefone = {'UAlg': 289800100, 'FCT': 289800953, 'FE': 289800915 }
telefone


# In[25]:


telefone['UAlg']


# In[26]:


# Eliminar um elemento
del telefone['FE']


# In[27]:


telefone


# In[28]:


# Alterar o valor
telefone['UAlg'] = 289800900


# In[29]:


# Adicionar um elemento
telefone['FE'] = 289800915


# In[30]:


list(telefone.keys())


# In[31]:


list(telefone.values())


# In[32]:


'UAlg' in telefone.keys()


# In[33]:


'FCT' not in telefone.keys()


# In[34]:


# Percorrer o dicionário
for k, v in telefone.items():
    print('O número da {0:s} é {1:d}'.format(k,v))


# ### Leitura recomendada
# 
# O tutorial sobre [Estruturas de dados](https://docs.python.org/pt-br/3.8/tutorial/datastructures.html), em particular:
# 
# + revisão de [listas](https://docs.python.org/pt-br/3.8/tutorial/datastructures.html#more-on-lists)
# + [tuplos](https://docs.python.org/pt-br/3.8/tutorial/datastructures.html#tuples-and-sequences)
# + [conjuntos](https://docs.python.org/pt-br/3.8/tutorial/datastructures.html#sets)
# + [dicionários](https://docs.python.org/pt-br/3.8/tutorial/datastructures.html#dictionaries)
# 
