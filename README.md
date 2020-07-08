# truss_analysis
Template para automatizar análise estrutural de treliças metálicas no ambiente Grasshopper + Karamba 3D


## Sobre

Neste repositório você encontrará um template escrito em Python para automatizar projetos de treliças metálicas constituídas de barras tubulares, de acordo com a norma brasileira [NBR8800](https://www.abntcatalogo.com.br/norma.aspx?ID=1459).

## Objetivo

O objetivo principal deste template é servir de ferramenta computacional para disseminar a utilização de scripts para solucionar problemas, ou ainda, automatizar tarefas entre arquitetos e engenheiros projetistas, assim como auxiliar o aprendizado de estudantes de estruturas metálicas.

# Estrutura 

Dividos em três partes (blocos A, B e C), o template funciona da seguinte maneira:

1. bloco A - busca opções de seções de perfils em uma tabela tipo .csv (arquivos de texto com valores separados por vírgulas);

2. bloco B - calcula a resistência máxima dos perfis selecionados no bloco anterior;

3. bloco C - verifica as condições de seguranças exigidas pela NBR8800, ou seja, se a solicitação máxima de cada perfil escolhido é menor ou igual sua resistência máxima. 

Como exemplo, veremos um caso de uma treliça espacial plana (imagem abaixo) genérica,  constituída por três diferentes seções (banzo superior, banzo superior e diagonal) e desenvolvida no ambiente rhinoceros + karamba. 


![](images/truss_diagram.jpg)


## Exemplo de aplicação

Neste exemplo, foram utilizados os seguintes *add-on* para Grasshopper 3d:

1. [karamba 3d](https://www.food4rhino.com/app/karamba3d) - aplicativo para análise estrutural; 

2. [ghpython](https://www.food4rhino.com/app/ghpython) - interpretador Python para o Grasshopper.


Modelos definidos, agora vamos ver como utilizar o template..


#### Bloco A

A primeira coisa é decidir com quantos tipos de perfis pretendemos trabalhar. Neste caso, utilizaremos três seções diferentes, uma para as barras do banzo superior (perfis 0), outra para as barras do banzo inferior (perfis 1) e outra para as diagonais (perfis 2).

![](images/1_apres.gif)

Em seguinda, mostramos o caminho que o *script* deverá fazer para ler a tabela .csv de perfis.

![](images/2_buscando_perfis.gif)

obs.: neste tabela, adotamos os 30 perfis mais frequentemente produzidas pela empresa [Vallourec](http://www.vallourec.com/COUNTRIES/BRAZIL/PT/Products-and-services/automotive-industrial-tubes/Documents/Catalogo%20Estruturais.pdf).

O próximo passa foi definir um controle deslizante de números para cada seção. Lembre-se de edita-los para deixa-los com números suficientes para percorrer todoas as seções contidas na tabela .csv.

![](images/3_index_perfis.gif)

Para que o interpretador Python do Grasshopper funcione bem, devemos informar corretamente o tipo de entradas que ele receberá.  

Para o bloco A, teremos as seguintes opções de inputs:

``` 
    INPUTS:
        f     --> Item access --> type: ghdoc (rhinoscriptsyntax)
        index --> um (01) perfil   : Item access --> type: int
                  dois ou n perfis : List access --> type: int
```


![](images/4_recebendo_perfis.gif)


Pronto, já podemos ver a resposta deste bloco, uma lista de diâmetros e espessuras das seções escolhidas:


![](images/5_saida_perfis.gif)

Atenção para o formato da saída deste bloco. Uma lista ordenada da seguinte maneira:

|         | perfil 0    |           | perfil 1    |           | ...    |       | perfil n    |           |
|---------|-------------|---------- |-------------|-----------|--------|-------|-------------|-----------|
|__lista__| diâmetro 0  |espessura 0| diâmetro 1  |espessura 1| ...    | ...   | diâmetro n  |espessura n|



Estas saídas devem ser ligadas aos nós *cross-sections* karamba respeitando a ordem de montagem do modelo estrutural.


![](images/6_perfis_karamba.gif)

#### Bloco B

As mesmas saídas ligas ao Karamba também precisam ser ligadas as entradas (componentes *merge* diâmetros e espessuras) do bloco B. Isso porque, este bloco é responsávl por calcular as resistências máximas de cada seção escolhida no bloco anterior.

Atenção para os inputs do bloco B. 

```
    INPUTS:
        diameterCm -->  um (01) perfil   : Item access --> type: float
                        dois ou n perfis : List access --> type: float
        thicknessCm --> um (01) perfil   : Item access --> type: float
                        dois ou n perfis : List access --> type: float
        materialResistance --> Item access --> type: float

```

![](images/7_perfis_caminho.gif)

Veja só o output deste nó. Os resultados das resistências máximas para cada seção devidamente calculados.

![](images/8_res_max.gif)

Cuidado com a saída. Os outputs do bloco B são dois, um meramente visual com a intenção de nós auxiliar no processo e outro com os dados, uma lista de valores que deverão ser enviados adiante. 

```
    OUTPUTS:
        out  --> informações visuais (resistência(s) máxima(s))
        maximumResistance --> lista de resistência(s) máxima(s)
```

#### Bloco C

Por fim, precisamos alimentar o último bloco do template. Ele será responsável por acusar quais seções atendem a exigência da norma descrita anteiormente. A seção aprovada receberá o 'OK', já a reprovada, 'NOT OK'.

Para isso, buscamos as solicitações de todas as barras diferentamente nos nós *b-res-force* karamba.

Então, novamente atenção para os inputs do bloco C

```
    INPUTS:
        x -->  List access --> type: ghdoc (rhinoscriptsyntax)
        y --> um (01) perfil   : Item access --> type: int
              dois ou n perfis : List access --> type: int
        z --> um (01) perfil   : Item access --> type: float
              dois ou n perfis : List access --> type: float
```

![](images/9_solic_karamba.gif)

Em seguidas, precisamos informar quantas barras têm no modelo (número de barras no banzo superior, inferior e diagonal).

![](images/10_num_barras.gif)

Pronto. Agora é só experimentar as seções contidas no arquivo .csv e ver quais atendem nosso projeto.

![](images/11_analise_final.gif)

obs. Output do bloco C

```
    OUTPUTS:
        out  --> informações visuais (OK ou NOT OK)
        a --> none
```

### Atenção

É claro que está é uma análise preliminar e não atende todas as exigências contidas na NBR8800. Mas, com certeza é uma boa maneira de evitar desperdício de tempo recalculando tração e compressão dezenas de vezes durante o projeto. 


### Gostou?

Link para baixar o template e exemplo [AQUI](https://github.com/renatogcruz/truss_analysis/tree/master/files).

Sinta-se à vontade para baixar, testar, usar e modificar este template.
