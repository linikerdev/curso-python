list = [ 1, 2, 3, 'Ana', 'Carla']

print(2 in list)


print('Ana' not in list)


x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2]
lista_b = lista_a
lista_c = [1, 2]
print('-----1-----')
print(lista_a is lista_b)
print('-----2-----')
print(lista_b is lista_c)
print('-----3-----')
print(lista_a is lista_c)