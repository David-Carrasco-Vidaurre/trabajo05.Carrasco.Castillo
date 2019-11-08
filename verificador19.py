# calculadora nro19
# esta calculadora realiza cálculos del área lateral de un prisma recto

# declaración de variables
perimetro, arista_lateral, area_lateral = 0.0 , 0.0 , 0.0

# calculadora
perimetro = 15
arista_lateral = 5
area_lateral = (perimetro * arista_lateral)
verificador=(area_lateral>=25)
# mostrar datos
print ( " perimetro = " , perimetro)
print ( " arista_lateral = " , arista_lateral)
print ( " area_lateral = " , area_lateral)
print("area_lateral>=25", verificador)
