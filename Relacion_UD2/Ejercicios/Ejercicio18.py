carrito = int(input("Cuantas unidades vas a comprar: "))
articulo = 8.75
total = articulo*carrito
if carrito>=1 and carrito<=10:
    print(f"No tienes descuento, compras un total de {total} euros")
elif carrito>=11 and carrito<=50:
    print(f"Tienes un descuento de el 5%, tu compra de {total} se queda en {total-(total*0.05)} ")
elif carrito>=51 and carrito<=100:
    print(f"Tienes un descuento de el 10%, tu compra de {total} se queda en {total-(total*0.10)} ")
else:
    print(f"Tienes un descuento de el 15%, tu compra de {total} se queda en {total-(total*0.15)} ")