
# calculadora nro6
# esta calculadora realiza calculos de calor sencible

# declaración de variables
masa, variacion_temperatura, calor_especifico, calor_sencible = 0.0 , 0.0 , 0.0 , 0.0

# calculadora
masa = 3
variacion_temperatura = 50
calor_especifico = 0.5
calor_sencible = (masa * calor_especifico * variacion_temperatura)
verificador=(calor_sencible>1)
# mostrar datos
print ( " masa = " , masa)
print ( " variacion_temperatura = " , variacion_temperatura)
print ( " calor_especifico = " , calor_especifico)
print ( " calor_sencible = " , calor_sencible)
print("calor_sencible>1",verificador)




