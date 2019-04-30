print(True or False)
print(7 != 3 and 2 > 3)

# python não tem xor

print(not True)
print(not False)
print(not 0)
print(not -1)
print(not not -1)
print(not not True)

# Operadores bit a bit

print(True & True)
print(False | False)
print(True ^ True)

# 3 = 11
# 2 = 10
print(3 & 2)
print(3 | 2)
print(3 ^ 2)

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)
