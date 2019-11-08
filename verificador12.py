# calculadora nro12
# esta calculadora realiza calculos de la energia elastica

# declaración de variables
constante_elastica, distancia_deformada, energia_elastica = 0.0 , 0.0 , 0.0

# calculadora
constante_elastica = 100
distancia_deformada = 20
energia_elastica = (constante_elastica * distancia_deformada * distancia_deformada) // 2
verificador=(energia_elastica<900)
# mostrar datos
print ( " constante_elastica = " , constante_elastica)
print ( " distancia_deformada = " , distancia_deformada)
print ( " energia_elastica = " , energia_elastica)
print("energia_elastica<900",verificador)




