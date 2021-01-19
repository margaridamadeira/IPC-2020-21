#!/usr/bin/env python
# coding: utf-8

# ## Introdução ao Matplotlib
# 
# ### Gráficos em Python
# 
# A representação gráfica da informação é frequentemente necessária. 
# Como existem várias abordagens possíveis em Python, revisitaremos este tema.
# 
# Hoje usaremos a biblioteca **Matplotlib** (https://matplotlib.org/).

# In[1]:


import pylab as plt


amostras = []
funcLinear = []
funcQuad = []
funcCubic = []
funcExp = []


for i in range(0, 30):
    amostras.append(i)
    funcLinear.append(i)
    funcQuad.append(i**2)
    funcCubic.append(i**3)
    funcExp.append(1.5**i)
    


# In[2]:


# caso 1
plt.plot(amostras, funcLinear)
plt.plot(amostras, funcQuad)
plt.plot(amostras, funcCubic)
plt.plot(amostras, funcExp)
plt.show() # no spyder não é preciso 


# In[3]:


# Tudo junto não se percebe nada
# caso 2
plt.figure('lin')
plt.plot(amostras, funcLinear)
plt.figure('quad')
plt.plot(amostras, funcQuad)
plt.figure('cubic')
plt.plot(amostras, funcCubic)
plt.figure('expo')
plt.plot(amostras, funcExp)
plt.show()


# In[4]:


# Mas o que significam os eixos?
# caso 3 
plt.figure('lin')
plt.xlabel('pontos')
plt.ylabel('Função linear')
plt.plot(amostras, funcLinear)
plt.figure('quad')
plt.plot(amostras, funcQuad)
plt.figure('cubic')
plt.plot(amostras, funcCubic)
plt.figure('expo')
plt.plot(amostras, funcExp)
plt.figure('quad') # note a referência à figura
plt.ylabel('função quadrática') 
plt.show()


# In[5]:


# E que tal um título para cada gráfico?
# caso 4 
plt.figure('lin') # <-- identifico o gráfico 
plt.plot(amostras, funcLinear)
plt.figure('quad')
plt.plot(amostras, funcQuad)
plt.figure('cubic')
plt.plot(amostras, funcCubic)
plt.figure('expo')
plt.plot(amostras, funcExp)

plt.figure('lin') # <-- e depois posso voltar a referi-lo
plt.title('Linear')
plt.figure('quad')
plt.title('Quadrática')
plt.figure('cubic')
plt.title('Cúbica')
plt.figure('expo')
plt.title('Exponential')
plt.show()


# In[6]:


# é boa política limpar o gráfico assim que criado
# caso 5
plt.figure('lin')
plt.clf()
plt.plot(amostras, funcLinear)
plt.figure('quad')
plt.clf()
plt.plot(amostras, funcQuad)
plt.figure('cubic')
plt.clf()
plt.plot(amostras, funcCubic)
plt.figure('expo')
plt.clf()
plt.plot(amostras, funcExp)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadrática')
plt.figure('cubic')
plt.title('Cúbica')
plt.figure('expo')
plt.title('Exponential')
plt.show()


# In[7]:


# Mas para comparação, é preferível se o eixo dos yys for o mesmo
# caso 6
plt.figure('lin')
plt.clf()
plt.ylim(0,1000) # <--------------------
plt.plot(amostras, funcLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0,1000) # <--------------------
plt.plot(amostras, funcQuad)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadrática')
plt.show()


# In[8]:


# Aliás, dois a dois talvez facilite a comparação
# caso 7
plt.figure('lin quad')
plt.clf()
plt.plot(amostras, funcLinear) # <--------------------
plt.plot(amostras, funcQuad)   # <--------------------
plt.figure('cubic exp')
plt.clf()
plt.plot(amostras, funcCubic) # <--------------------
plt.plot(amostras, funcExp)   # <--------------------
plt.figure('lin quad')
plt.title('Linear vs. Quadrática')
plt.figure('cubic exp')
plt.title('Cúbica vs. Exponential')
plt.show()


