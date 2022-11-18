#Author: Eduardo Sousa
#Email: edu815761@gmail.com

import matplotlib.pyplot as plt
import numpy as np

a = float(input("Digite o primeiro valor do intervalo: "))
b = float(input("Digite o segundo valor do intervalo: "))
c = float(input("Digite o valor de precisão(quanto maior, mais preciso será. máximo:997): "))
pontos = []
valores = []
areas = []
i = 0
j = 0
resultado = 0

#pega valores em X e tranforma em f(X)
def f(i, c) : 
    if (len(valores) == c) :
        return 2
    else:
        #Inserir dentro dos parenteses do append a função a ser calculada
        #pontos[i] equivale a X
        valores.append(pontos[i] ** 2 + 5*pontos[i]+ 4) 
        i = i + 1
        f(i, c)
    return valores


#Encontra a base do retangulos
def base_n(a, b, c):
    base = (b-a)/c
    
    return base


#Encontra os valores medios de cada retangulo
def pontos_m(a, base, c):
    if (len(pontos) == c) :
        return pontos
    else:
        alt = a+(base/2)
        pontos.append(alt)
        pontos_m(a+base, base, c)
         
         
         
#Encontra a area de cada retangulo     
def area_m(base, j):
    if (len(areas) == c) :
        return 2
    else:
        areas.append(valores[j] * base)    
        j = j + 1
        area_m(base, j)
    return areas  
    
     
#Informações para depuração	do codigo
#-------------------------------------
base = base_n(a, b, c)
print(base)

pontos_m(a, base, c)
print(pontos)

f(i, c)
print(valores)

area_m(base, j)
print(areas)
#-------------------------------------

#soma as areas de cada retangulo
resultado = sum(areas)
print("\n\n|#o resultado da Integral definida com intervalo %s e %s foi: %s#|" % (a, b, resultado))

plt.title("Gráfico da função")
plt.plot(pontos, valores, color="red")
plt.plot([-100, 100],[0,0], color="black")
plt.plot([0, 0],[-200,100], color="black")
plt.fill_between(pontos, valores, color="red", alpha=0.2)
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.show()
