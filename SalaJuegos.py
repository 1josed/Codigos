#Sala de juegos
nombre=input("Ingrese su Nombre")
edad=int(input("ingrese edad"))

if edad<12:
    valor_entrada = 0
elif 12<= edad <=16:
    valor_entrada =2000
else:
    valor_entrada =3500

print("El Valor de la entrada es:"+ str(valor_entrada))


contrasena = "1"

while True:
    clave = input("ingrese la clave:")
    if clave == contrasena:
        print("clave correcta")
        break
    else:
        print("clave incorrecta")

num1 = float(input("ingrese el primer número:  "))
num2 = float(input("ingrese el segundo número: "))
num3 = float(input("ingrese el tercer número:  "))
num4 = float(input("ingrese el cuarto número:  "))

suma = num1 + num2 + num3 + num4
promedio = suma / 4

print(f"la suma de los números es {suma}")
print(f"el promedio de los números es {promedio}")

numero = int(input("ingrese un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")