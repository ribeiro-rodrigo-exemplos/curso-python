#!/usr/bin/python3


def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    resultado = mapear(lambda x: x**2, [2, 3, 4])
    print(list(resultado))
