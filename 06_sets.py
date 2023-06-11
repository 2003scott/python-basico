# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Diego","Scott",19}
print(type(my_other_set))

print(len(my_other_set)) # Cuenta cuantos datos hay dentro del set

my_other_set.add("Ckott")
print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Ckott") #Un set no permite repetidos
print(my_other_set)

print("Scott" in my_other_set)
print("Scochi" in my_other_set)

my_other_set.remove("Scott")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) # NameEror : name 'my_other_set' id not defined

my_set = {"Diego","Scott",19}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = { "Javascript","Java","Python"}

my_new_set= my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set.union({"Javascript","C#"})))

print(my_new_set.difference(my_set)) # Buscas diferencias entres estos 2 sets

