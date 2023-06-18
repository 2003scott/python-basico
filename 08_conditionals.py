# Condicionales

my_condition = False

if my_condition:  # esto es igual que if my_condition === true
    print("Se ejecuta la condicion del if")

my_condition = 25

if my_condition == 10:
    print("Se ejecuta la condicion true")

if my_condition > 10 and my_condition < 20:
    print("Es Mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


print("La ejecucion continua")

my_string = ""

if not my_string :
    print("Mi cadena de texto no es vacia")
if my_string=="Mi cadena de textooooo":
    print("Estas cadenas de texto coinciden")
    
