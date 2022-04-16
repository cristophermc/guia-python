#En este programa vamos a ver diferentes tipos de datos.
#Los datos son entidades que representan un tipo de valor, que guardan un significado.

#Lo primero que vamos a ver son los datos de tipo string. Los string son caracteres de texto, como por ejemplo la palabra perro.
print("Esto de aquí es un string. Perro es un dato de tipo string.")
#¡Python puede usarse como una calculadora!
#En python puedes utilizar los operadores siguientes para calcular:  + - / *
# + Sirve para sumar
# - Sirve para restar
# / Sirve para dividir de forma inexacta
# // Sirve para dividir de forma exacta
# * Sirve para multiplicar
# ** Sirve para exponenciales

#Los siguientes datos son de tipo numérico. Hay diferentes tipos numéricos.
#Los numéricos float y los numéricos int


#Los numéricos float permiten operar con decimales. Veamos un ejemplo:
print(float(2.3-1))
#Observa que para que podamos mostrar en pantalla el resultado tenemos primero que añadir un paréntesis con la función float para convertir los datos a tipo float. De otra manera 
#serían de tipo string.

#Los numéricos int permiten operar con números enteros. Veamos un ejemplo:
print(int(4-1))
#Observa que para que podamos mostrar en pantalla el resultado tenemos primero que añadir un paréntesis con la función int para convertir los datos a tipo int. De otra manera
#serían de tipo string. 

#Por último tenemos los tipos de datos booleanos o lógicos. Estos determinan si una relación entre datos son verdaderas o falsas. 

#En el siguiente ejemplo vamos a comprobar si 3 es igual a 1. Lo normal sería que fuera falso. Comprobemos:
print(3==1)
#El resultado tiene que ser false.

#En el siguiente ejemplo vamos a comprobar lo contrario. Si 3 es distinto de 1. Esto es correcto. Comprobemos:
print(3!=1)
#El resultado tiene que ser true.

#En el siguiente ejemplo vamos a comprobar que 3 es mayor que 1. Comprobemos:
print(3>1)
#El resultado tiene que ser true.

#En el siguiente ejemplo vamos a comprobar que 1 es menor que 3. Comprobemos:
print(1<3)
#El resultado tiene que ser true.

#En el siguiente ejemplo vamos a comprobar que 5 es menor o igual que 10. Comprobemos:
print(5<=10)
#El resultado tiene que ser true porque 5 es menor que 10 y al menos una de esas dos condiciones se evalua y es true. 
#Comprobemos el caso siguiente:
print(10<=10)
#El resultado ahora también será true porque se evalua la condición de que 10 = 10.

#En el siguiente ejemplo vamos a comprobar que 5 es mayor o igual que 1. Comprobemos:
print(5>=1)
#El resultado tiene que ser true porque 5 es mayor que 1 y al menos una de esas dos condiciones se evalua y es true.
#Comprobemos el caso siguiente:
print(1>=1)
#El resultado ahora también será true porque se evalua la condición de que 1 = 1.

#En resumen, el álgebra booleana determina si dos condiciones son verdaderas o falsas. 