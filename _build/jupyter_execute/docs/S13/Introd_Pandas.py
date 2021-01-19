#!/usr/bin/env python
# coding: utf-8

# # Introdução ao Pandas
# 
# 
# *pandas* é uma biblioteca de código aberto em Python   que dispõe de funcionalidades de importação, exportação e manipulação de dados para exploração e análise de dados.
# 
# 

# ## Introdução
# 
# Tipicamente, a exploração e análise de dados com *pandas* considera a importação dos módulos

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# e apoia-se nas funcionalidades obtidas com a utilização das estruturas de dados fundamentais em *pandas*: Series e DataFrame.

# #### Series
# 
# A primeira dessas estruturas é **Series** que representa um objeto unidimensional. As novidades principais desta estrutura são: os dados podem ter tipos distintos e possibilidade de definição explícita do índice.  
# 
# Por exemplo, 

# In[2]:


# a partir de um ndarray 
data = np.random.randint(10, 50, 5)
print('data é do tipo', type(data), '\n')


# In[3]:


indice = ['um', 'dois', 'tres', 'quatro', 'cinco']
s = pd.Series(data, index=indice)
s


# In[4]:


# a partir de um dicionário
d = {'a': 1., 'b': 2. , 'c': 4., 'd': 8., 'e':16., 'f':32.}
print('d é do tipo', type(data), '\n')
pot2 = pd.Series(d)
pot2


# In[5]:


# ou mesmo de um escalar
num = 3.14
sn = pd.Series(num, index = ['pi', 'outro pi', 'e ainda pi'])
sn


# #### Dataframes
# 
# Outra estrutura de dados fundamental no *pandas* é **DataFrame**, uma estrutura de dados composta por linhas e colunas e que pode ser entendida como um grupo de *Series*.

# In[6]:


d = {'2' : pot2,
     '3' : 3**np.log2(pot2)}
df = pd.DataFrame(d)
df


# In[7]:


mat = np.random.randint(16, size = (4, 4))
df1 = pd.DataFrame(mat)
df1


# #### Exemplos de uso

# In[8]:


df


# In[9]:


df['2']


# In[10]:


df['outro'] = df['2'] * df['3']
df


# In[11]:


meio = df[(df>10) & (df <100)].copy()
meio


# In[12]:


meio[meio.isnull()] = 0
meio


# In[13]:


maior = meio['3'].idxmax()
print(maior)


# In[14]:


meio['3'][maior]


# In[15]:


meio.describe()


# ## Referências adicionais
# 
# Leitura recomendada: http://pandas.pydata.org/pandas-docs/stable/tutorials.html
# 
# Documentação de referência: http://pandas.pydata.org/pandas-docs/stable/
