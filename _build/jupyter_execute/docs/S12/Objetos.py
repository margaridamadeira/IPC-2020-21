#!/usr/bin/env python
# coding: utf-8

# # Programação orientada por objetos
# 
# A programação orientada por objetos centra-se no facto de que existir um modelo (uma abstração) que incorpora caraterísticas e funcionalidades e que, na prática, é instanciado para preencher uma necessidade na aplicação.
# 
# 

# ## Objetivos de aprendizagem
# 
# 
# Já nos deparamos com o termo *objeto* em Python. Vamos agora ver como podemos criar classes e, consequentemente, novos tipos de objetos.

# ## Introdução
# 
# A programação orientada a objetos é um paradigma avançado que reúne dados (atributos ou propriedades) e as funções (métodos) para as manipular num objeto.
# 
# Esta abordagem permite maior estruturação que o paradigma declarativo pois teremos maior coesão entre as funções e os dados que elas manipulam.

# Uma classe é um tipo de objeto. Numa classe estão reunidos os métodos para operar sobre os atributos.

# Por exemplo, considere o operador '+'. Que funcionalidade oferece?

# Se estivermos a manipular inteiros, 

# In[1]:


x, y = 3, 4


# In[2]:


x + y


# o operador '+' representa a adição.

# Se estivermos a manipular strings,

# In[3]:


a, b = 'Bom ', 'dia'


# In[4]:


a + b


# Porquê?
# 
# Porque efetivamente o que temos é

# In[5]:


print(type(x))


# In[6]:


print(type(a))


# E a funcionalidade do método **+** depende da classe em causa.

# Uma classe é um tipo. Um objeto é uma instância da classe. Estando definida a classe, podemos criar objetos dessa classe.
# 
# O encapsulamento esconde o detalhe da implementação permitindo, no entanto, a programação usando objetos de uma classe.

# ## Criar uma classe
# 
# A criação de uma classe consegue com a palavra-chave **class**. 
# 
# Usamos *self* para, dentro da classe, nos referirmos à instância da classe.

# In[7]:


""" A classe Ponto
(c) Margarida Madeira e Moura, 2021
"""

class Ponto:
    """Definição de um ponto no espaço cartesiano"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# Criamos os objetos *p* e *q*

# In[8]:


p = Ponto()
q = Ponto(3, 4)


# Se, para verificar, usassemos uma instrução de *print*, o resultado não seria muito útil.

# In[9]:


print(p)


# Podíamos fazer 

# In[10]:


print('x =', p.x, 'y =', p.y)


# In[11]:


print('x =', q.x, 'y =', q.y)


# Vamos criar um *método* da classe Ponto para imprimir os valores. 
# 
# A nossa classe ficaria agora assim

# In[12]:


"""
A classe Ponto
(c) Margarida Madeira e Moura, 2021
"""

class Ponto:
    """Um ponto no espaço cartesiano"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        print('x =', self.x, 'y =', self.y)


# e usaríamos

# In[13]:


r = Ponto(0, 5)
s = Ponto(2, 5)

r.imprimir()
s.imprimir()


# Python prevê que se existir um método designado **__str__* esse método será usado na instrução de print do objeto. 
# 
# Alteremos então a nossa classe criando, no método *__str__* a string a apresentar.

# In[14]:


# -*- coding: utf-8 -*-

"""
A classe Ponto
(c) Margarida Madeira e Moura, 2021
"""

class Ponto:
    """Um ponto no espaço cartesiano"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return('x = ' + str(self.x) + ' y = ' + str(self.y))

    def imprimir(self):
        print('x =', self.x, 'y =', self.y)


# In[15]:


z = Ponto(-1, -3)
print(z)


# Queremos agora calcular a distância entre dois pontos.
# 
# Sabemos que a distância entre os pontos *P* e *Q* é dada por $\sqrt{(P.x - Q.x)^2 + (P.y-Q.y)^2) }$
# 
# A nossa classe ficaria agora com mais um método

# In[16]:


"""
A classe Ponto
(c) Margarida Madeira e Moura, 2021
"""

class Ponto:
    """Um ponto no espaço cartesiano"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return('x = ' + str(self.x) + ' y = ' + str(self.y))

    def imprimir(self):
        print('x =', self.x, 'y =', self.y)

    def distancia(self, outroPonto):
        """Distância entre dois pontos"""
        dist_x = self.x - outroPonto.x
        dist_y = self.y - outroPonto.y
        resultado = (dist_x**2 + dist_y**2)**0.5
        return(resultado)


# In[17]:


r = Ponto(0, 5)
s = Ponto(2, 5)
r.distancia(s)


# In[18]:


t = Ponto()
r.distancia(t)


# ## Composição de classes
# 
# Uma lista é um objeto da classe *list*. Podemos ter listas com inteiros, com strings, com diversos tipos de elementos.
# 
# Vamos agora criar uma classe Segmento, representando um segmento de reta definido a partir de dois dos seus pontos.

# In[19]:



"""
A classe Segmento
(c) Margarida Madeira e Moura, 2021

"""
from ponto import Ponto

class Segmento(Ponto):
    """Um segmento de reta, definido a partir de dois pontos no espaço cartesiano"""

    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    def __str__(self):
        return('A: ' + str(self.A)+ ' B: ' + str(self.B))

if __name__ == '__main__':
    s = Segmento(Ponto(), Ponto(3,4))
    print(s)


# E como o comprimento de um segmento de reta é dado pela distância dos seus pontos, poderíamos incluir mais um método na classe Segmento e teríamos

# In[20]:



"""
A classe Segmento
(c) Margarida Madeira e Moura, 2021

"""
from ponto import Ponto

class Segmento(Ponto):
    """Um segmento de reta, definido a partir de dois pontos no espaço cartesiano"""

    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    def __str__(self):
        return('A: ' + str(self.A)+ ' B: ' + str(self.B))

    def length(self):
        return(self.A.distancia(self.B))

if __name__ == '__main__':
    P = Ponto()
    Q = Ponto(3,4)
    print(P.distancia(Q))

    s = Segmento(Ponto(), Ponto(3,4))
    print(s)
    print(s.length())


# ## Exemplo: Biopython
# 
# Aceda ao [exemplo de sequências no tutorial do Biopython](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec9). Note que para definirmos uma sequência, importamos a classe *Seq* definida no módulo *Seq* de *Bio*. 
# 
# Se, no [repositório do Biopython](https://github.com/biopython/biopython), escolhermos *Bio* e então o módulo *Seq.py*, encontraremos na linha 286, a definição da classe.
# 

# ## Referências
# 
# [Classes](https://docs.python.org/pt-br/3/tutorial/classes.html) na documentação do Python.
# 
# Biopython, na [wikipédia](https://pt.wikipedia.org/wiki/Biopython).
# 
# Biopython, [documentação oficial](https://biopython.org/wiki/Documentation).
# 
# [Repositório](https://github.com/biopython/biopython) do Biopython.
