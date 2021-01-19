#!/usr/bin/env python
# coding: utf-8

# ## Introdução ao NumPy
# 
# 
# *NumPy* é particularmente útil para produzir soluções rápidas de processamento vetorial. 
# 
# Leitura inicial:
# https://numpy.org/devdocs/user/quickstart.html
# 
# Leitura recomendada:
# http://www.scipy-lectures.org/intro/numpy
# 
# Documentação de referência:
# http://docs.scipy.org/
# 

# In[1]:


# Um exemplo
import numpy as np
a = np.array([0, 1, 2, 3])
a


# In[2]:


b = np.array([[0,1, 2],
              [3, 4, 5]])
b


# In[3]:


# dimensão da matriz
b.shape


# ### Documentação

# In[4]:


# Acesso à documentação 
help (np.array)


# In[5]:


# Em alternativa
get_ipython().run_line_magic('pinfo', 'np.array')


# In[6]:


# ou ainda
np.lookfor('create array')


# In[7]:


# ou ainda
get_ipython().run_line_magic('psearch', 'np.con*')


# ### Alguns exemplos

# In[8]:


# matriz com 1s
a = np.ones((3, 3)) 
a


# In[9]:


# matriz com 0s
b = np.zeros((2, 2))
b


# In[10]:


# Matrix com 1 na diagonal e demais elementos a zero
c = np.eye(3, dtype=int) 
c


# In[11]:


# Matrix com 1.0 na diagonal e demais elementos a zero
c = np.eye(3, dtype=float) 
c


# In[12]:


d = np.diag(np.array([1, 2, 3, 4]))
d


# In[13]:


a = np.arange(10)
a


# In[14]:


a[2:9:3] # [start:end:step]


# In[15]:


# Indexação dos elementos das matrizes
a = np.diag(np.arange(3))
a


# In[16]:


a[1, 1]


# In[17]:


a[2, 1] = 10 # third line, second column


# In[18]:


a


# In[19]:


# a segunda linha
a[1]


# In[20]:


# a segunda coluna
a[:,1]


# ### Operações elementares

# In[21]:


a = np.array( 10 * np.arange(4) )
a


# In[22]:


b = np.arange( 4 )
b


# In[23]:


c = a-b
c


# In[24]:


d = b**2
d


# In[25]:


d1 = d + 5
d1


# In[26]:


A = np.array( [[1,1],
            [0,1]] )
B = np.array( [[2,0],
            [3,4]] )


# In[27]:


C = A * B                       # produto elemento a elemento
C


# In[28]:


D = A @ B                       # produto de matrizes
D


# In[29]:


A.dot(B)                    # outra forma de multiplicar matrizes


# ### Exercícios
# Crie as matrizes abaixo (e atenção aos tipos de dados)

# In[30]:



[[1, 1, 1, 1],
 [1, 1, 1, 1],
 [1, 1, 1, 2],
 [1, 6, 1, 1]]

[[0., 0., 0., 0., 0.],
 [2., 0., 0., 0., 0.],
 [0., 3., 0., 0., 0.],
 [0., 0., 4., 0., 0.],
 [0., 0., 0., 5., 0.],
 [0., 0., 0., 0., 6.]]

