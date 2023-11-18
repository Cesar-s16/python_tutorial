monto_compra = float(input("Ingresa el monto de la compra: "))

#Calculamos el descuento (15%)
descuento = 0.15 * monto_compra

#Calculamos el monto a pagar por el IVA (16%)
iva = 0.16 * monto_compra

#Calculamos el monto total a pagar
monto_total = monto_compra - descuento + iva

#resultados
print(f"Monto de la compra: ${monto_compra:.2f}")
print(f"Descuento (15%): ${descuento:.2f}")
print(f"Monto a pagar por IVA (16%): ${iva:.2f}")
print(f"Monto total a pagar: ${monto_total:.2f}")
