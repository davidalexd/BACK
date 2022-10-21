from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def fluoroscopia_repetibilidad_cai(attribute):
    resultado = [{"resultado":0}]
    desv = desviacion_estandar_m(attribute[0])
    prom = promedio(attribute[0])
    tolerancia = True
    
    if(prom == 0):
        operacion = 0
    else:
        operacion = desv/prom
        
    redondear = round(operacion,2)
    
    if(redondear<=10):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]

    return resultado
