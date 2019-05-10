from string import Template

nome, idade = 'Ana', 30.9875

print('Nome: %s Idade: %.2f %r %r' % (nome, idade, True, False))  # mais antiga

# recomendando em python < 3.6
print('Nome: {0} Idade: {1}'.format(nome, idade))

print(f'Nome: {nome} Idade: {idade} {2 ** 8 + 1}')  # apartir do python 3.6

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
