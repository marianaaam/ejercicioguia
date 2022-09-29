def suma(x, y):
 return x + y

def resta(x, y):
 return x - y

def multiplicacion(x, y):
 return x * y

def division(x, y):
 return x / y

print("Operación a realizar")
print("1: Sumar")
print("2: Restar")
print("3: Multiplicar")
print("4: Dividir")

operacion = input("¿Qué operación quieres hacer? (1; 2; 3 o 4): ")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo numero: "))

if operacion == "1" :
 print (num1,"+",num2,"=", suma(num1,num2))

elif operacion == "2":
 print(num1,"-",num2,"=", resta(num1,num2))

elif operacion == "3":
 print(num1,"*",num2,"=", multiplicacion(num1,num2))

elif operacion == "4":
 print(num1,"/",num2,"=", division(num1,num2))
