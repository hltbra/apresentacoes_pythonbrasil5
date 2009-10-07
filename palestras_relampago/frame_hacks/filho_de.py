'''
    >>> class Pessoa(object):
    ...     filho_de = None
    ...     filhos = []
    ...

    >>> class Joao(Pessoa):
    ...    pass

    >>> Joao.filhos
    []

    >>> class Jose(Pessoa):
    ...     filho_de('Joao')

    >>> Joao.filhos
    ['Jose']

'''
import sys


def filho_de(pai):
    contexto_do_filho = sys._getframe(1)
    nome_do_filho = contexto_do_filho.f_code.co_name
    classe_do_pai = contexto_do_filho.f_globals[pai]
    classe_do_pai.filhos.append(nome_do_filho)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
