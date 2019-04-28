"""
BLOCO_C
    INPUTS:
        x -->  List access --> type: ghdoc (rhinoscriptsyntax)
        y --> um (01) perfil   : Item access --> type: int
              dois ou n perfis : List access --> type: int
        z --> um (01) perfil   : Item access --> type: float
              dois ou n perfis : List access --> type: float
    OUTPUTS:
        out  --> informações visuais (OK ou não OK)
        a --> none
"""

lista_grande = x 
sub_lista = y    

size_lista_grande = len(lista_grande)
size_sub_lista = len(sub_lista)

nova_lista = []

for i in range (size_sub_lista):
    nova_lista.append([])

n = int(sub_lista[0])
cont = 0
cont_big_list = 0
cont_sub = 0
while (cont < 3):
    size_atual = y[cont_sub]
    cont_sub += 1
    
    for j in range(int(size_atual)):
        value = x[cont_big_list]
        nova_lista[cont].append(value)
        cont_big_list += 1
    cont += 1

a = nova_lista[2]
#print a

solMax = []                                             
cont_three = 0

while (cont_three < 3):
    lista_atual = nova_lista[cont_three]
    listAbs = map(abs, lista_atual)                    
    listAbs.sort()                                     
    solMax.append(listAbs[-1])                         
    cont_three += 1



#Check security (request <resistance)
maxRes = z                           
maxSol = solMax

num = (len(maxRes))
cont_four = 0

a = []
p = []

while cont_four < num:
    if solMax[cont_four] < maxRes[cont_four]:
        print ('Barras %i estão OK!' %cont_four)
    else:
        print ('Barras %i estão NOT OK!' %cont_four)
    cont_four += 1