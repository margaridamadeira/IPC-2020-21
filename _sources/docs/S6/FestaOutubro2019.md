# Festa de outubro de 2019

Esta foi a primeira festa do ano letivo de 2019-2020.


Reúna todos os seus materiais para consulta durante a festa e os seus programas anteriores (e os que estão no Mooshak pode sempre ir lá buscá-los). 
Prepare uma pasta para cada problema que vai abordar, e a versão inicial da sua resolução.
E idealmente, reserve três horas e tente resolver os exercícios da festa.

## Objetivo de aprendizagem

Com este este exercício, exercitaremos uma festa de programação.

## A qualidade da água


```{figure} ./waterfall.png
---
height: 300px
name: cascata
---
Imagem de [Sergio Palao](http://www.palao.es/) (CC)BY-NC-SA
```

Fazemos vários tipos de análises, como por exemplo, qualidade da água ou existência de químicos em produtos alimentares. Para a produção de relatórios, queremos determinar a conformidade dos produtos analisados, sabendo os valores de referência e tolerância admissível. Um produto analisado está conforme se a variação percentual acumulada não exceder a tolerância admissível. A variação percentual acumulada, como o nome indica, é a soma das diferenças percentuais.


Por exemplo, se a referência de um parâmetro for 200 e o resultado for 190 ou 210, a variação percentual em ambos os casos não excedeu $5\%$.

Considere então que queremos verificar se há desvio superior a $5\%$ quando os valores de referência são $150.2$ e $2.5$.
Se os valores das análises indicassem $167.4$ e $2.5$, o produto não estaria conforme, pois o primeiro valor tem uma variação superior a $5\%$. Se os valores das análises fossem $150.2$ e $2.8$, ou $157.2$ e $2.55$ o produto também não estaria conforme.

Acontece que a tolerância e os valores de referência variam consoante o tipo de análise.

As duas primeiras linhas que o programa receberá contêm a tolerância e os valores de referência. Em cada uma das linhas seguintes apresentam-se  os resultados da análise a um produto. Se os resultados da análise a um produto estiverem dentro da tolerância admitida, escreva "OK" (sem as aspas); caso contrário, escreva "Fail" (sem as aspas).

Prepare um programa (incluindo main e função de teste) que verifique a conformidade dos resultados das análises e submeta na tarefa **A** do concurso IPC_F1_2019.

**Caso de teste**

**Input**

```
0.05
150.2 2.5
167.4 2.5
150.2 2.8
157.2 2.55
150.2 2.55
157.2 2.5
```

**Output**

```
Fail
Fail
Fail
OK
OK
```

## Migração


```{figure} ./flocks.png
---
height: 300px
name: aves
---
Imagem de [Sergio Palao](http://www.palao.es/) (CC)BY-NC-SA
```

Queremos avaliar, de forma muito geral, o padrão migratório de algumas aves que nidificam na Ria Formosa. Dispomos de anilhas que, colocadas numa pata de uma ave, regista a localização. Essas anilhas já são inteligentes e a informação de percursos curtos não é considerada.
Quando, após um ano, se recolhem as anilhas, obtêm-se as coordenadas (latitude e longitude) da origem e destino de cada etapa. A latitude, Norte ou Sul, indica a distância ao equador; a longitude, Este ou Oeste, indica a distância ao meridiano primário. A latitude e longitude são indicadas em graus e minutos e incluem uma letra que indica o hemisfério. Assumimos que cada minuto de grau corresponde a <del>1852</del> 1 853 metros e sabemos que cada grau tem 60 minutos.

Para cada ave, pretendemos saber a distância total percorrida e a distância da maior etapa.

O programa lerá tantas linhas quantas as etapas registadas. Em cada linha teremos duas coordenadas, cada uma com seis partículas, a saber: graus de latitude, minutos de latitude, hemisfério (N ou S), graus de longitude, minutos de longitude e hemisfério (E ou W). Graus e minutos são números inteiros e o hemisfério é uma letra.

Ao terminar a leitura, o programa escreverá na mesma linha dois valores reais em notação científica separados pelo carater espaço que correspondem à distância total e à percorrida e à distância da maior etapa.

Prepare um programa (incluindo main e função de teste) que verifique a conformidade dos resultados das análises e submeta na tarefa **B** do concurso IPC_F1_2019.

**Caso de teste**

**Input 1**

```
00 00 N 00 00 E 37 01 N 07 49 W
```

**Output 1**

```
4.206e+06 4.206e+06
```

**Input 2**

```
37 01 N 07 49 W 38 43 N 09 08 W
38 43 N 09 08 W 41 09 N 08 37 W
41 09 N 08 37 W 37 01 N 07 49 W
```

**Output 2**

```
9.837e+05 4.681e+05
```

## Trabalho e mais trabalho

Estavamos a testar formas de eliminar um fungo das batatas quando se notou que tínhamos conseguido eliminar completamente um outro fungo. Acontece que o nosso preparado já está muito complexo e agora, para isolar os elementos responsáveis, vou ter que refazer as experiências.

De forma a podermos distribuir o trabalho e não deixarmos nenhuma combinação por testar, preciso de um programa que me crie todas as variações. É claro, não quero repetir trabalho. Assim, numero cada substância usada e preciso de obter todas as possíveis variações, ou seja, os subconjuntos do conjunto inicial com todas as substâncias.

Por exemplo, se tiver lido para a minha lista inicial os números $1$ e $2$, terei os subconjuntos

[], [1], [2], [1, 2]

Se tiver na lista inicial os números $4$, $7$ e $11$, terei os subconjuntos

[], [4], [7], [4, 7], [11], [4, 11], [7, 11], [4, 7, 11]

O seu programa deverá ler o número de elementos e essa quantidade de números inteiros. Deverá apresentar, numa única linha, os subconjuntos por ordem crescente. Note que se pretende a lista com as sublistas.

Prepare um programa (incluindo main e função de teste) que determine os divisores de um número e submeta na tarefa C do concurso IPC_F1_2019.

**Caso de teste**

**Input 1**

```
2
1
2
```

**Output 1**

```
[[], [1], [2], [1, 2]]
```

**Input 2**

```
3
4
7
11
```

**Output 2**

```
[[], [4], [7], [4, 7], [11], [4, 11], [7, 11], [4, 7, 11]]
```
