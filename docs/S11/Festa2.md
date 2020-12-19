# Festa de Programação

**Introdução à programação científica - Bioengenharia**

**18 de dezembro de 2020, das 10h às 13h**

<hr> 

## Informação sobre a Festa de Programação

### Regras

É permitida a consulta aos materiais e recursos da unidade curricular, acessíveis pela Tutoria Eletrónica, bem como à documentação em linha do Python no site [python.org](https://docs.python.org/pt-br/3.8/).

É permitida a consulta dos programas anteriormente feitos pelo próprio(a) bem como das anteriores submissões ao mooshak.

Foi recomendado que trouxessem já programas começados e com algumas variantes de leitura de dados e escrita de resultados; podem e devem usá-los.

É ainda permitido a breve troca de impressões com os colegas, sobre os problemas da Festa, desde que tal não perturbe o ambiente dos demais colegas. E, como nas aulas práticas, pode também pedir ajuda à professora.

_Não_ é permitido a consulta ou partilha de código de colegas e _não_ é permitida qualquer ajuda exterior ou consulta de outros locais não autorizados. 

### Avaliação da Festa

Esta Festa de Programação tem três tarefas e a duração máxima de três horas.
Cada tarefa submetida durante a festa no concurso IPC_F2, aceite e validada vale 20 pontos.

Note que ao ser pedido "um programa em Python" isso significa escrever a função de teste chamada se o script for o *main* e a função de teste fará a chamada à função (ou funções) de resolução do problema. Ou seja, formando um programa completo como temos vindo a fazer nos exercícios e tarefas das aulas práticas. 

A validação, feita pela professora, consiste na apresentação da solução pelo aluno. Submissões que não cumpram os requisitos técnicos ou cuja qualidade seja muito baixa serão invalidadas. As validações poderão ser feitas durante a Festa ou durante as aulas da próxima semana.

### Após a Festa

Os mesmos problemas estarão disponíveis após a Festa, durante a primeira semana após a pausa letiva, no concurso IPC_F2_C. A submissão de cada problema iniciado na Festa, aceite no mooshak e validado, vale 8 pontos.


<div style="page-break-after: always"></div>

## Produtos

```{figure} ./reagentes-quimicos.jpg
---
height: 300px
name: Reagentes
---
```

Quero organizar o stock do laboratório e vou usar o código universal de produtos.

O código universal de produtos prevê números com 12 dígitos numéricos e o dígito da direita é o dígito de controlo. Formalmente, um número de produto é correto sse

$$ (3 x_1 + x_2 + 3 x_3 + x_4 + 3 x_5 + x_6 + 3 x_7 + x_8 + \\ 3 x_9  + x_{10} + 3 x_{11} + x_{12}) \equiv 0 \pmod {10} $$ 
em  que $\equiv \pmod{10}$ indica que a expressão à esquerda é congruente a $0$ módulo 10.

Assim, se quiser obter manualmente o dígito de controlo para o código "03600029145x", farei:

+ a soma de algarismo sim, algarismo não, multiplicando o resultado por 3
+ a soma dos restantes algarismos (obtendo, neste caso, 58)
+ determino o resto da divisão por 10 (que neste caso é 8)
+ Se o resto fosse zero, o dígito de controlo seria 0; neste caso o dígito de controlo será $10-8$, portanto 2.

Preciso de um programa para determinar o dígito de controlo.

### Tarefa

Prepare um programa em Python completando que determine o dígito de controlo de um código universal de produto. O programa recebe, da consola, uma única linha contendo 11 carateres numéricos e a letra 'x' e devolverá o dígito de controlo.

### Exemplos

**Input 1**

```
03600029145x
```

**Output 1**

```
2
```

**Input 2**

```
03600024145x
```

**Output 2**

```
7
```

**Input 3**

```
01234567895x
```

**Output 3**

```
0
```

Submeta no problema A do concurso IPC_F2.

## Eficácia

```{figure} ./eficacia.jpeg
---
height: 300px
name: Eficácia
---
```

Pretende-se proceder à avaliação de uma experiência. Cada um de *n* produtos é ensaiado num número indeterminado de amostras. 

A eficácia de um produto numa amostra é marcada com *1* se o produto é eficaz ou *0* se o produto não é eficaz. Para já, considera-se a eficácia do produto como a média aritmética  dos resultados desse produto nas diferentes amostras.

Pretendo uma listagem ordenada dos produtos que têm uma eficácia superior a um valor *v*.

### Tarefa

Prepare um programa em Python para produzir a listagem pretendida. 

O seu programa deve ler, numa primeira linha, um número inteiro e um número real separados por espaços, números esses que correspondem ao número de produtos *n* e ao patamar de eficiência *v*, respetivamente.
As *n* linhas seguintes contêm a informação de cada produto sendo que em cada linha surgem, separados por vírgulas, o nome do produto e a eficácia desse produto em cada uma das amostras.

O seu programa deve produzir uma listagem dos produtos onde se verificou uma eficácia superior ou igual ao patamar *v*. Nessa listagem, os produtos devem surgir por ordem alfabética e apenas um por linha.
Caso não existam produtos a apresentar o seu programa deverá apresentar a mensagem "Não há produtos com a eficácia pretendida." (sem as aspas).

**Requisito técnico**: deve usar, pelo menos, um dicionário.

#### Exemplos

**Input 1**

```
3 0.3
Silicato de sódio,1,1,0,0,0
Oxido de chumbo,0,0,1,0,1
Acetato de chumbo,0,1,0,1,0
```

**Output 1**

```
Acetato de chumbo
Oxido de chumbo
Silicato de sódio
```

**Input 2**

```
5 0.5
Carbonato de bário,0,0,1
Violeta de genciana,1,0,0
Cloreto de cálcio,0,1,0
Acetona,1,1,0
Azul de metileno,0,1,1
```

**Output 2**

```
Acetona
Azul de metileno
```

**Input 3**

```
5 0.7
Carbonato de bário,0,0,1
Violeta de genciana,1,0,0
Cloreto de cálcio,0,1,0
Acetona,1,1,0
Azul de metileno,0,1,1
```

**Output 3**

```
Não há produtos com a eficácia pretendida.
```

Submeta no problema B do concurso IPC_F2.

## Maior subida de temperatura

```{figure} ./subida-temperatura.jpeg
---
height: 300px
name: Subida de temperatura
---
```

Porque muitas das nossas experiências que funcionaram de forma anómala dependem da temperatura, passámos então a recolher a temperatura no laboratório de hora a hora.
Houve alturas em que se verificou uma sequência crescente, ou seja, um conjunto de medidas T em que $t_n < t_{n+1}$.
Para analisarmos a evolução das temperaturas, queremos identificar a maior amplitude das sequências crescentes de temperatura.

### Tarefa

Dada uma série de medidas de temperatura obtidas durante a realização de uma experiência, pretende-se identificar qual a maior amplitude das sequências crescentes de temperatura. 

O seu programa deve ler, da consola, uma única linha contendo números reais separados por espaços.

O programa deve apresentar um número real com 4 casas decimais que corresponde à maior amplitude das sequências crescentes.


#### Exemplo

**Input 1**

```
26.79 26.76 26.62 26.12 25.47 30.12 30.18 30.65 32.07 32.13 33.17 32.83 32.89 35.47 35.91 37.34 37.62 36.89
```

**Output 1**

```
7.7000
```

**Input 2**

```
0

```

**Output 2**

```
0.0000
```

**Input 3**

```
0.0 27.0
```

**Output 3**

```
27.0000
```

**Input 4**

```
27.0 0.0
```

**Output 4**

```
0.0000
```

**Input 5**

```
12 -5 -4 -3 -2 -1 22 27 0 5 6 7
```

**Output 5**

```
32.0000
```

**Input 6**

```
12 5 6 7 -5 -4 -3 -2 -1 22 27 0
```

**Output 6**

```
32.0000
```

Submeta no problema C do concurso IPC_F2.
