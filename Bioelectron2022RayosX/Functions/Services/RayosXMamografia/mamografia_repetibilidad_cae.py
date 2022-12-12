from Functions.Services.valores_coeficiente_s import valores_coeficiente_s
from Functions.Services.interpolar import interpolar
from Functions.Services.validacion import validacion
from Functions.Services.maxima_desviacion_absoluta_procentual import maxima_desviacion_absoluta_procentual
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.espesor_pmma import espesor_pmma
from Functions.Services.chr_mmal import chr_mmal

def mamografia_repetibilidad_cae(attribute_1,attribute_2,attribute_3,attribute_4,attribute_5,attribute_6,attribute_7,attribute_8,attribute_9):
    try:
        tolerancia_1 = True
        tolerancia_2 = True
        Uc = []
        RSR = []

        for x in range(len(attribute_1)):
            part_1 = float(attribute_1[x])*float(attribute_6[x])
            part_2 = ((float(attribute_2[x]**2)/float(attribute_7[x])**2))
            part_3 = valores_coeficiente_s(attribute_4[0])
            part_4 = interpolar(attribute_5[0],attribute_3[0],espesor_pmma(),chr_mmal()[0],chr_mmal()[1])
            operacion = part_1*part_2*part_3*part_4
            Uc.append(operacion)
        
        devAbsPrc = maxima_desviacion_absoluta_procentual(Uc)
        redondear = round(devAbsPrc,2)

        if(valor_absoluto(devAbsPrc)<=5 or valor_absoluto(devAbsPrc)<=-5):
            tolerancia_1 = True
        else:
            tolerancia_1 = False

        for x in range(len(attribute_8)):
            RSR.append(attribute_8[x]/attribute_9[x])
            
        devAbsPrcRSR = maxima_desviacion_absoluta_procentual(RSR)
        redondearRSR = round(devAbsPrcRSR,2)

        if(valor_absoluto(devAbsPrcRSR)<=5 or valor_absoluto(devAbsPrcRSR)<=-5):
            tolerancia_2 = True
        else:
            tolerancia_2 = False

        estado = validacion([tolerancia_1,tolerancia_2])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":"DG: "+redondear+" %",
                    "estado":tolerancia_1
                },
                            {
                    "parametros":"",
                    "resultado":"RSR: "+redondearRSR+" %",
                    "estado":tolerancia_2
                },
            ]
            ,"tolerancia":"DG: máxima desviación ≤± 5%, RSR: máxima desviación ≤± 5%",
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