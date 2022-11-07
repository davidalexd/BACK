from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def fluoroscopia_compensacion_diferentes_espesores(attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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
            "resultado":redondeo+" %",
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
        

