#crear la funciòn
def calcular_descuento(monto_total, descuento=10):
    resp = monto_total*(descuento/100)
    return resp

def total(monto_total, descuento=10):
    des = calcular_descuento(monto_total, descuento)
    #calcular el descuento
    total = monto_total - des
    return des, total
#1era llmara a la funcion
monto_total = 500
des, precio_final = total(monto_total)
print(f"valor sin descuento: {monto_total}")
print(f"valor de descuento: {des}")

#2da llamada a la funcion
monto_total1 = 500
des1, precio_final1 = total(monto_total1)
print(f"\nvalor sin descuento: {monto_total1}")
print(f"valor de descuento: {des1}")
print(f"valor con descuento aplicado: {precio_final1}")