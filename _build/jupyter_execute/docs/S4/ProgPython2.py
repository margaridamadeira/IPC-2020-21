#!/usr/bin/env python
# coding: utf-8

# # Programação em Python - parte 2

# ## Objetivos de aprendizagem
# 
# Nesta lição, vamos dedicar especial atenção à manipulação de strings.  Teremos assim oportunidade de conhecer outra forma de controlar ciclos de execução e usar algumas das funções do Python. Em particular, veremos:
# 
# 1. Ciclo *for*
# 1. Função *len* e *range*
# 1. Funções nativas do Python 

# ### Ciclo *for*

# Sabemos que as ações a desempenhar dependem das circunstâncias e vimos duas formas de definir o que vai ser, ou não, feito. 
# 
#     - if
#         Se <algo se verifica> <faça-se>
#         Se <acabou o filme> <sair da sala>
#         
#     - while
#         Enquanto <algo se verifica> <faça-se>
#         Enquanto <o filme decorre> <silêncio>

# A instrução *if* é interessante quando temos uma ação pontual, ou seja, **se** a condição se aplica.
# 
# O ciclo *while* é especialmente interessante quando as ações são para ser feitas **enquanto** uma condição se verifica. Ou seja, quando precisamos de avaliar continuamente se devemos continuar a fazer determinada ação ou se já é suficiente.
# 
# Mas, em algumas situações, sabemos à partida que é para fazer e quantas vezes o queremos fazer. E é então que que escolhemos usar um ciclo *for*.
# 
#     - for
#         Para <enumeração do elementos do conjunto> <faça-se>
#         Para <as senhoras de um grupo> <entregar uma flor>

# #### Exemplo
# 
# Imagine que, por questões de acessibilidade, queriamos escrever entre cada carater de uma string um ponto ('.').
# 
# Uma string tem um número definido de carateres, ainda que não saibamos quantos são.
# 

# In[1]:


frase = 'Python é muito giro e interessante!'

for letra in frase:
    print(letra, end='.')


# ### Função *len*

# Sabemos que é possível indexar as strings, ou seja, indicar qual é a posição de um dado elemento da string.

# In[2]:


frase[0:6]


# E se quisessemos saber quantos carateres tem a string? 
# 
# Usávamos a função *len*.

# In[3]:


len(frase)


# A frase tem então 35 carateres. Como os índices começam em zero, então o 34º elemento terá que ser o ponto de exclamação.
# 
# Verifiquemos:

# In[4]:


frase[34]


# Isto é muito útil. Os carateres de uma string de dimensão $n$ podem ser acedidos nas posições, em Python, [ 0, n [ $.
# 
# Verifiquemos:

# In[5]:


frase[0:len(frase)]


# ### Função *range*
# 
# Imagine agora que queriamos escrever a frase ao contrário.
# Há várias alternativas.

# In[6]:


# Se não soubessemos melhor, fazíamos esta coisa
pos = len(frase)-1
while (pos >= 0):
    print(frase[pos], end='')
    pos -=1


# Mas se sabemos quantas vezes temos que fazer, não podemos usar um *for*?
# Podemos e devemos.
# 
# A função *range* produz uma sequência de inteiros, e podemos indicar o passo.

# In[7]:


for idx in range(5):
    print(idx, end='')


# In[8]:


for idx in range(5-1, -1, -1):
    print(idx, end='')


# Como ficaria então para inverter a frase?

# In[9]:


for pos in range(len(frase)-1, -1, -1):
    print(frase[pos], end='')
    


# ### Funções nativas do Python
# 
# Já vimos algumas das funções do Python. Vimos funções "gerais" e outras que são específicas de alguns tipos de dados.
# 
# #### Recordemos
# 

# In[10]:


abs(-4)


# In[11]:


type(-4)


# In[12]:


int('5')


# In[13]:


int(5.0)


# In[14]:


float('5')


# In[15]:


lido = '5.0'
print(lido.isnumeric())


# #### Conhecer novas funções
# 
# Para sabermos que funções estão disponíveis, no spyder ou mesmo num notebook, podemos usar a ajuda em linha. Experimente escrever
# 
# ```
# frase.
# ```
# 
# e percorra as sugestões.
# 
# Para saber mais, use a função *help*. Por exemplo, 
# 
# ```
# help(frase.count)
# ```
# 
# ##### Alguns exemplos

# In[16]:


help(frase.count)


# In[17]:


frase


# In[18]:


# quantas vezes aparece o carater 'o'
frase.count('o')


# In[19]:


# e onde aparece o primeiro?
frase.index('o')


# In[20]:


# E o segundo 'o'?
frase.index('o', 5)


# In[21]:


# E o terceiro?
frase.index('o', 14)


# In[22]:


# Vamos substituir os 'o's por '.'
nova_frase = frase.replace('o', '.')
print(nova_frase)


# Veja que outras funções para strings existem e experimente-as.
