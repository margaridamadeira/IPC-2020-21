#!/usr/bin/env python
# coding: utf-8

# # Programação em Python - parte 3
# 
# Vamos ver mais alguns aspetos da linguagem Python, nomeadamente:
# 
# 
# 1. a utilização de listas
# 1. a leitura da consola, vários valores por linha e até ao fim dos dados
# 1. escrita formatada
# 

# ## Tipo de dados: lista
# 
# ### Recordemos
# 
# Python é uma linguagem de programação *orientada a objetos*. Já abordámos o conceito de objetos e ainda não é agora que vamos aprofundar este tema.
# Para já, será suficiente que se considere que cada objecto é caracterizado por um identificador, um valor corrente, e um conjunto de métodos e operações que lhe são aplicáveis (e que são determinados pela *classe* do objeto). 
# 
# Ora sucede também que o Python é uma linguagem *fortemente tipada*. Isto significa que se se aplicar uma operação a um valor inadequado resulta numa mensagem de erro. 
# 
# O sistema de tipos é dinâmico e os tipos são implícitos: se por um lado, não é necessário declarar o tipo, por outro lado cada expressão tem associado um objeto de determinado tipo.
# 
# Se o valor que está associado a um objeto é sempre o mesmo, o tipo diz-se *imutável*; se existirem métodos para alterar o valor associado a um objeto então o tipo diz-se *mutável*.

# #### Tipos básicos
# 
# Em Python, cada valor pertence a um determinado tipo. Esse tipo determina quais as operações que podem ser aplicadas a esse valor. Hoje (re)veremos alguns aspetos dos tipos numéricos, de sequências e de mapeamento.
# 
# Com esta perspectiva, vejamos em maior detalhe alguns tipos básicos com que já trabalhámos.
# 
# Alguns tipos básicos com que já trabalhámos são: números inteiros ( **int** ),  números reais ( **float** ) e valores lógicos ( **bool** ). Os tipos básicos são **imutáveis**.
# 
# Usando *type()* podemos ver o tipo. Experimentemos.

# In[1]:


type(1)


# In[2]:


type(1.0)


# In[3]:


type(True)


# In[4]:


type(2+2)


# In[5]:


type(2+2.0)


# In[6]:


type(2 == 2.0)


# #### Strings
# 
# Também já usámos cadeias de carateres ( **str** ), um tipo de sequências.

# In[7]:


type('Maria')


# In[8]:


nome = 'Maria'
nome[0]


# Mas
#     `nome[0] = 'm'` 
# não funciona porque as cadeias de carateres em Python são **imutáveis**.
# 
# Se tentasse teria um erro!

# In[9]:


# Porque as strings são sequências podemos fazer
nome = 'Maria'; 
for letra in nome:
    print(letra)


# ### Listas
# 
# As [listas](https://docs.python.org/pt-br/3/tutorial/introduction.html#lists) são um tipo de dados *composto* usado para agrupar outros valores. Este tipo de dados é também designado *iterável* ou *sequencial*. Não nos preocupemos para já demasiado com estas designações, teremos mais oportunidades de detalhar.
# 
# O que é muito interessante é que as listas são **mutáveis**.
# 
# Uma lista pode ser escrita como uma sequência de valores separados por vírgula e contidos entre parênteses retos. Embora as listas possam conter elementos de tipos variados, normalmente os elementos são todos do mesmo tipo. 
# 
# #### Introdução

# In[10]:


primos_até_10 = [2, 3, 5, 7]


# In[11]:


primos_até_10


# Podemos indexar a lista (ou seja, aceder a uma posição usando o índice)

# In[12]:


primos_até_10 [0]


# Se quiser saber quantos elementos tenho

# In[13]:


len(primos_até_10)


# Algumas operações alteram a lista, pelo que se não quiser alterações, devo ter o cuidado de guardar criar uma versão de trabalho.

# In[14]:


primos_até_10_invertido = primos_até_10.copy()
primos_até_10_invertido.reverse()
print(primos_até_10)
print(primos_até_10_invertido)


# Mas atenção: tenho que usar **.copy**.
# Se tivesse apenas criado uma nova variável, estava a falar da mesma lista.

