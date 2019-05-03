
teste = 'blabla'

pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': [
    'Inglês', 'Português'], teste: 'testando...'}

print(type(pessoa))
print(len(pessoa))
print(pessoa)

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][0])
# print(pessoa['tags']) -> erro
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))

pessoa = {'nome': 'Prof(a). Alberto', 'idade': 43, 'cursos': [
    'React', 'Python']}

pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)

print(pessoa.pop('idade'))
print(pessoa)

pessoa.update({'idade': 40, 'Sexo': 'M'})

print(pessoa)

del pessoa['cursos']

print(pessoa)

pessoa.clear()
print(pessoa)
