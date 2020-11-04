# Lab4

## Objetivos de aprendizagem

Com este guião, exercitaremos:

1. a leitura da consola, vários valores por linha e até ao fim dos dados
1. escrita formatada
1. a utilização de listas



### Tarefa A

Pretende-se a ordenação crescente de sequências de números. Não sabemos quantas sequências temos nem quantos elementos por sequência. Para cada linha lida, ordenamos os elementos e apresentamos a sequência ordenada.

Vamos então preparar um programa que receba da consola, até ao fim dos dados, linhas com sequências de inteiros e, para cada linha, apresente a sequência por ordem crescente, com dada elemento separado por um espaço. 

Porque queremos um programa "completo", comece pelas linhas que indicam ao Python que deve começar pela função de teste, ou seja

```
if __name__ == "__main__":
    test_ordem_crescente()
```
Em seguida, escrevemos a função de  *test_ordem_crescente*, responsável pela leitura, chamada da função *ordem_crescente* e apresentação dos resultados. Mantenha a função *ordem_crescente* vazia, de forma a poder verificar se a leitura e escrita estão a funcionar bem. 

Vamos começar por passar cada linha para uma lista. E para verificar, preparamos uma função *mostra_sequência_separada_por_espaços* (para que não haja dúvidas sobre o que a função faz) que apresente a lista. Note que deve haver um espaço entre cada dois elementos, mas não pode haver um espaço antes do primeiro elemento en um espaço depois do último.

Prepare uma função *ordem_crescente* para a ordenação crescente dos elementos lidos em cada linha.


#### Caso de teste 

**Input**

```
2
9
1
8
6
```

**Output**

```
1
2
6
8
9
```

### Tarefa B

Fizemos uma série de experiências e a duração foi cronometrada de forma automática, em segundos. Queremos saber a duração de cada experiência em horas, minutos e segundos.

Prepare um programa em Python que leia uma sequência de números, um por linha e, para cada número lido, apresente esse valor no formato HH:MM:SS.

#### Casos de teste 

**Input 1**

```

```

**Output 1**

```

```

**Input 2**

```

```

**Output 2**

```

```

Submeta no problema B do Lab4.

### Tarefa C

Atualizamos os equipamentos e agora os tempos das experiências são apresentados em horas, minutos e segundos. Queremos saber o tempo total gasto nas experiências, em dias, horas, minutos e segundos.

Podíamos converter os tempos para segundos e depois de termos um total, converter então para o formato desejado. Mas a nossa conversão não considerava a possibilidade de traduzir valores de horas superiores a 24 em dias e horas. Assim, vamos lendo a duração das experiências e atualizandoo tempo total.

Prepare um programa que leia os tempos da consola, um por linha, até ao fim dos dados e apresente o tempo total em dias, horas, minutos e segundos. Cada linha contém uma string com o formato *HH:MM:SS* em que *HH* correponde às horas, *MM* corresponde aos minutos e *SS* aos segundos. O tempo total, que deve ser apresentado num única linha, deverá respeitar o formato "nn:xx:yy:zz" (sem as aspas), em que *nn*, *xx*, *yy* e *zz* correspondem ao valores de dias, horas, minutos e segundos, respetivamente. Note que deve usar dois dígitos para cada valor.



#### Casos de teste 

**Input 1**

```


```

**Output 1**

```

```

**Input 2**

```

```

**Output 2**

```

```

Submeta no problema C do Lab4.

### Tarefa D

Estamos a registar o trabalho e verificámos que muitas vezes há erros na introdução das datas. É preciso então validar as datas introduzidas. 

Usamos o [formato padrão](https://pt.wikipedia.org/wiki/ISO_8601), *YYYY-MM-DD* em que *YYYY* representa o ano, *MM* representa o mês e *DD* o dia. Para simplificar, vamos considerar o [calendário gregoriano](https://pt.wikipedia.org/wiki/Ano_bissexto), ou seja, que temos datas a partir de 1582.

Relembremos agora as regras para as datas. Os meses são 12, isso é simples. Os dias variam, como sabemos do ditado popular: "Trinta dias tem novembro, abril, junho e setembro, vinte e oito terá um e os mais têm trinta e um". Fevereiro terá 28 dias, ou, num ano bissexto, 29. Um ano bissexto é divisível por quatro mas, se for um ano secular só será bissexto se for divisível por 400. E um ano secular é um ano divisĩvel por 100.

Prepare um programa que leia as datas da consola, uma por linha, até ao fim dos dados. Por cada linha lida, o seu programa deve repetir a data lida, indicando se é válida ou não. Cada linha do input conterá *YYYY-MM-DD* em que *YYYY*, *MM* e *DD* representam ano, mês e dia, respetivamente. 


#### Casos de teste


 # Tarefa E 
 
 Dizemos que um número natural *n* é palíndromo se
        o 1º algarismo de n é igual ao seu último algarismo,
        o 2º algarismo de n é igual ao penúltimo algarismo,
        e assim sucessivamente.


        Exemplos:

                567765 e 32423 são palíndromos.

                567675 não é palíndromo.

Dado um número natural   n > 10 , verificar se n é um palíndromo.

Submeta no problema E do Lab4.
