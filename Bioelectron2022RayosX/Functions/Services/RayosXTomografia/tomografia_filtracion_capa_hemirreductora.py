from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def tomografia_filtracion_capa_hemirreductora(attribute=[0],element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    tolerancia = True
    operacion = float(element_1[0])-prom-float(element_2[0])
    redondear = round(operacion,2)
    tolerancia_1 = 1
    tolerancia_2 = -1

    if (valor_absoluto([redondear]) <= tolerancia_1 or valor_absoluto([redondear]) <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":["Valor medido (VM): 6.3 mmAl a 120 kV ","Valor nominal (VN): 6.3 mmAl a 120 kV"],
                "resultado":"VM - VN = "+redondear+" mmAl",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Según especificaciones del fabricante: (VM – VN) ≤ ±1 mmAl  ",
        "estado":estado
        }
    
    return resultado
