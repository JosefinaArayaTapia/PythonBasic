print("Hola Mundo")

#Variables

numero=5
print(numero)
cadena="Josefina"
print(cadena)
numero1=1
Numero1=2

print(numero1)
print(Numero1)

print(Numero1+numero1)

cadena1="Hola"
cadena2="Josefina"
print(cadena1+" "+cadena2)

print("---------------------------------------------")
print("EJERCICIO")

numero_1=5
print(type(numero_1))
numero_2=6.3
print(type(numero_2))
numero_3=7
print(type(numero_3))
sum=numero_1+numero_2+numero_3
print(sum)
print(type(sum))

print("---------------------------------------------")
print("tuplas")
##Inmutables : No se puede cambiar ni agregar datos

tup1=(1,"a",True,"b",23.0)
print(tup1[-1])

print("---------------------------------------------")
print("List")

list=[1,"a",True,"b",23.0]
print(list[-1])

list[0]=100
print(list)
list.append("Nuevo Valor")
print(list)
list.append([1,2,3,4,5,6])
print(list)


print("---------------------------------------------")
print("Dictionary")


d1={"Mango":45,"platano":56}
print(d1)
print(d1.keys())
print(d1.values())
print(d1["Mango"])
d1["Mango"]=100
print(d1["Mango"])

print("---------------------------------------------")
print("Decisiones")

a=20
b=10

if(a>b):
    print("A es mayor que B")

if(a>b) & (a>30):
     print("A es Grande")
elif (b<10):
     print("B es menor que 10")    
else:
    print("Nada")



print("---------------------------------------------")
print("Loops") 

i=1
while(i<=10):
    print(i)
    i=i+1
            

lista=["Rojo","Verde","Amarillo"]
for i in lista:
    print(i)




