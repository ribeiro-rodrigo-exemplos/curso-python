lista = []
print(type(lista))
dir(lista)
print(len(lista))
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]

print(lista.index('Guilherme'))
# lista.index(42) -> erro
print(lista[2])

print(1 in lista)
print('Pedro' not in lista)
print(lista[0])
print(lista[4])
print(lista[-1])  # -> pega o ultimo elemento da lista
print(lista[-5])

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']

print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])
del lista[2]

print(lista)
del lista[1:]
print(lista)
