"""
BLOCO_A
    INPUTS:
        f     --> Item access --> type: ghdoc (rhinoscriptsyntax)
        index --> um (01) perfil   : Item access --> type: int
                  dois ou n perfis : List access --> type: int
    OUTPUTS:
        out  --> informações visuais (perfi(s), diâmetro(s) e espessura(s))
        lista_perfil --> lista de diâmetro(s) e espessura(s) dos perfis
"""

import rhinoscriptsyntax as rs

lista = []               
f = open(f, 'r')         

for line in f:
    lista_line = line.rstrip().split('\t')
    lista.append(lista_line)

tamanho_index = len(index)
lista_perfil = []
cont = 0

while cont < tamanho_index:      
    i = index[cont]
    profile = lista[i]
    p = profile[0].split(',')  
    diameter = p[0] 
    Diameter = float(diameter) / 10
    lista_perfil.append(Diameter)
    thickness = p[1]
    Thickness = float(thickness) / 10
    lista_perfil.append(Thickness)
    cont += 1


a = (lista_perfil)

cont_2 = 0
cont_3 = 1
size_lista_perfil = len(a)
for i in range(tamanho_index):
    print ("perfil %s -(d) %.2f cm -(t) %.2f cm" %(i, a[cont_2], a[cont_3]))
    cont_2 += 2
    cont_3 += 2