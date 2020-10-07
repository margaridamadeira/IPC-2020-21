# Breve apresentação de Python

## O IPython como interpretador de comandos

O ambiente IPython, simples e interactivo, é extremamente conveniente para a aprendizagem da programação em Python, pois permite a elaboração de pequenos programas e sua experimentação. 

Na maioria dos tutoriais, a primeira proposta de utilização do Python é como [calculadora](https://docs.python.org/3/tutorial/introduction.html) simples. 

Isto porque o Python disponibiliza à partida, para além de algumas funcionalidades básicas, várias operações numéricas que podemos utilizar:

> `+` (adição)

> `-` (subtração)

> `*` (multiplicação)

> `/` (divisão)

> `**` (exponenciação)

> `//` (divisão inteira)

> `%` (resto da divisão inteira)

A utilização das operações de adição, subtração, multiplicação e divisão é muito simples.
O único cuidado que temos que ter é lembrarmo-nos da prioridade das operações e usar parenteses se for caso disso.
Vejamos alguns exemplos.

5+4*2

(5+4)*2

A exponenciação é usada para calcular potências.

2**3 

5**2

A divisão inteira e resto da divisão inteira merece alguma atenção. 
Na divisão *normal*, teriamos

7/2

Na divisão inteira, o resultado é um número inteiro e poderá haver resto

7//2

7%2

Existem funções, disponíveis em Python, que iremos conhecendo aos poucos. 
Tente determinar o resultado antes de executar a célula.

> abs(-1)*max(1, 2, 3) + min(4, 5, 6)

Para executar a célUla abaixo, remova o carater '#' que indica um comentário.

# abs(-1)*max(1, 2, 3) + min(4, 5, 6)

Pode consultar a documentação, embora a forma exata possa variar consoante a ferramenta que está a usar (Spyder ou Jupyter). E frequentemente, há mais de uma maneira de obter essa documentação. Por exemplo,

?abs

abs?

help(abs)

## Uso de bibliotecas

É de notar que existem numerosas e diversas bibliotecas com extensões à linguagem básica, que servem os mais diversos fins. Há bibliotecas que dão suporte a mecanismos de cálculo e visualização gráfica que poderão ser bastante úteis. 

Nesta unidade curricular iremos por vezes usar alguns desses mecanismos. Iniciamos com a programação em Python e avançamos depois para a utilização das bibliotecas. 

Um exemplo é *Math*.

from math import *

pi

cos(pi)

> *Sugestão*: Crie uma nova célula antes de importar *math* e tente obter o valor de $ \pi $, ou o $ cos(2\pi) $. A execução da célula vai falhar. Explique porquê.

log(e**5)

log2(1024)-log10(1000)



Outro exemplo do que usaremos é *Matplotlib*.

?matplotlib

No futuro, para se trabalhar com vetores e matrizes, poderíamos usar *NumPy* ou outras alternativas.

?numpy

A instrução precedida de % é aquilo a que na terminologia do IPython se denomina *magic*, uma extensão à linguagem Python que facilita a interacção com o sistema. Introduziremos, quando necessário, outras magias do IPython.

Neste caso e apenas para efeitos de demonstração, ativamos o Pylab. No futuro, em vez de trazermos a caixa de ferramentas toda, escolhemos a ferramenta que precisamos.

%pylab inline

E já temos mais funcionalidades disponíveis, por exemplo, para gerar gráficos.


### Geração de gráficos
A representação gráfica é uma parte importante e, felizmente, não é complicada.
Vejamos como faríamos para representar a função $f(x) = x² $ quando o conjunto de partida é $ \{0, 1, 2, 3, 4, 5 \} $

x = arange(6) # 


# O que está afinal no eixo do x
print (x)

plot(x, x**2)

E como faríamos para representar as funções seno e coseno no mesmo gráfico?

x=arange(0,10,0.1); 

plot(x, sin(x), 'r', x, 1+cos(x),'b')

Há outros tipos de gráficos para além do *plot*, e quando chegarmos lá veremos melhor. Uma *espreitadela* rápida ao que seremos capazes de fazer.

?pie


pie([45,30,10,10,4,1], labels=[45,30,10,19,4,1],frame=0)

from matplotlib.pyplot import plot as dataplot 

?dataplot

dataplot([1,2,3,4,5])

dataplot([1,-2,3,-4,5],"ro-")

dataplot([1,5,3,4,2,6],"g*--")

dataplot([1,2,3,4,5], "go-", label="line 1", linewidth=2)
dataplot([2,9,0,4], "rs",  label="line 2")
axis([-2, 8, -2, 10])
legend()

## Em resumo

* O IPython é um ambiente de programação interactivo muito simples, apropriado à experimentação rápida de programas em Python, e portanto adequado à aprendizagem da programação
* Munido das extensões adequadas o ambiente IPython pode ser utilizado como poderosa ferramenta de cálculo numérico e simbólico, e de visualização gráfica, extremamente útil em aplicações científicas, matemática e engenharia
* A biblioteca Matplotlib fornece um ambiente de computação essencialmente equivalente ao popular sistema proprietário MATLAB, também muito usado em aplicações científicas. 