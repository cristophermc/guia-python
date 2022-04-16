#En este programa vamos a ver lo que son los condicionales.
#Los condicionales son estructuras que permiten ejecutar códigos que dependen de una condición.
#Veamos el siguiente ejemplo:

edad = int(input(("¿Qué edad tienes?: ")))

if edad >= 18:
    print("Eres mayor de edad, porque tienes" + " " +  str(edad) + " " + "años.")
else:
    print("Eres menor de edad.")