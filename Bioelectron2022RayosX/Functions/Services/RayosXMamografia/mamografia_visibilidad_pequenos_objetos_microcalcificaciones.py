from Functions.Services.suma_range import suma_range
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion

def mamografia_visibilidad_pequenos_objetos_microcalcificaciones(element=[0],element_1=[0],element_2=[0],element_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    suma = suma_range([element_1[0],element_2[0],element_3[0]])

    operacion = desviacion_estandar_m([element[0],suma])

    if(operacion<=10,operacion<=-10):
        tolerancia = True
    else:
        tolerancia = False

    redondear = round(operacion,2)
    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":redondear+" %",
                "estado":tolerancia
            },
        ]
        ,"tolerancia":"Desviación con respecto al valor de referencia: ≤±10%",
        "estado":estado
        }
    

    return resultado