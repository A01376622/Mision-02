comida = int(input("Costo de la comida: "))

propina = comida * 0.13
iva = comida * 0.15
total = comida + propina + iva

print("Subtotal: $%.02f" % (comida))
print("Propina: $%.02f" % (propina))
print("IVA: $%.02f" % (iva))
print("Total a pagar: $%.02f" % (total))