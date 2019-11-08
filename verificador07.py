# calculadora nro7
# esta calculadora realiza calculos de las resistencias

# declaración de variables
voltaje, resistencia, intencidad_corriente = 0.0 , 0.0 , 0.0

# calculadora
voltaje = 80
intencidad_corriente = 5
resistencia = ( voltaje // intencidad_corriente)
verificador=(resistencia==20)
# mostrar datos
print ( " voltaje = " , voltaje)
print ( " intencidad_corriente = " , intencidad_corriente)
print ( " resistencia = " , resistencia)
print("resistencia==20",verificador)
