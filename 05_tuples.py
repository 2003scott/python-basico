## Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19,1.74,"Scott","Angeles")
my_other_tuple = (35,60,30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) #IndexError
# print(my_tuple[-6]) #IndexError

print(my_tuple.count("Scott")) #Cuenta cuantos datos hay iguales dentro de la tupla
print(my_tuple.index("Angeles")) # Nos dicen en que posicion esta

# my_tuple[] = 1.80
# print(my_tuple)

