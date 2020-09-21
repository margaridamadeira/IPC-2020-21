# Breve apresentação de Python

## O IPyhton como interpretador de comandos

O ambiente IPython, simples e interactivo, é extremamente conveniente para a aprendizagem da programação em Python, pois permite a elaboração de pequenos programas e sua experimentação. 

Na maioria dos tutoriais, a primeira proposta de utilização do Python é como [calculadora](https://docs.python.org/3/tutorial/introduction.html) simples. 

Isto porque o Python disponibiliza à partida, para além de algumas funcionalidades básicas, várias operações numéricas que podemos utilizar:
- `+` (adição),
- `-` (subtracção),
- `*` (multiplicação), 
- `/` (divisão),
- `**` (exponenciação),
- `//` (divisão inteira), 
- `%` (resto da divisão inteira). 

Vejamos alguns exemplos.

1+1-2

(2*3)%5

7/3

7//3

10**3

1/3+1/2

Existem funções, disponíveis em Python, que iremos conhecendo aos poucos.

abs(-1)*max(1,2,3)+min(1,2,3)+round(2.6)

É de notar que existem numerosas e diversas bibliotecas com extensões à linguagem básica, que servem os mais diversos fins. Há bibliotecas que dão suporte a mecanismos de cálculo e visualização gráfica que poderão ser bastante úteis, nomeadamente: Scipy e Matplotlib, ambas incluindo Numpy, que por sua vez inclui Math, e ainda Sympy, cuja utilização ilustramos de seguida.

Nesta unidade curricular iremos por vezes usar alguns desses mecanismos. Iniciamos com a programação em Python e avançamos depois para a utilização das bibliotecas. 

As extensões Numpy e Matplotlib estão incluídas na extensão Pylab, que pode ser carregada como se mostra abaixo. A instrução precedida de % é aquilo a que na terminologia do IPython se denomina $\textrm{magic}$, uma extensão à linguagem Python que facilita a interacção com o sistema. Introduziremos, quando necessário, outras magias do IPython.


%pylab inline

?pylab

Avaliando a expressão acima e percorrendo a informação na janela que se abre podemos identificar as funcionalidades que passamos a ter disponíveis, algumas das quais ilustraremos de seguida. Poderá ser útil averiguar também os conteúdos de Numpy e Matplotlib, bem como da extensão Math que é incluída conjuntamente.

?pi

pi

cos(2*pi)

sin(pi/6)

sin(2*pi/3)-sqrt(3)/2

log(e**5)

log2(1024)-log10(1000)

Veremos mais tarde como fazer para trabalhar com precisão arbitrária, ou mesmo com representações simbólicas, exactas mas menos eficientes.

### Vetores e matrizes

Vetores e matrizes são designações usadas em matemática e, de forma simplificada, correspondem a uma forma de organizar coleções de números.

A manipulação numérica de vectores e matrizes é disponibilizada directamente pela extensão Pylab. Veremos isto mais tarde do ponto de vista da utilização na programação. O significado e importância de operações matriciais como produtos, inversas, determinantes ou valores próprios é objecto de estudo da disciplina de Álgebra Linear.

### Números complexos

complex(1,1)

conjugate(1+1j)

real(complex(1,-1))

imag(complex(1,-1))

abs(1+1j)

### Geração de gráficos
A representação gráfica é uma parte importante e, felizmente, não é complicada.
Vejamos como faríamos para representar a função $f(x) = x² + 1$ no intervalo $[-5,5]$.

x=arange(-5,6,0.1)


# O que está afinal no eixo do x
print (x)

plot(x, x**2+1)

E como faríamos para representar as funções seno e coseno no mesmo gráfico?

x=arange(0,10,0.1); 

plot(x, sin(x), 'r', x, 1+cos(x),'k')

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
* A extensão Pylab fornece um ambiente de computação essencialmente equivalente ao popular sistema proprietário MATLAB, também muito usado em aplicações científicas. 