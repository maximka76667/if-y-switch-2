cantidad = int(input("Cantidad: "))
moneda = input("Moneda: ")

if moneda.lower() == "peseta":
    multiplicador = 166.333
else: 
    multiplicador = 0.006
    
resultado = round(cantidad * multiplicador, 2)
print(resultado)
