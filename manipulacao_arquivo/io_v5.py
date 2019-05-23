#!/usr/bin/python3


with open('pessoas.csv') as arquivo:

    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip('\n').split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')
