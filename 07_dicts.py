## Diccionaries 

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Scott","Apellido":"Angeles","Edad":19, 1:"Python"}

my_dict = {
    "Nombre":"Scott",
    "Apellido":"Angeles",
    "Edad":19,
    "Lenguajes":{"Python","Java","JavaScript"},
    1 : 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Diego"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle ScottDev" # Anadimos a nuestra diccionario
print(my_dict)

del my_dict["Calle"] # Eliminamos de nuestro diccion
print(my_dict)

# Esto nos dice si existe o no exite dentro de nuestro dict
print("Scott" in my_dict)
print("Apellido" in my_dict)
 
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1 , "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1 , "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict,["Diego","Scott"])
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))



