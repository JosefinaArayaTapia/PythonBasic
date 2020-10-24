import pandas as pd

##Series
s1=pd.Series([1,2,3,4])
print(s1)
print(type(s1))

s1=pd.Series([1,2,3,4],index=["a","b","c","d"]) #Indice
print(s1)
print(type(s1))

s2=pd.Series({'a':10,'b':20}) ##Diccionario
print(s2)
print(type(s2))


##Dataframe: Like Table (Rows / Columns)

Estudiantes = {"Nombres_Estudiantes":["Pedro","Juana","Carmela"],"Notas":[7,7,1]}
df=pd.DataFrame(Estudiantes)
print(df)

nz=pd.read_csv('https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional-csv.csv')
print(nz.head(5)) ##Primeros
print(nz.tail()) ## Ultimos
print(nz.describe())


print(nz.iloc[0:5,0:5]) #Localiza las filas del 0 al 5 y las columnas del 0 al 3 (Tipo Matriz)

print(nz.iloc[0:5,[8,4]]) 

print(nz.loc[1:3,("Year","Units")])


df1= nz[nz["Year"]==2019]
print(nz.head())
print(df1.count())