# In[15]:


primos_até_10_invertido = primos_até_10 # sem o copy
primos_até_10_invertido.reverse()
print(primos_até_10)
print(primos_até_10_invertido)


# Vamos repor o exemplo e criar uma nova lista para conter, em breve, os números primos até 20.

# In[16]:


primos_até_10 = [2, 3, 5, 7]
primos_até_20 = []


# Começamos por acrescentar os primos_até_10, um a um 

# In[17]:


primos_até_20.append(primos_até_10[0])
primos_até_20.append(primos_até_10[1])
primos_até_20.append(primos_até_10[2])
primos_até_20.append(primos_até_10[3])

print(primos_até_20)


# Ou mesmo, todos de uma vez

# In[18]:


primos_até_20 = []
for elem in primos_até_10:
    primos_até_20.append(elem)
print(primos_até_20)


# **Atenção**: não podemos adicionar a lista de uma só vez.

# In[19]:


primos_até_20_temporário = []
primos_até_20_temporário.append(primos_até_10)
primos_até_20_temporário


# porque teríamos uma lista onde o primeiro elemento da lista seria uma lista! Não era isto que queríamos. 

# Acrescentemos agora alguns elementos

# In[20]:


primos_até_20.append(11)
primos_até_20.append(11) #repetimos o mesmo elemento
primos_até_20.append(13)
primos_até_20.append(17)
primos_até_20.append(19)


# In[21]:


print( primos_até_20 )


# Ups! E quantas vezes surge o elemento 11 na lista? e onde?

# In[22]:


primos_até_20.count(11)


# In[23]:


primos_até_20.index(11)


# Retiremos então o elemento da posição 4

# In[24]:


primos_até_20[4:5] = []
primos_até_20


# E podemos pedir o último elemento, o penúltimo, 

# In[25]:


primos_até_20[-1]


# In[26]:


primos_até_20[-2]


# Ou fazer algumas operações

# In[27]:


primos_até_10 + primos_até_10


# In[28]:


t_lista = primos_até_10 * 2
t_lista


# Podemos ordenar

# In[29]:


t_lista.sort() # ordenar, por omissão crescente
t_lista


# In[30]:


t_lista = primos_até_10 * 2
list.sort(t_lista, reverse=True) # ordenação decrescente
t_lista


# O que posso fazer com as listas, posso fazer com as *variáveis* do tipo lista.
# Experimente, no Spyder, fazer
# 
#         list.<Tab>
#         primos_até_10.<Tab>

# #### Range
# 
# Já falámos de *range*. Na verdade, **range** é um tipo (uma classe) e representa uma sequência imutável de números inteiros e é muito útil para ciclos específicos.

# In[31]:


for i in range(10):
    print(i, end = ' ')    


# In[32]:


inic = 5
fim = 50
passo = 5
list(range(inic, fim, passo))


# In[33]:


t_range = range(inic, fim, passo)
32 in t_range


# In[34]:


t_range[3]


# #### Outros usos de listas

# In[35]:


quadrados = [x**2 for x in range(10)]
quadrados


# #### Exemplo
# 
# Neste outro exemplo, queremos saber qual é o maior elemento da lista e onde está.
# Não vamos fazer duas funções, devolvemos dois valores a partir da mesma função.
# 
# Saber qual é o maior elemento consegue-se com uma estratégia simples: é o último elemento de uma lista ordenada.
# 
# Para saber onde está o maior elemento, procuro-o na lista original.
# 
# No Spyder, criamos um exemplo e ensaiamos as instruções que precisamos. Aqui no Jupyter Notebook, juntamos umas instruções de *print* para que tudo faça sentido.
# Depois reunimos as instruções numa função e experimentamos.
# 
# Vejamos, pois.

# In[36]:


# A minha lista de teste
tt_lista = [2, 5, 7, 1, 4, -16]


# In[37]:


# Faço já os ensaios pensando que a função vai ter como parâmetro t
t = list.copy(tt_lista)

t


# In[38]:


# Vou precisar de uma cópia para não perder a ordem original
v = list.copy(t)

