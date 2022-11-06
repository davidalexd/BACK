from Functions.Services.promedio import promedio

from Functions.Services.validacion import validacion


def tomografia_exploracion_para_abdomen(element=[0],element_1=[0],element_2=[0],attribute=[0],attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0],element_3=[0],element_4=[0],element_5=[0],element_6=[0],opcion=[""],element_7=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
    kv = element[0]

    CDTIC = promedio(attribute)*100*float(element_1[0])/float(element_2[0])

    CDTIP = promedio(attribute_1+attribute_2+attribute_3+attribute_4)*100*float(element_1[0])/float(element_2[0])

    CTDIW = (1*(float(element_3[0])*float(element_4[0])))*((CDTIC/3)+(2*CDTIP)/3)

    CargaCorte = float(element_3[0])*float(element_4[0])/float(element_5[0])

    if(opcion[0] == "Axial"):
        CTDIVOL = (CTDIW*CargaCorte)/(float(element_6[0])/(float(element_2[0])*float(element_5[0])))
    else:
        CTDIVOL = (CTDIW*CargaCorte)/float(element_7[0])

    redondear = round(CTDIVOL,2)
    tolerancia = True

    if(redondear < 60):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"Modo Helicoidal / "+kv+" kV / "+element_3[0]+" mAs / "+element_2[0]+" mm de espesor de corte",
        "data":[
            {
                "parametros":"",
                "resultado":redondear+" mGy",
                "estado":tolerancia
            }
        ],
        "tolerancia":"< 30 mGy. (Exploración: Abdomen adulto)",
        "estado":estado
        }
    
    return resultado