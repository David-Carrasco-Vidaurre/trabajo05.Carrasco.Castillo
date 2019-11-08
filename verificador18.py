# calculadora nro18
# esta calculadora realiza cálculos de la fuerza de rozamiento

# declaración de variables
coeficiente_rozamiento, fuerza_normal, fuerza_rozamiento = 0.0 , 0.0 , 0.0

# calculadora
coeficiente_rozamiento = 2.5
fuerza_normal = 100
fuerza_rozamiento = (coeficiente_rozamiento * fuerza_normal)
verificador=(fuerza_rozamiento<15)
# mostrar datos
print ( " coeficiente_rozamiento = " , coeficiente_rozamiento)
print ( " fuerza_normal = " , fuerza_normal)
print ( " fuerza_rozamiento = " , fuerza_rozamiento)
print("fuerza_rozamiento<15",verificador)
