#!/usr/bin/env python
# coding: utf-8

# # Ficheiros

# ## Objetivos de aprendizagem
# 
# Vamos começar a ver como se trabalha com ficheiros de texto, nomeadamente:
# 
# + ler informação de ficheiros e 
# + escrever informação em ficheiros.
# 

# Os ficheiros permitem o armazenamento _persistente_ de informação. Essa informação pode estar organizada de diferentes formas e a forma de organização é por vezes indicada pelo tipo do ficheiro.
# 
# Python tem muitas funções para ler e escrever ficheiros e vamos começar com ficheiros de texto.

# ## Aceder a um ficheiro
# 
# Para trabalharmos com um ficheiro, temos primeiro de o abrir. Para tal, podemos utilizar a função *open*, que requer dois parâmetros: o nome do ficheiro-alvo e o modo. Há três modos possíveis:
# 
# + r - do inglês read, indica modo de leitura (o ficheiro está aberto para leitura);
# + w - do inglês write, indica modo de escrita (o ficheiro é aberto para escrita, e se existir um ficheiro com o mesmo nome, será apagado);
# + a - do inglês append, indica modo de adição (o ficheiro é aberto para acrescentar, o que significa que os dados só devem ser escritos depois dos dados existentes no ficheiro).
# 
# E o ficheiro deve ser fechado assim que já não seja necessário.
# 
# ## Ler informação de um ficheiro
# 
# Para abrir um ficheiro com o nome 'entrada.txt' para leitura, fazemos:

# In[1]:


f = open('entrada.txt', 'r')


# Esta instrução indicou ao Python que deve guardar no objeto de ficheiro *f* o resultado da operação de abertura do ficheiro em modo de leitura.
# 
# Para obtermos os dados do objeto de ficheiro *f* criado, podemos aplicar os seguintes métodos:
# + f.read(n) - que devolve *n* bytes de dados do ficheiro como uma cadeia de carateres (*string*). Quando o parâmetro de tamanho é omitido, todo o conteúdo do ficheiro será lido e devolvido.
# + f.readline() - que obtém uma única linha do ficheiro. Todas as linhas (exceto a última linha de ficheiro) terminam num carácter de quebra de linha (\n) *newline* . Para remover este carácter da extremidade de uma linha lida podemos utilizar o método .strip(). Note que cada vez que chamar .readline() obtém a próxima linha do ficheiro.
# + f.readlines() - devolve uma lista contendo todas as linhas do ficheiro. 
# 
# ### Usos comuns
# 
# Se precisarmos de obter uma determinada linha, podemos indicar o índice do item de lista.
# 
# Por exemplo, 

# In[2]:


f.readlines()[1]


# devolve a terceira linha do objeto de ficheiro *f*.
# 
# Aproveitando a ideia, uma forma alternativa de ler linhas é iterar sobre o objeto de ficheiro, com
# 

# In[3]:


f=open('entrada.txt', 'r')
for linha in f:
    print(linha, end='')


# Note que como não retiramos o carácter quebra de linha, não podemos permitir que o *print* termine com esse carácter.
# 
# Usando ciclos semelhantes a este, podemos fazer o que for preciso para todas e cada uma das linhas do ficheiro.
# 
# Se os dados do ficheiro não forem separados por novas linhas, mas sim por espaços brancos, vírgulas ou qualquer outro delimitador, então os comandos tal como apresentados acima e que devolvem os dados apenas sob a forma de linhas são insuficientes. 
# Nesses casos, podemos utilizar a instrução linha.split(). Esta instrução considera como delimitador o carácter quebra de linha e bem como o carácter branco ou seuqências de caracteres brancos. Por exemplo,
# 
# 

# In[4]:


"Python é muito giro e interessante!".split()


# Podemos especificar qual o delimitador que deve ser considerado.

# In[5]:


"Python, é muito giro, e é interessante!".split(',')


# Ao usarmos *.read()*, se não indicarmos quantos bytes queremos ler então todo o ficheiro é lido. Isto deve ser usado com cuidado pois o ficheiro poderá ocupar uma porção significativa da memória disponível.

# In[6]:


