import random

''' numeros = [0, 1, 2, 3, 4, 5 ,6 ,7 ,8 ,9]
print(numeros, "\n")

for i in range(0, len(numeros)):
    aleatorio = random.randint(0, len(numeros) - 1)
    numeros.pop(aleatorio)
    print(numeros)
     '''
    
    
cuadros_y = [0, 1, 2, 3]
cuadros_x = [0, 1, 2, 3, 4, 5]
x = 60
y = 35 

cuadros_utilizados = []
for i in range(0, len(cuadros_y)*len(cuadros_x)):
    #self.ventana.blit(imagen, (720, 250))
    while True:
        aleatorio_y = random.randint(0, len(cuadros_y) - 1)
        aleatorio_x = random.randint(0, len(cuadros_x) - 1)
        if [aleatorio_y, aleatorio_x] in cuadros_utilizados:
            a = [aleatorio_y, aleatorio_x]
            print(a, end=" ") 
        else:
            print("aaa")
            break
    cuadros_utilizados.append([aleatorio_y, aleatorio_x])
    #print(cuadros_utilizados)