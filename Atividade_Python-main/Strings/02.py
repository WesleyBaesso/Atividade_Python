nome = str(input('dig o nome: '))
cont = 0
space = 0
con = nome.lower()  
for i in range(len(con)):
    if con[i] == 'a' or con[i] == 'e' or con[i] == 'i' or con[i] == 'o' or con[i] == 'u':
        cont += 1
    if con[i] == ' ':
        space += 1
print(cont)  
print(space)  
