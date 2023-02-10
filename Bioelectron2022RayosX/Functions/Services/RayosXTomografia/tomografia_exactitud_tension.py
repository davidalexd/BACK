from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo 
from Functions.Services.valor_minimo import valor_minimo 
from Functions.Services.validacion import validacion


def tomografia_exactitud_tension(attribute_1,attribute_2,attribute_3,attribute_4):
    print(attribute_1,attribute_2,attribute_3,attribute_4,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    try:
        tolerancia = True
        Uc = []
        proms = []

        for x in range(len(attribute_1)):
            try:
                element_2 = attribute_2[x]
            except Exception as e:
                element_2 = 0
            try:
                element_3 = attribute_3[x]
            except Exception as e:
                element_3 = 0
            try:
                element_4 = attribute_4[x]
            except Exception as e:
                element_4 = 0

            prom = promedio([element_2,element_3,element_4])
            correcion = prom
            operacion = (float(attribute_1[x])-correcion)*100/float(attribute_1[x])

            redondear = round(operacion,2)
            
            proms.append([element_2,element_3,element_4])
            Uc.append(redondear)

        if(valor_absoluto(valor_maximo(Uc))>=valor_absoluto(valor_minimo(Uc))):
            operacion_2 = valor_maximo(Uc)
        else:
            operacion_2 = valor_minimo(Uc)


        redondear_2 = round(valor_absoluto(operacion_2),2)
        tolerancia_1 = 5
        tolerancia_2 = -5

        if(redondear_2 <= tolerancia_1 or redondear_2 <= tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":str(attribute_1[0])+" kV",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear_2)+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Desviación ≤ ±5% (entre "+str(attribute_1[0])+" y "+str(attribute_1[-1])+" kVp).",
            "estado":estado
            }
        return resultado
    except Exception as e:
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":"",
                    "estado":""
                }
            ],
            "tolerancia":"",
            "estado":"No Aplica"
            }
        return resultado