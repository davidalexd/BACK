from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def fluoroscopia_variacion_rendimiento_carga(element_1,attributes_1,attributes_2,attributes_3,attributes_4):
    try:
        prom_1 = promedio([attributes_2[0],attributes_3[0],attributes_4[0]])
        prom_2 = promedio([attributes_2[1],attributes_3[1],attributes_4[1]])
        tolerancia = True
        cuad = float(element_1[0])**2
        part_1 = (((prom_1*cuad)/float(attributes_1[0]))-((prom_2*cuad)/float(attributes_1[1])))
        part_2 = (((prom_1*cuad)/float(attributes_1[0]))+((prom_2*cuad)/float(attributes_1[1])))
        

        if (part_2 == 0):
            operacion = 0
        else:
            operacion = part_1/part_2

        redondear = round(operacion,2)

        if(redondear<=0.1):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+"%",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Coeficiente de linealidad 0.1",
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