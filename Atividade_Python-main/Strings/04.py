n = int(input('dig o codigo: '))
resulta = []
n_str = str(n) 
for i in range(len(n_str)): 
    if n_str[i] == '1':  
        resulta.append('um') 
    elif n_str[i] == '2':  
        resulta.append('dois')
    elif n_str[i] == '3':  
        resulta.append('três') 
    elif n_str[i] == '4':  
        resulta.append('quatro')  
    elif n_str[i] == '5':  
        resulta.append('cinco') 
    elif n_str[i] == '6':  
        resulta.append('seis') 
    elif n_str[i] == '7':  
        resulta.append('sete') 
    elif n_str[i] == '8':  
        resulta.append('oito') 
    elif n_str[i] == '9':  
        resulta.append('nove') 
    else: 
        resulta.append('zero') 
print(resulta)
