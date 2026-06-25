
def calcular_promedio(nota1,nota2,nota3):
    promedio = (nota1 + nota2 + nota3)/3
    return promedio

n1 = float(input("ingrese primera nota: "))
n2 = float(input("ingrese segunda nota: "))
n3 = float(input("ingrese tercera nota: "))

promedio_final = calcular_promedio(n1,n2,n3)
print("promedio:",round(promedio_final, 2))

if promedio_final >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")