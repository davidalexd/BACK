from Functions.Services.valores_coeficiente_s import valores_coeficiente_s
from Functions.Services.interpolar import interpolar
from Functions.Services.validacion import validacion
from Functions.Services.maxima_desviacion_absoluta_procentual import maxima_desviacion_absoluta_procentual
from Functions.Services.valor_absoluto import valor_absoluto

def mamografia_repetibilidad_cae_valores_dg(attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0],attribute_5=[0],attribute_6=[0],attribute_7=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []

    for x in range(len(attribute_1)):
        part_1 = float(attribute_1[x])*float(attribute_6[x])
        part_2 = ((float(attribute_2[x]**2)/float(attribute_7[x])**2))
        part_3 = valores_coeficiente_s(attribute_4[0])
        part_4 = interpolar(attribute_5[0],attribute_3[0],espesor_pmma(),chr_mmal()[0],chr_mmal()[1])
        operacion = part_1*part_2*part_3*part_4
        Uc.appedn(operacion)
    
    devAbsPrc = maxima_desviacion_absoluta_procentual(Uc)
    redondear = round(devAbsPrc,2)

    if(valor_absoluto(devAbsPrc)<=5 or valor_absoluto(devAbsPrc)<=-5):
        tolerancia = True
    else:
        tolerancia = False

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
        ,"tolerancia":"≤±5%",
        "estado":estado
        }
    

    return resultado