# In[9]:


# Adicionando legenda 
# caso 8
plt.figure('lin quad')
plt.clf()
plt.plot(amostras, funcLinear, label = 'linear') # <----- label -----------
plt.plot(amostras, funcQuad, label = 'Quadrática')
plt.legend(loc = 'upper left') # <--------------------
plt.title('Linear vs. Quadrática')
plt.figure('cubic exp')
plt.clf()
plt.plot(amostras, funcCubic, label = 'cubic')
plt.plot(amostras, funcExp, label = 'exponencial')
plt.legend()
plt.title('Cúbica vs. Exponential')
plt.show()


# In[10]:


# e mudando cor, marca
# caso 9
plt.figure('lin quad')
plt.clf()
plt.plot(amostras, funcLinear, 'b-', label = 'linear') # <-----------------
plt.plot(amostras, funcQuad,'ro', label = 'Quadrática') # <----------------
plt.legend(loc = 'upper left')
plt.title('Linear vs. Quadrática')
plt.figure('cubic exp')
plt.clf()
plt.plot(amostras, funcCubic, 'g^', label = 'cubic')
plt.plot(amostras, funcExp, 'r--',label = 'exponencial')
plt.legend()
plt.title('Cúbica vs. exponencial')
plt.show()


# In[11]:


# e espessura
# caso 10
plt.figure('lin quad')
plt.clf()
plt.plot(amostras, funcLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.plot(amostras, funcQuad,'r', label = 'Quadrática', linewidth = 3.0)
plt.legend(loc = 'upper left')
plt.title('Linear vs. Quadrática')
plt.figure('cubic exp')
plt.clf()
plt.plot(amostras, funcCubic, 'g--', label = 'cubic', linewidth = 4.0)
plt.plot(amostras, funcExp, 'r',label = 'exponencial', linewidth = 5.0)
plt.legend()
plt.title('Cúbica vs. exponencial')
plt.show()


# In[12]:


# É possível ter subplots

# caso 11
plt.figure('lin quad')
plt.clf()

plt.subplot(211) # <--- Duas linhas, uma coluna, primeira posição
plt.ylim(0, 900)
plt.plot(amostras, funcLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.subplot(212) # <--- Duas linhas, uma coluna, segunda posição
plt.ylim(0, 900)
plt.plot(amostras, funcQuad,'r', label = 'Quadrática', linewidth = 3.0)
plt.legend(loc = 'upper left')

plt.title('Linear vs. Quadrática')


# In[13]:


# e usar notação científica
plt.figure('cubic exp')
plt.clf()
plt.subplot(121) # <--- Uma linha, duas colunas, primeira posição
plt.ticklabel_format(style='sci', axis = 'y', scilimits=(0,0)) # <-----
plt.ylim(0, 140000)
plt.plot(amostras, funcCubic, 'g--', label = 'cubic', linewidth = 4.0)
plt.subplot(122) # <--- Uma linha, duas colunas, segunda posição
plt.ticklabel_format(style='sci', axis = 'y', scilimits=(0,0))
plt.ylim(0, 140000)
plt.plot(amostras, funcExp, 'r.',label = 'exponencial', linewidth = 5.0)
plt.legend()
plt.title('Cúbica vs. exponencial')
plt.show()


# In[14]:


# E mudar a escala 
# caso 12
plt.figure('cubic exp log')
plt.clf()
plt.plot(amostras, funcCubic, 'g--', label = 'cubic', linewidth = 2.0)
plt.plot(amostras, funcExp, 'r',label = 'exponencial', linewidth = 4.0)
plt.yscale('log') # <---------------------------------------------------
plt.legend()
plt.title('Cúbica vs. exponencial')

# Ou não
plt.figure('cubic exp linear')
plt.clf()
plt.plot(amostras, funcCubic, 'g--', label = 'cubic', linewidth = 2.0)
plt.plot(amostras, funcExp, 'r',label = 'exponencial', linewidth = 4.0)
plt.legend()
plt.title('Cúbica vs. exponencial')
plt.show()

