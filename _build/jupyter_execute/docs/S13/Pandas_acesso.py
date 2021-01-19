#!/usr/bin/env python
# coding: utf-8

# ## Seleção de elementos no pandas
# 
# <a href="https://pandas.pydata.org/pandas-docs/stable/dsintro.html">Fonte</a>

# In[1]:


import pandas as pd
import numpy as np


# ### Acesso elementar a elementos de uma Series

# In[2]:


s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:


s


# In[4]:


s.index


# In[5]:


for elem in s.index:
    print (elem)


# In[6]:


s.loc['a']


# In[7]:


for elem in s.index:
    print (s[elem])


# In[8]:


for elem in s.index:
    print (s.loc[elem])


# #### Por posição
# 
# Uma Series funciona de forma semelhante a um ndarray do NumPy

# In[9]:


s[3]


# In[10]:


for elem in range(len(s)):
    print (s[elem])


# In[11]:


for elem in range(len(s)):
    print (s.iloc[elem])


# In[12]:


print('4: %f, 3: %f, 1:%f '%(s[4], s[3], s[1]))


# In[13]:


s[1:3]


# In[14]:


s[2:-2]


# In[15]:


s[0:-2]


# ### Acesso elementar a elementos de uma Dataframe

# In[16]:


np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), 
                   columns=list('BCDE'))],
               axis=1)
df.iloc[7, 0] = np.nan


# In[17]:


df


# In[18]:


df.iloc[7]


# In[19]:


df.iloc[:,0]


# In[20]:


df.iloc[7,0]


# In[21]:


df['A']


# In[22]:


# loc[row, column] 
df.loc[7,'A']


# In[23]:


# Numpy style: [column][row]
df['A'][7]


# ### Sobre estilos

# In[24]:


df


# In[25]:


def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'green'
    return 'color: %s' % color


# In[26]:


s = df.style.applymap(color_negative_red)
s

