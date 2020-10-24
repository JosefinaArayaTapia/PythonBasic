import numpy as np

#Single Dimensional numpy array

n1=np.array([1,2,3,4,5])
print(type(n1))

#Multiple dimensional numpy

n2=np.array([[1,2,3,4],[5,6,7,8]])
print(type(n2))

#Zeros

n3=np.zeros((60,9)) #Matriz
print(n3)

n4=np.full((3,3),7) #Full matriz con el numero indicado
print(n4)


#ranges
n5=np.arange(1,11)
print(n5)
n6=np.arange(100,300,50) ##Rango de 50 en 50
print(n6)

#random

n7=np.random.randint(1,100,6)
print(n7)

## suma para arrays

n8=np.array([10,20])
n9=np.array([30,50])

print(np.sum([n8,n9])) ##Suma total

print(np.sum([n8,n9],axis=1)) ##Suma Horizontal
print(np.sum([n8,n9],axis=0)) ##Suma Vertical


##Join de arrays

n8=np.array([10,20])
n9=np.array([30,50])

print(np.vstack((n8,n9))) ##Join en un solo Arrray Vertical
print(np.hstack((n8,n9))) ##Join en un solo Arrray Horizonal
print(np.column_stack((n8,n9))) ##Join en un solo Arrray Columnal


