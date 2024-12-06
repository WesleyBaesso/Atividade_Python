"""
Faça um programa para ler e imprimir uma matriz 2 × 4 de números inteiros.
"""
matriz = [[0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input('Digite numero: '))
print(matriz)
