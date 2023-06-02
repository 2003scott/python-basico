# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # esto lo cambia a str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print("Este es el valor de : ",my_bool_variable)

# Algunas funciones del sistema / para contar 
print(len(my_string_variable))

# Variable en una sola linea
name , surname , alias , edad = "Scott", "Angeles", "Ckott", 19
print("Me llamo :",name,surname,"Y mi edad es :",edad, "Y mi alias es :",alias)

# Inputs
nombre = input("Ingresa tu nombre :")
edad = input("Ingresa tu edad :")

print(nombre)
print(edad)

# Cambiamos su tipo
nombre = "Scott"
edad = 25
print(name)
print(edad)

# ¿Forzamos el tipado ?
address: str = "Mi direccion"
address = 32
print(type(address))