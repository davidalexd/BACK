from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def dental_panoramico_valor_rendimiento(element,element_1,element_2,attribute):
    print(element,element_1,element_2,attribute,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
    try: 
        prom = promedio(attribute)
        # dosis
        variante = float(element[0])
        
        variante_1 = float(element[0])**2
        # distancia foco detector 
        variante_2 = float(element_1[0])*float(element_2[0])
        # corriente + tiempo de exposicion
    
        if (variante_2 == 0):
            operacion = 0
        else:
            operacion = (prom*variante_1)/variante_2

        redondeo = round(operacion,2)
        tolerancia = True

        if(redondeo > 25):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":str(variante)+" cm /  80 kV / "+str(element_2[0])+" mm Al de filtración total",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondeo)+" uGy/mAs",
                    "resultado_salida":redondeo,
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Rendimiento a 1m > 25 uGy/mAs a 80 kV reales y 2.5 mm Al de filtración total.",
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