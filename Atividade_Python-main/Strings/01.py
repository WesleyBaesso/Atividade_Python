n = input('Digite o seu nome: ')
n1 = ''
for i in range(len(n) - 1, -1, -1): 
    n1 += n[i]
n1 = n1.upper()  
print(n1)
