# String 

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\Este es un String con spacio \\n escapado"
print(my_scape_string)

#Formateo

name ,surname ,edad= "Diego", "Scott",19

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,edad))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,edad))
print("Mi nombre es " +name+" "+surname+" y mi edad es "+str(edad))
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")

# Desenpaquetado de caracteres
language= "python"
a,b,c,d,e,f = language
print(a)
print(b)

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)


# Reverse 

reverse_language = language[::-1]
print(language_slice)


# Funciones

print(language.upper())
print(language.capitalize())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print(language.upper().isupper())
print(language.startswith("py"))