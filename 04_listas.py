# Mi listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list)) #Cuenta la lista

my_other_list = [19,1.77,"Scott","Angeles"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
# print(my_other_list[4]) #IndexError
# print(my_other_list[-5]) #IndexError

age,height,name,surname = my_other_list
print(name)

name,height,age,surname= my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3]

print(name)

print(my_list + my_other_list)

my_other_list.append("ScottTecnology")
print(my_other_list)

my_other_list.insert(1,"Negro")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop()) #Eliminar el ultimo dato de la lista
print(my_list)

my_pop_list = my_list.pop(2)
print(my_pop_list)
print(my_list)

del my_list[2] #Eliminar un dato de la lista
print (my_list)

my_new_list = my_list.copy() #Copia una lista
print(my_new_list)

my_new_list.reverse() #Voltea la lista alrevez
print(my_new_list)

my_list.clear() #Limpia la lista
print(my_list)

my_new_list.sort() #Ordena la lista
print(my_new_list)

print(my_new_list[1:2])

my_list = "Hola python"
print(my_list)
print(type(my_list))



