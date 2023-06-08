# Operadores ternários 

esta_chovendo = False

print('Hoje estou com as roupas ' + ('secas.', 'molhadas')[esta_chovendo])
print('Hoje estou com as roupas ' + ('molhada.' if esta_chovendo else 'seca.'))