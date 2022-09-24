'''
Escriba un programa que pida el ancho y largo de un rectángulo y permita calcular:
-Área
-Perímetro
-Graficar el rectángulo

Ejemplo: Ancho=5 Altura=3

'''
ancho = float(input("Digite el ancho del rectángulo en metros: "))
alto = float(input("Digite el alto del rectángulo en metros: "))

area = ancho * alto
perimetro = (ancho * 2) + (alto * 2)
# area = ancho * alto

print(f'El área es: {area}')
print(f'El perímetro es: {perimetro}')

# m = input() n = input()
# for i in range(n): print"|" for j in range(m): print "-",

# for i in range(ancho):
#     print("|") 

#     for j in range(alto):
#         print("-")