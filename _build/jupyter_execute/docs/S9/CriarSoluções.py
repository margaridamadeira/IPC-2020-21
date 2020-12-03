#!/usr/bin/env python
# coding: utf-8

# # Criação de soluções - parte 2
# 
# Hoje vamos ver algumas mais algumas técnicas para criar soluções mais robustas e mais complexas, aproveitando para consolidar o que já vimos de programação.
# 

# ## Objetivos de aprendizagem
# 
# Vamos ver algumas técnicas usadas no processo de criação de soluções computacionais, nomeadamente:
# 
# + Módulos
# + Testes usando as strings de documentação
# 

# ## Desenvolvimento modular
# 
# Quando os problemas se tornam mais complexos, o código do programa tende a ficar muito longo. Mas, no desenvolvimento de uma solução computacional, nem todo o código tem que estar no mesmo ficheiro.  
# 
# Dividir o programa em várias partes tem vantagens:
# + é mais fácil de manter
# + as partes são reutilizáveis
# 
# Para criar uma solução mais complexa, podemos criar scripts com cada uma das partes e depois, usando **import**, reunir essas partes. 

# ### Exemplo
# 
# Consideremos a conversão de temperaturas. 
# 
# Tendo já implementado as funções que fazem a conversão de temperatura em kelvin para celsius (*k2c*) e a conversão de temperaturas em celsius para farenheit (*c2f*), a conversão de temperaturas de kelvin para farenheit pode ser feita usando as funções já definidas.
# 
# Mas não é necessário copiar essas funções o novo script, podemos importá-las.
# 

# Vejamos o que temos na diretoria corrente:

# In[1]:


get_ipython().run_line_magic('ls', '')


# E o que temos já no nosso espaço de nomes:

# In[2]:


dir()


# Importemos um dos módulos que já tínhamos feito.

# In[3]:


import c2f


# E vejamos o que temos:

# In[4]:


dir()


# Apareceu (no final) c2f. Vejamos o que c2f é:

# In[5]:


type(c2f)


# E o que contém:

# In[6]:


dir(c2f)


# Usamos <nome do módulo>.<nome da função> para indicar uma função dentro de um módulo.
# Para nos referirmos à função c2f que está no módulo c2f, teríamos:

# In[7]:


help(c2f.c2f)


# Importemos também o outro módulo e testemos:

# In[8]:


import k2c


# In[9]:


kelvins = 273.15
resultado = c2f.c2f(k2c.k2c(kelvins))
print(resultado)


# E o nosso módulo ficaria:

# ```
# # -*- coding: utf-8 -*-
# 
# """
# kelvin para farenheit, usando import
# (c) Margarida Madeira e Moura, 2020
# """
# 
# import c2f, k2c
# 
# def k2f(kelvins: float) -> float:
#     """Função que converte uma temperatura de kelvin para farenheit.
#     
#     Exemplos:
#     >>> k2f(273.15)
#     32.0
#     >>> k2f(373.15)
#     212.0
#     
#     """
#     return c2f.c2f(k2c.k2c(kelvins))
# 
# 
# def test_k2f():
#     x = float(input())
#     z = k2f(x)
#     print(z)
#     
# if __name__ == '__main__':
#     test_k2f()
# ```

# Podemos também eliminar os módulos:

# In[10]:


del(c2f, k2c)


# e verificamos que já não existe:

# In[11]:


dir()


# Idealmente vamos buscar só o que precisamos, para não usar memória desnecessariamente:

# In[12]:


from c2f import c2f
from k2c import k2c


# Com a vantagem que já não precisamos prefixar o nome da função com o nome do módulo:

# In[13]:


help(c2f)


# In[14]:


help(k2c)


# E usaríamos apenas:

# In[15]:


kelvins = 273.15
resultado = c2f(k2c(kelvins))
print(resultado)


# E a nossa nova função ficaria:

# ```
# # -*- coding: utf-8 -*-
# 
# """
# kelvin para farenheit, usando import
# (c) Margarida Madeira e Moura, 2020
# """
# 
# from k2c import k2c
# from c2f import c2f
# 
# def k2f(kelvins: float) -> float:
#     """Função que converte uma temperatura de kelvin para farenheit.
#     
#     Exemplos:
#     >>> k2f(273.15)
#     32.0
#     >>> k2f(373.15)
#     212.0
#     
#     """
#     return c2f(k2c(kelvins))
# 
# 
# def test_k2f():
#     x = float(input())
#     z = k2f(x)
#     print(z)
#     
# if __name__ == '__main__':
#     test_k2f()
# ```

# ### Módulos padrão
# 
# Python inclui alguns módulos (veja A Biblioteca padrão do Python em https://docs.python.org/pt-br/3/library/index.html)
# 
# 
# Já usámos o *sys*, para podermos usar a função *sys.exit()* e assim forçar a saída do ciclo de leitura.
# 
# Outro módulo que já referimos, logo na apresentação de Python, foi *math* para acedermos às funções trignométricas.
# 
# Nesse caso, importámos tudo e assim não foi necessário prefixar as funções com o nome do módulo.
# 

# ## Testes usando as strings de documentação
# 
# O módulo *doctest* identifica as partes de texto nas strings de documentação que se parecem com sessões interativas do Python ('>>>') e, em seguida, executa as instruções correspondentes e verifica se o funcionamento atual corresponde ao descrito.
# 
# No script mostrado abaixo, foi incluída a chamada ao módulo de testes e também, a título de demonstração, um exemplo errado na documentação.

# ```
# # -*- coding: utf-8 -*-
# 
# """
# kelvin para farenheit, usando import e doctest
# (c) Margarida Madeira e Moura, 2020
# """
# 
# 
# from k2c import k2c
# from c2f import c2f
# 
# def k2f(kelvins: float) -> float:
#     """Função que converte uma temperatura de kelvin para farenheit.
#     
#     Exemplos:
#     >>> k2f(273.15)
#     32.0
#     >>> k2f(373.15)
#     212.0
#     >>> k2f(373.15) # errado
#     212.5
#     
#     """
#     return c2f(k2c(kelvins))
# 
# 
# def test_k2f():
#     x = float(input())
#     z = k2f(x)
#     print(z)
#     
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
#     test_k2f()
# ```

# Note que embora o script funcione, indica que teste falhou.
# 
# Recrie os exemplos na sua área e teste.
