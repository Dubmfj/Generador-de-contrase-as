import random

print("Hola mundo!")
caracteres = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
longitud = int(input("Introduce la longitud de la contraseña: "))
contraseña = ""
for i in range(longitud):
        contraseña += random.choice(caracteres)
print("Contraseña generada:", contraseña, "\nLongitud:", longitud)