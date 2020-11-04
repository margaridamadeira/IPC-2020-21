#!/usr/bin/env python
# coding: utf-8

# # Começar a programar

# ## Objetivos de aprendizagem
# 
# Nesta lição veremos:
# 
# 1. os diferentes tipos de dados nativos simples (numéricos, alfanumérico, lógico e _None_)
# 1. como criar e usar variáveis
# 1. como usar e definir funções
# 

# ### Tipos de dados nativos simples
# 
# Para resolvermos o nosso problema e criarmos uma solução, temos que ser capazes de representar a realidade.
# A linguagem Python considera de raiz (nativamente) tipos de dados, uns simples outros nem tanto. Começemos pelos tipos de dados simples.
# 

# #### Tipos de dados númericos
# 
# Na semana passada tivemos a oportunidade de experimentar o uso do Python como calculadora e começar a trabalhar com números. Os tipos de dados numéricos incluem os números inteiros (*int*), os números reais (*float*, ou seja, com vírgula flutuante) e os números complexos (*complex*).
# 
# Já conhecemos, da Matemática, os números inteiros ($Z$) e os números reais ($R$). Pode ser que conheçam
# Por exemplo, 
# 
# > $ 2 \in N$
# 
# > $ 2.0 \notin N$
# 
# > $ 2.0 \in R$
# 
# 
# Há uma forma de determinarmos qual o tipo de dados, usando a função nativa do Python *type*.

# In[1]:


type(2)


# In[2]:


type(2.0)


# Os números complexos são representados em Python usando a forma algébrica, usando-se 'j' ou 'J' na parte imaginária. 

# In[3]:


type(3 + 2j)


# #### Tipos de dados alfanuméricos
# 
# Se podemos representar números, também podemos representar caracteres. Os caracteres incluem letras e também algarismos, o caracter <espaço> e sinais de pontuação. O que recebemos do teclado é uma sequência de caracteres. 
# 
# O Python inclui um tipo para cadeias de caracteres, o tipo *str*  (em inglês *string*), usado para sequências imutáveis de dados textuais. 
# 
# Palavras e frases são do tipo *str*. É necessário delimitar a cadeia de caracteres, usando aspas, para que se saiba onde começa e acaba. As aspas podem ser simples (') ou duplas ("). 
# 

# In[4]:


type('Nome')


# In[5]:


type('2')


# In[6]:


type("2.0")


# #### Tipo lógico
# 
# Este tipo, *bool*, inclui as constantes *True* e *False*. Há um conjunto de operações, entre as quais conjunção, disjunção e negação, que usamos muito na programação.

# In[7]:


type(True)


# In[8]:


type(False)


# #### Tipo *NoneType*
# 
# E para terminar, há que referir o tipo *NoneType*. O único valor deste tipo é a constante *None*. 
# 

# In[9]:


type(None)


# ### Criar e usar variáveis
# 
# As constantes, como *True*, *False* ou *None*, nunca mudam. São _constantes_.
# 
# Já as variáveis, são como caixas, onde colocamos conteúdo.

# In[10]:


distancia_em_polegadas = 30
centimetros_por_polegada = 2.54
ponto = 3 + 2j
nome = 'Maria'
resposta = 'A Maria escolheu 5'


# É muito útil pois assim conseguimos fazer programas que se podem aplicar em mais de um caso.
# Para usar, preferimos o nome ao conteúdo. Por exemplo,
# 

# In[11]:


# distância em centímetros
distancia_em_polegadas * centimetros_por_polegada


# In[12]:


distancia_em_polegadas = 10


# In[13]:


# distância em centímetros
distancia_em_polegadas * centimetros_por_polegada


# ### Usar e definir funções
# 
# A linguagem Python considera de raiz algumas funções, e permite-nos criar funções novas.
# No nosso primeiro programa, vimos a função *print*, e usámo-la para apresentar uma cadeia de carateres.   

# In[14]:


print('Olá mundo')


# Usamos funções para reunir um conjunto de ações que vão considerar o que está dentro de parênteses. 

# In[15]:


print (distancia_em_polegadas)


# Se a função *print* apresenta o que está entre parênteses (argumento ou argumentos), podemos usar a função *print* para apresentar algo mais. 

# In[16]:


print ('Distância (in):', distancia_em_polegadas)
print ('Distância (cm):', distancia_em_polegadas * centimetros_por_polegada)


# Se quisermos agilizar o processo, podemos criar uma função que recebe a distância em polegadas e a apresenta em centímetros.
# 
# A ideia seria poder fazer
# 
# > print ('Distância (in):', distancia_em_polegadas)
# 
# > resultado = converte_polegada_para_centimetro(distancia_em_polegadas)
# 
# > print('Distância (cm):', resultado)

# ou mesmo
# 
# > print ('Distância (in):', distancia_em_polegadas)
# 
# > print('Distância (cm):', converte_polegada_para_centimetro(distancia_em_polegadas))

# Em qualquer dos casos, queremos uma função com o nome *converte_polegada_para_centimento* que recebe a distância em polegadas e devolve a distância em centímetros.

# In[17]:


def converte_polegada_para_centimetro(dist_polegadas):
    """Função que converte uma distância de polegadas para centímetros."""

    centimetros_por_polegada = 2.54
    resultado = dist_polegadas * centimetros_por_polegada
    return resultado 


# Note que as instruções dentro da função estão alinhadas a quatro espaços (ou um `<tab>`).
# O alinhamento é _muito_ importante em Python, pois indica um bloco de código.
# 
# Testemos então.

# In[18]:


print ('Distância (in):', distancia_em_polegadas)

print('Distância (cm):', converte_polegada_para_centimetro(distancia_em_polegadas))


# Ou

# In[19]:


print (distancia_em_polegadas, '(in) corresponde a', converte_polegada_para_centimetro(distancia_em_polegadas), '(cm)')


# Agora é muito mais simples usar.

# In[20]:


distancia_em_polegadas = 15
print (distancia_em_polegadas, '(in) corresponde a', converte_polegada_para_centimetro(distancia_em_polegadas), '(cm)')


# ## Em resumo
# 
# A linguagem Python considera diferentes tipos de dados. De entre os tipos de dados simples, vimos exemplos de dados numéricos, alfanuméricos, lógicos e do tipo TypeNone. Para saber qual é o tipo, podemos usar a função *type*.
# 
# As variáveis são identificadas por um nome (identificador) e são criadas de forma dinâmica quando lhes atribuímos conteúdo. Depois de criada uma variável, em vez de referirmos o conteúdo, referimos o nome. 
# 
# Para usar uma função, indicamos dentro dos parênteses o valor ou variável que a função deve considerar. Para criarmos uma função, usamos `def ` seguido do nome que queremos dar à função e indicando dentro de parênteses o identificador do argumento. Entre as três aspas duplas colocamos a informação de ajuda. As instruções que fazem parte da função devem estar alinhadas a quatro espaços (ou um `<tab>`), pelo menos. Usamos o return para indicar o valor ou variável que a função calculou.
# 
# 
