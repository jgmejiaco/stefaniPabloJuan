
print("\n")
print("\n")

print("¡Hola! bienvenido al programa que calcula la temperatura del valle de aburrá\n")

cantidad = int(input(f"Digite la cantidad de registros de temperatura que desea analizar: "))


contador = 0

temperaturas = []

promedio = 0

while contador < cantidad:
    contador += 1
    temperatura = int(input(f"Ingrese la temperatura N° {contador}: "))
    temperaturas.append(temperatura)
 
for temperaturaPromedio in temperaturas:
    promedio = promedio + temperaturaPromedio

    
print(f"La temperatura promedio del valle de aburrá es de {promedio / cantidad}°")

