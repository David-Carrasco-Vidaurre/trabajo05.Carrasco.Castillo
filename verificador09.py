
# calculadora nro9
# esta calculadora realiza calculos del potencial electrico

# declaración de variables
constante_electrica, carga, distancia, potencial_electrico = 0.0 , 0.0 , 0.0 , 0.0

# calculadora
carga = 60
constante_electrica = 9000000000
distancia = 30
potencial_electrico = (carga * constante_electrica) // (distancia)
verificador=(potencial_electrico<50)
# mostrar datos
print ( " carga = " , carga)
print ( " contante_electrica = " , constante_electrica)
print ( " distancia = " , distancia)
print ( " potencial_electrico = " , potencial_electrico)
print("potencial_electrico<50",verificador)


