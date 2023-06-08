## Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19,1.74,"Scott","Angeles","Scott")
my_other_tuple = (35,60,30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) #IndexError
# print(my_tuple[-6]) #IndexError

print(my_tuple.count("Scott")) #Cuenta cuantos datos hay iguales dentro de la tupla
print(my_tuple.index("Angeles")) # Nos dicen en que posicion esta

# my_tuple[] = 1.80 'tuple' object does not suppoty iteam assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(my_tuple)

my_tuple[4] = "Dscott"
my_tuple.insert(1,"Azul") # Inserta un dato ala tupla
my_tuple= tuple(my_tuple)
print(my_tuple)
print(tuple(my_tuple))

del my_tuple[2]
print(my_tuple)

del my_tuple
# print(my_tuple) NameError : __name__ "My_tyuple" is not defined



