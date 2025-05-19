"Definir listas de artículos y precios"
items = ["Pasta de dientes", "cepillo de dientes", "enjuage bucal"]
prices = [10.5, 8, 14.7]

" Inicializar las variables"
subtotal = 0

"Recorrer los artículos y calcular el subtotal"
for i in range(0, length(items)):
    item = items[i]
    price = prices[i]
    print("Item " + (i+1) + ": " + item + " - Price: " + price)
    subtotal = subtotal + price

"Calcular IVA (por ejemplo, 15%)"
iva = subtotal * 0.15
total = subtotal + iva

// Show results
print("Subtotal: " + subtotal)
print("iva (15%): " + iva)
print("Total: " + total)