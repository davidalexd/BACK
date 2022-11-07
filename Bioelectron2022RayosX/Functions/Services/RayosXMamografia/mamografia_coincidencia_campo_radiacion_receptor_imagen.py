from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def mamografia_coincidencia_campo_radiacion_receptor_imagen(attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    abs = valor_absoluto(int(attribute[3]))

    if(abs<=5 or abs<=-5):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":"El campo de radiación cubre todo el área del detector sobrepasando "+attribute[3]+" mm el lado que corresponde a la pared del tórax",
                "estado":tolerancia
            },
        ]
        ,"tolerancia":"≤±5mm",
        "estado":estado
        }
    

    return resultado