#1
number1 = input (" ingrese su edad \n")
while not number1.isdigit():
    number1 = input(" ingrese su edad \n") 


number_int = 100 - int(number1)
print ("faltan " + str(number_int) + " años para llegar a los cien años. \n")

  

#2
gradosC = (input ("ingrese una temperatura en grados celcius: \n"))
while not gradosC.isdigit():
    gradosC = (input ("ingrese una temperatura en grados celcius: \n"))
grados_F= ((int(gradosC) * (9/5)) + 32)
print ("la temperatura ingresa en farenheit " + str(grados_F))

#3
nro = 1
sumaNat = 0
for nro in range(101):
    sumaNat += nro
    nro += 1
print ("la suma de los numeros naturales hasta el 100 es de " + str (sumaNat))

#4
lista = [1, 5, 8, 10, 12, 25, 31, 40, 47, 58]
for nro in lista:
    if nro%2 == 0:
        print (str(nro) + "\n" )

#5
entrada = input (" Ingrese los numeros separados con un espacio \n")
lista2 = list (map(int, entrada.split()))
print (" Los numeros ingresados son \n")
for num in lista2:
    if num < 0:
        break
    print ( " el numero es " , num)


#6
listaPar = [nro for nro in lista if nro%2 == 0]
listaImp = [nro for nro in lista if nro%2 != 0]
print (" \n en la lista par tenemos \n")
for n in listaPar:
     print (str(n))
print (" \n en la lista impar tenemos \n")
for n in listaImp:
     print (str(n))
        
#7

entrada7 = input (" Ingrese la lista de numeros separados con un espacio \n")
lista7 = list (map(int, entrada7.split()))
resultado = "-".join(str(number) for number in lista7 if number % 3 != 0)
print (" la lista que queda sin los multiplos de 3 es de ", resultado)