f=open('entrada.txt', 'r')
tudo = f.read()
tudo


# Nesse caso, podemos usar *.splitlines()* para separar a string no caráter quebra de linha e guardar cada segmento num item de uma lista.

# In[7]:


linhas = tudo.splitlines()
linhas


# Se tentar ler para além do fim do ficheiro o resultado é nulo. Mas o ficheiro ainda está aberto e, se a leitura está terminada, devemos fechar o ficheiro.

# In[8]:


f=open('entrada.txt', 'r')
for linha in f:
    print(linha, end='')

# Mudar de linha    
print()

vazio = f.readline()
print(len(vazio))

print('Fechado?',f.closed)
f.close()
print('Fechado?', f.closed)


# É uma boa prática usar *with* ao trabalhar com ficheiros. Com a vantagem que, ao terminar o ficheiro é fechado.

# In[9]:


with open('entrada.txt') as f:
    tudo = f.read()

print(tudo)
print('Fechado?',f.closed)


# Outro exemplo do uso de *with* na leitura linha a linha:

# In[10]:


with open('entrada.txt') as f:
    for linha in f:
        print('-> {}'.format(linha))


# ## Escrever informação num ficheiro
# 
# A escrita faz-se com o método *.write()*. 
# Para uma escrita bem sucedida há que ter em atenção que:
# + o ficheiro deve ter sido aberto de forma apropriada. O modo 'w' cria um ficheiro, o modo 'a' adiciona a um ficheiro se o ficheiro existir, senão cria-o.
# + A instrução *f.write (string)* escreve o conteúdo da string no ficheiro *f*. Se quisermos escrever algo que não uma string então devemos converter primeiro para *string* com a função str(). Se/quando quisermos mudança de linha, devemos incluir o carácter quebra de linha.
# + Se não estiver a usar a palavra-chave *with* o ficheiro deve ser fechado com *f.close()*. Caso o programa termine e o ficheiro não tenha sido fechado poderão perder-se dados.
# 
# 

# In[11]:


with open('saida.txt', 'w') as f:
    for idx in range(5):
        print('{0:>2s}{1:>8s}{2:>6s}'.format(str(idx), str(idx**10), str(10**idx)))
        f.write('{0:>2s}{1:>8s}{2:>6s}\n'.format(str(idx), str(idx**10), str(10**idx)))


# ## Exercício exemplificativo
# 
# (adaptado de [Introduction to Programming in the Biological Sciences Bootcamp - Lesson 11](https://justinbois.github.io/bootcamp/2020/lessons/l11_file_io.html), (c)2020 Justin Bois, CC-BY 4.0)
# 
# 

# Considere o ficheiro 10LG.pdb, de [Protein Databank](http://www.rcsb.org/pdb/explore/explore.do?structureId=1olg) com informação sobre a proteína [p53](https://pt.wikipedia.org/wiki/P53).
# 
# ### Extrair informação
# 
# Queremos isolar os registos ATOM da primeira cadeia e escrevê-los para um novo ficheiro.
# 
# Consultando a [especificação do formato PDB](http://www.wwpdb.org/documentation/file-format-content/format33/sect9.html#ATOM), notamos que a coluna 22 nas linhas *ATOM* correspondem ao *ID* da cadeia (que corresponderá à posição 21 da *string* em Python).
# 
# Podemos usar mais que um ficheiro no bloco *with* e usamos um ficheiro para a leitura e outro para a escrita.
# 

# In[12]:


with open('1OLG.pdb', 'r') as f_in, open('atoms_chain_A.txt', 'w') as f_out:
    # Put the ATOM lines from chain A in new file
    for line in f_in:
        if len(line) > 21 and line[:4] == 'ATOM' and line[21] == 'A':
            f_out.write(line)


# Vejamos as primeiras 10 linhas.

# In[13]:


with open('atoms_chain_A.txt') as f:
    for i, line in enumerate(f):
        print(line)
        if i >= 9:
            break


# ## Exercícios
# 
# Quantos elementos diferentes existem nesta cadeia?
# 
# Que elementos são?
# 
# Quantos átomos de cada elemento existem?
# 
