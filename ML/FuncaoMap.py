# FUNCAO MAP()
kmh = [40, 50, 56, 64, 73, 79, 85, 96, 100, 120]

mph = list(map(lambda x: x/1.61, kmh))
print(mph)

# FUCAO LIST COMPREHENSION

mph2 = [x/1.61 for x in kmh]
print(mph)

caracteres = [i for i in "Machine Learning"]
print(caracteres)
