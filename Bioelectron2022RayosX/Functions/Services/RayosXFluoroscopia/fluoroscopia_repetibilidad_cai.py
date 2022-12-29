from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion

def fluoroscopia_repetibilidad_cai(attribute_1,attribute_2,attribute_3):
        try:
            desv = desviacion_estandar_m([attribute_1[0],attribute_2[0],attribute_3[0]])
            prom = promedio([attribute_1[0],attribute_2[0],attribute_3[0]])
            tolerancia = True
            if(prom == 0):
                operacion = 0
            else:
                operacion = desv/prom
                
            redondear = round(operacion*100,2)
            
            if(redondear<=10):
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
                "tolerancia":"Coeficiente de variación ≤ 10%",
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