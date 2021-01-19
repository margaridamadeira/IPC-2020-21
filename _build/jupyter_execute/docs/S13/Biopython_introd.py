#!/usr/bin/env python
# coding: utf-8

# # Introdução ao Biopython
# 
# [Biopython](https://biopython.org/) facilita o trabalho em biologia computacional usando Python. Biopython disponibiliza um conjunto de ferramentas de entre as quais se destacam as funcionalidades para:
# 
# + manipular, em Python, de ficheiros com formatos específicos da bioinformática como BLAST, FASTA, GenBank e outros;
# + aceder a recursos em linha como NCBI ou ExPASy;
# + efetuar em modo gráfico algumas das operações mais frequentes;
# 
# e documentação sobre o uso dos módulos, que inclui tutorial e receitas.

# ## Instalação
# 
# Usando a distribuição de Python da Anaconda, a instalação do BioPython é conseguida com o comando
# 
#     conda install biopython
#     
# Na imagem abaixo, podemos ver que inicialmente o Biopython não estava instalado. Tendo emitido o comando para instalar, e indicado que pretendemos prosseguir o módulo é instalado. Finalmente, quando importamos o módulo na *prompt* do python, o comando é bem sucedido.
# 
# 
# ![Instalação do módulo Biopython](img/Biopython_instalar.png "Instalação")

# A verificação da versão instalada, consegue-se com 

# In[1]:


import Bio
Bio.__version__


# ## Visão panorâmica
# 
# O [tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html) do Biopython ilustra as funcionalidades com alguns exemplos, que a seguir se transcrevem.
# 
# Um tipo fundamental na bioinformática é a **sequência**. Uma sequência é uma coleção ordenada de letras, tal como surge em vários formatos de ficheiros com dados biológicos.
# 

# In[2]:


from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
my_seq


# In[3]:


print (my_seq)


# Nas sequências, de forma semelhante às strings, as operações de indexação, corte e iteração estão disponíveis.

# In[4]:


my_seq[2]


# In[5]:


my_second_seq = my_seq[0:4]
print(my_second_seq)


# In[6]:


for item in my_second_seq:
    print (item, end=' ')


# In[7]:


# A ajuda em linha  
get_ipython().run_line_magic('pinfo', 'my_seq')


# In[8]:


# Experimentemos os exemplos
# from Bio.Seq import Seq # Já tínhamos importado este módulo
from Bio.Alphabet import IUPAC
my_seq = Seq("MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF",IUPAC.protein)


# In[ ]:


my_seq


# In[ ]:


print (my_seq)


# In[ ]:


my_seq.alphabet


# A sequência inclui alguns métodos que a string não contém. 

# In[ ]:


my_seq = Seq("AGTACACTGGT")
my_seq.alphabet


# In[ ]:


my_seq_complement = my_seq.complement()
my_seq_complement


# In[ ]:


my_seq_rc = my_seq.reverse_complement()
my_seq_rc


# ### Ficheiros FASTA 

# In[ ]:


from Bio import SeqIO
for seq_record in SeqIO.parse("data\ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))


# ### Ficheiros GenBank

# In[ ]:


from Bio import SeqIO
for seq_record in SeqIO.parse("data\ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))


# ## Outros recursos
# ### Rosalind

# [Rosalind](http://rosalind.info/about/) é uma plataforma disponível em linha para a aprendizagem de bioinformática pela resolução de problemas. 
# 
# Na seção [Bioinformatics Armory](http://rosalind.info/problems/list-view/?location=bioinformatics-armory) privilegia-se a resolução de problemas usando ferramentas já disponíveis. O primeiro problema ilustra a utilização de Biopython no separador *Programming Shortcut*.

# In[ ]:


from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
my_seq.count("A")


# Sugere-se a resolução desses exercícios.

# ### Cookbook
# 
# Em [Cookbook Entries](https://biopython.org/wiki/Category%3ACookbook) estão disponíveis vários exemplos que facilitam a familiarização com este módulo.
# 
# 
