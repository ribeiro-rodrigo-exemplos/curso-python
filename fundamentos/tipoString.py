nome = 'Saulo Pedro'
print(nome)
print(nome[0])

# nome[0] = 'P' -> não funciona

print("Dias D'Avila" == 'Dias D\'Avila')
texto = 'Texto entre apostrófos pode ter "aspas"'
print(texto)
print("Teste \" funciona!")

doc = """
Texto com multiplas
    ... linhas
"""

doc2 = '''
    Também é possível 
    criar com aspas simples
'''

print(doc)
print("Texto com multiplas\n\t...linhas")
print(doc2)

nome = 'Ana Paula'
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[2:5])

numeros = '123456789'

print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])
print(nome[::-1])

frase = 'Python é uma linguagem excelente'

print('py' not in frase)
print('ing' in frase)
print(len(frase))
print(frase.lower())
print('py' in frase.lower())
print(frase.upper())
frase = frase.upper()
print(frase.split())
print(frase.split('E'))
dir(str)

a = '123'
b = 'de Oliveira 4'

print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))
dir(str)
print(len(a))
print(a.__len__())
print('1' in a)
print(a.__contains__('1'))
