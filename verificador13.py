# calculadora nro13
# esta calculadora realiza calculos de la altura maxima

# declaración de variables
gravedad, tiempo_vuelo, altura_máxima = 0.0 , 0.0 , 0.0

# calculadora
gravedad = 9.8
tiempo_vuelo = 20
altura_maxima = (gravedad * tiempo_vuelo * tiempo_vuelo) // 8
verificador=(altura_maxima>=30)
# mostrar datos
print ( " gravedad = " , gravedad)
print ( " tiempo_vuelo = " , tiempo_vuelo)
print ( " altura_maxima = " , altura_maxima)
print("altura_maxima>=30",verificador)



