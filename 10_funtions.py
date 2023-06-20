### Functions 

def my_funtion():
    print("Esto es una funcion")

my_funtion()
my_funtion()
my_funtion()

def suma(a,b):
    print(a + b)

def resta(a,b):
    print(a - b)

def multiplicacion(a,b):
    print(a * b)

def division(a,b):
    print(a / b)

suma(20,2)
resta(20,2)
multiplicacion(20,2)
division(20,2)



# Función con parámetros de entrada/argumentos

def sum_two_values(first_value:int , second_value):
    print(first_value + second_value)

sum_two_values(5,7)
sum_two_values(54754,71231)
sum_two_values("5","7")
sum_two_values(1.4,5.2)



# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4,5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)


# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}") # Tipo de concatenacion


print_name(surname="Moure", name="Brais")


# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Diego", "Scott")
print_name_with_default("Diego", "Scott", "Ckott")



# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "2003scott")
print_upper_texts("Hola")


