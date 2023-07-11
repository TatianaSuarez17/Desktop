Venta:int(input("Ingrese valor de factura"))

Iva = 0.15
Precioventa= Venta
Preciobruto= Precioventa + Iva

if Preciobruto > 1000:
    descuento= Preciobruto - 0.5
else:
    iva= 0.15

print(f"Factura de su compra es {Preciobruto}")