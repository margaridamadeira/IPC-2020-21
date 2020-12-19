# -*- coding: utf-8 -*-

"""
Solução recursiva para o problema what 
(originalmente TIUP 2008)
(c) Margarida Madeira e Moura, 2020
"""

import doctest
from what import rna3

def traduzir(seq: str, tabela: dict) -> str :
    """ Traduz os codões de seq pelos aminoácidos conforme indicado na tabela.
    Usa o dicionário rna3 do módulo what

    Exemplos:
    >>> traduzir('AUG', rna3)
    'M'
    >>> traduzir('CUU', rna3)
    'L'
    >>> traduzir('AUGCAAUAGGU', rna3)
    'MQ*'
    """
    resultado = ''
    for item in range(0,len(seq)-2,3):
        # print(item)
        resultado += tabela[seq[item:item+3]]

    return resultado

def deteta_inicio(seq: str) -> int:
    """Devolve a posição do codão de abertura de uma sequência.

    Exemplos:
    >>> deteta_inicio('AUG')
    0
    >>> deteta_inicio('UUAUG')
    2
    """
    try:
        result = seq.index('AUG')
    except ValueError:
        result = -1 # Mesmo comportamento que o find

    return result

def deteta_fim(seq: str) -> int:
    """Devolve a posição do codão de fecho de uma sequência aberta ou, 
    se não existir fecho, devolve a dimensão da sequência.

    Exemplos:
    >>> deteta_fim('AUG')
    3
    >>> deteta_fim('AUGCAAUAGGU')
    6
    >>> deteta_fim('AUGAACUAAU')
    6
    """
    fecho = ['UAG','UGA','UAA'] 

    resultado = len(seq)
    
    for item in range(0, len(seq)-2, 3):
        if seq[item:item+3] in fecho:
            resultado = item
            break
    
    return resultado

def L6(seq: str) -> str:
    """ Resolve o exercício do Lab 6 """
    resultado = ''

    # Tem que existir pelo menos um codão 
    if len(seq) >= 3:
        inicio = deteta_inicio(seq)
        fim = inicio + deteta_fim(seq[inicio:])
        # Tem que existir a abertura de uma sequência
        if inicio >= 0:
            resultado += traduzir(seq[inicio:fim+3], rna3) + L6(seq[fim+3:])
    return resultado


def test_l6():
    teste = input()
    print(L6(teste))


if __name__ == '__main__':
    doctest.testmod()
    test_l6()
