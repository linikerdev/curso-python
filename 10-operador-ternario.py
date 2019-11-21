
esta_chovendo = False
esta_sol = not esta_chovendo
# opção 1
op1 = 'Hoje estou com as roupas ' + ('secas', 'molhadas')[esta_chovendo]
print(op1)

print('--------------------')

# opção 2
op2 = 'Hoje estou com as roupas ' + ('molhadas' if esta_sol else 'secas')
print(op2)