# Uso o método sort das listas para ordenar os elementos na lista v
v.sort()

# E tenho então
v


# In[39]:


print('A minha lista ordenada é', v)


# In[40]:


# Guardo o maior elemento, que é o primeiro a contar do fim
maior = v[-1]


# In[41]:


print(f'O maior é {maior:d}')


# In[42]:


# E vejo onde estava na lista original
onde = t.index(maior)

print('A minha lista é', t)
print('O maior elemento é o {0:d} e está na posição {1:d}'.format(maior, onde))


# In[43]:


# Juntando tudo.
# A minha lista de teste
tt_lista


# In[44]:


# A minha função que devolve dois valores
def maior_onde(t):
    """Função que devolve o maior valor de uma lista e o seu índice."""
    v = list.copy(t)
    v.sort()
    maior = v[-1]
    onde = t.index(maior)
    return maior, onde


# In[45]:


# e aplico a função à minha lista de teste
maior_onde(tt_lista)
    


# In[46]:


x, y = maior_onde(tt_lista)
print ('x =', x ,' y =', y)


# (Leitura)=
# ## Leitura da consola

# Já vimos alguns casos em que aparecem mensagens de erro. Acontece que em alguns desses casos queremos _interceptar_ o erro, ou seja, não permitir que o programa termine por causa desse erro e reagir à situação de forma mais positiva. A forma de fazer isso é usar a instrução *try-except*.
# 
# A instrução *try-except* é constituída por dois blocos: o bloco do *try* e o bloco do *except*. No bloco do *try* incluímos as instruções quer poderão dar origem a erros. No bloco do *except*, incluímos o tratamento desse erro. Mas, tipicamente, indicamos quais os erros que desejamos tratar.
# 
# E usamos estas funcionalidades para ler dados da consola, tantas vezes quantas necessárias, e terminamos o programa graciosamente, sem erros.
# 
# No programa seguinte temos um ciclo *while* que não termina por si só. A forma que usamos para terminar graciosamente este programa é chamando a função de saída (*sys.exit()*). E chamamos a função de saída se a leitura dos dados não correr bem, nomeadamente se chegarmos ao fim dos dados - EOFError - ou se o utilizador primir as teclas <Ctrl><C> - KeyboardInterrupt.

# Nota: este programa deve ser experimentado na consola.
# 
# 
#     import sys
# 
#     def soma(x, y):
#         return int(x)+int(y)
# 
# 
#     def test_soma_e_segue():
#         while True:
#             try:
#                 line = input().split()
#             except (EOFError, KeyboardInterrupt):
#                 sys.exit(0)
#             if line:
#                 x,y = line
#                 z = soma(x,y)
#                 print(z)
#             else:
#                 sys.exit(0)
# 
#     if __name__ == '__main__':
#         test_soma_e_segue()
#   

# ## Apresentar informação
# 
# 
# Para apresentar informação usamos **print**. Já o usámos em algumas instruções simples. Na documentação do Python pode encontrar mais exemplos sobre [formas elaboradas de escrita](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#fancier-output-formatting).
# Vejamos alguns dos exemplos mais interessantes para agora.
# 

# In[47]:


from math import pi
print(pi)
print(f'O valor de pi é aproximadamente {pi:.3f}.')
print('O valor de pi é aproximadamente {0:.3f}.'.format(pi))
print('{0:1.3e}'.format(pi))


# In[48]:


for i in range(1,3):
    print('{0:f} x {1:d} ~= {2:1.3f} '.format(pi, i, i*pi))


# In[49]:


for i in range(1, 5):
    print('{0:d}{1:> 6d}'.format(i, 10**i))


# In[50]:


print ('Range(1,5) vai iterar sobre', end = ": ")
for i in range(1, 5):    
    print(i,  end = ";")


# Se quisermos todos os valores numa linha, podemos criar a string pretendida e apresentá-la de uma só vez.

# In[51]:


resultado = ''
for i in range(1, 5):
    if len(resultado) == 0:
        resultado = str(i)
    else:
        resultado = resultado + ' ' + str(i)
print(resultado)

