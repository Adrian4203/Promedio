#Nombre
nom=input("Ingrese el nombre del estudiante"":_")

#Cotidiano
for i in range (1,6):
    suma=int(input("Digite el trabajo cotidiano"+str(i)+":_"))
    promedio=(suma/5)*0.4
print("Su promedio de cotidiano es de: ")
print(promedio)

#TrabajoExtraclase

for a in range (1,3):
    suma=int(input("Digite el trabajo Extraclase"+str(a)+":_"))
    promedioEx=(suma/2)*0.1
print("Su promedio de Trabajo Extracase es de: ")    
print(promedioEx)

#pruebas

for e in range (1,3):
    suma=int(input("Digite las notas de las pruebas"+str(e)+":_"))
    promediopr=(suma/2)*0.2
print("Su promedio de prueba es de: ")
print(promediopr)

#Proyecto

Pry=int(input("Ingrese la nota del proyecto"":_"))
promedioproyecto=(Pry)*0.2
print("Su promedio de proyecto es de: ")
print(promedioproyecto)

#Asistencia
ausencias=int(input("Digite el numero de ausencias: "))
tardias=int(input("Digite numero de tardias: "))
rebajo=ausencias*1+tardias*0.5

if(rebajo<=9):
    asistencia=10-rebajo
else:
    asistencia=1

print("Su promedio de asistencia es de: ")
print(asistencia)
#Nota Final

notafinal=int(promedio+promedioEx+promediopr+promedioproyecto)/2
print(nom)
print("Su promedio final es de: ")
print(notafinal)
#Salir
prompt = "\nIngresa 'Salir' para salir del programa: "

while True:
    opcion = input(prompt)

    if opcion == 'salir':
        break



