from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def mamografia_almacen(attribute,attribute_1,attribute_2,attribute_3):
    try:
        tolerancia = True
        Uc = []

        for x in range(len(attribute)):
            prom = promedio([attribute_1[x],attribute_2[x],attribute_3[x]])
            valor = float(attribute[x])/prom
            Uc.append(valor)
        
        max = valor_maximo(Uc)

        redondear = round(max,2)
    
        estado = validacion([tolerancia]) 

        
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" µGy/mAs",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"",
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