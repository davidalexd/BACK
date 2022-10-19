from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.RayosXDental.dental_valor_rendimiento import dental_valor_rendimiento
def dental_repetibilidad_rendimiento(attribute,element_1,element_2,element_3):
    dvr = dental_valor_rendimiento(attribute,element_1,element_2,element_3)[0]["resultado"]

    desvm = desviacion_estandar_m(attribute)
    variante_1 = float(element_1[0])*2

    operacion = (desvm*variante_1)/dvr

    redondeo = round(operacion,2)

    tolerancia = True

    if(redondeo < 10):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondeo)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado