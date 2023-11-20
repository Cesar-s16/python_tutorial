# Inicializamos variables
total_personas = int(input("Ingrese el número total de personas: "))
nombre_mujer_salario_min = ""
nombre_hombre_salario_max = ""
salario_promedio_hombres = 0

# Inicializamos variables para el cálculo del salario promedio de hombres
sum_salario_hombres = 0
total_hombres = 0

# Inicializamos variables para el cálculo del salario mínimo de mujeres
min_salario_mujer = float('inf')

# Iteramos para cada persona
for _ in range(total_personas):
    # Solicitamos datos de la persona
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona (M/F): ").upper()
    salario = float(input("Ingrese el salario de la persona: "))

    # Realizamos las tareas solicitadas
    if sexo == "F" and 5000 <= salario <= 7500:
        print(f"{nombre} es mujer con salario entre 5.000 Bs. y 7.500 Bs.")

    if sexo == "M":
        sum_salario_hombres += salario
        total_hombres += 1
        if salario > salario_promedio_hombres:
            salario_promedio_hombres = salario
            nombre_hombre_salario_max = nombre

    if sexo == "F" and salario < min_salario_mujer:
        min_salario_mujer = salario
        nombre_mujer_salario_min = nombre

# Calculamos el salario promedio de los hombres
if total_hombres > 0:
    salario_promedio_hombres = sum_salario_hombres / total_hombres
else:
    salario_promedio_hombres = 0

# Mostramos los resultados
print("\nResultados:")
print(f"Nombre de la mujer con el sueldo más bajo: {nombre_mujer_salario_min}")
print(f"Nombre del hombre con el sueldo más alto: {nombre_hombre_salario_max}")
print(f"Salario promedio de los hombres: {salario_promedio_hombres:.2f} Bs.")
