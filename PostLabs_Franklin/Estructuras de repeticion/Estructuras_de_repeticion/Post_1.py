cont = 0
cont_par = 0
cont_impar = 0
cont_repetido = 0
sum = 0
suma_par = 0
suma_impar = 0

repetido = int(input("Ingresar que numero a se va a contar si se repite en la serie: "))

while True:
    num = int(input("Ingrese el numero '0', para salir: "))
    if num > 0:
        cont += 1
        sum = sum + num
        
        #verificar si el numero que ingresaron previamente aparece
        if num == repetido:
            cont_repetido += 1
        
        #verificar si el numero es par o impar
        if num%2 == 0:
            cont_par += 1
            suma_par += num
        else:
            cont_impar += 1
            suma_impar += num  
    elif num < 0:
        print("No se aceptan numeros negtivos")      
    else:
        if cont != 0:
            prom = sum/cont
            print(f"El promedio de la lista es de: {prom:.2f}.")
        else:
            print(f"El promedio de la lista es de: 0.")
        
        if cont_par != 0:
            prom_par = suma_par/cont_par
            print(f"El promedio de mumeros pares de la lista es de: {prom_par:.2f}.")
        else:
            print(f"El promedio de numeros pares de la lista es de: 0.")
        
        if cont_impar !=0:    
            prom_impar = suma_impar/cont_impar
            print(f"El promedio de la lista es de: {prom_impar:.2f}.")
        else:
            print(f"El promedio de numeros impares de la lista es de: 0.")
            
        print(f"el numero {repetido}, se repite: {cont_repetido} veces.")
        break