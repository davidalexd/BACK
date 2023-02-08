from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def fluoroscopia_compensacion_diferentes_espesores(attribute_1,attribute_2,attribute_3,attribute_4):
    try:
        if(attribute_1[0]!=None or attribute_2[0]!=None or attribute_3[0]!=None or attribute_4[0]!=None):
            tolerancia=True
            tolerancia_1 = 20
            tolerancia_2 = -20
            Uc = []
            validar = []
            for x in range(len(attribute_1)):
                element_1 = float(attribute_1[x])
                prom = promedio([attribute_2[x],attribute_3[x],attribute_4[x]])

                operacion = (element_1-prom)*100/element_1
                redondeo = round(operacion,2)   

                if(redondeo <=tolerancia_1 or redondeo<=tolerancia_2):
                    tolerancia=True
                else:
                    tolerancia=False

                validar.append(tolerancia)
                Uc.append({
                    "parametros":"",
                    "resultado":str(redondeo)+" %",
                    "estado":tolerancia
                })

            estado = validacion([validar])

            resultado = {
                "condicion":"",
                "data":Uc,
                "tolerancia":"Variación < ±20% respecto a los valores de referencia",
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

