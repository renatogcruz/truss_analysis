"""
BLOCO_B
    INPUTS:
        diameterCm -->  um (01) perfil   : Item access --> type: float
                        dois ou n perfis : List access --> type: float
        thicknessCm --> um (01) perfil   : Item access --> type: float
                        dois ou n perfis : List access --> type: float
        materialResistance --> Item access --> type: float
    OUTPUTS:
        out  --> informações visuais (resistência(s) máxima(s))
        maximumResistance --> lista de resistência(s) máxima(s)
"""

listDiameter = (diameterCm)
listThickness = (thicknessCm)

num = (len(listThickness))
cont = 0

maximumResistance = []

while cont < num:
    diameter = listDiameter[cont] * 10
    thickness = listThickness[cont] * 10
    profileArea = (((3.14159 * diameter ** 2)/4) 
                - ((3.14159 * (diameter-(thickness*2)) **2 )/4))
    maxRes = profileArea * materialResistance
    maximumResistance.append(maxRes)
    cont += 1

size_maximumResistance = len(maximumResistance)
cont_2 = 0
for i in range(size_maximumResistance):
    valor = maximumResistance[cont_2]
    print("Res. Máxima perfil %s = %.2f KN." %(i, valor))
    cont_2 += 1