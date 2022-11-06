from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def tomografia_valor_medio_numero_ct(element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
    tolerancia_1 = True
    tolerancia_2 = False

    redondear_1 = round(float(element_1[0]))
    redondear_2 = round(float(element_2[0]))

    tolerancia_a_1 = 4
    tolerancia_a_2 = -4

    tolerancia_b_1 = -1004
    tolerancia_b_2 = 996

    if(valor_absoluto(redondear_1)<tolerancia_a_1 or valor_absoluto(redondear_1)<tolerancia_a_2):
        tolerancia_1 = True
    else:
        tolerancia_1 = False

    if(valor_absoluto(redondear_2)<tolerancia_b_1 or valor_absoluto(redondear_2)<tolerancia_b_2):
        tolerancia_2 = True
    else:
        tolerancia_2 = False

    estado = validacion([tolerancia_1,tolerancia_2])
    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":"Agua: "+redondear_1+" UH",
                "estado":tolerancia_1
            },
            {
                "parametros":"",
                "resultado":"Aire: "+redondear_2+" UH",
                "estado":tolerancia_2
            }
        ],
        "tolerancia":"Agua (0 ± 4) UH / Aire (-1000 ± 4) UH.",
        "estado":estado
        }

    return resultado
    