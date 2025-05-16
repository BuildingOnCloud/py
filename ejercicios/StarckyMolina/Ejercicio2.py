string articulo1 = "pasta dental"
string articulo2 = "cepillo de dientes"
string articulo3 = "enguaje bucal"

float precio1 = 10.5
float precio2 = 8
float precio3 = 14.7

float subtotal = precio1 + precio2 + precio3
float totaliva = subtotal * 0.15 
float total = subtotal + totaliva

#Opcion 1
print("articulo 1: " articulo1 "precio: " precio1 )
print("articulo 2: " articulo2 "precio: " precio2 )
print("articulo 3: " articulo3 "precio: " precio3 )

#Opcion 2
for x in range(1..3):
		print("articulo "x": " articulo1 "precio "x": " precio1 )



print("Subtotal: " subtotal)

print("Total IVA: " totaliva)

print("Total: " total)


