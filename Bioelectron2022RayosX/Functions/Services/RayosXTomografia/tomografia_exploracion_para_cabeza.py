from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion


def tomografia_exploracion_para_cabeza(element,element_1,element_2,attribute,attribute_1,attribute_2,attribute_3,attribute_4,element_3,element_4,element_5,element_6,opcion,element_7):
    # element = Tensión Kv
    # element_1 = Fc exploración de cabeza
    # element_2 = Espesor de corte (mm)    
    # attribute = dosis Central range 3
    # attribute_1 = dosis periferia L1 range 3
    # attribute_2 = dosis periferia L2 range 3
    # attribute_3 = dosis periferia L3 range 3
    # attribute_4 = dosis periferia L4 range 3
    # element_3 = Corriente (mA) 
    # element_4 = tiempo por rotacion (seg) 
    # element_5 = 'Numero de Cortes por rotacion:
    # element_6 = Longitud irradiada (mm):
    # opcion = tipo se exploracion
    # element_7 = Pich
    try:
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
            "tolerancia":"< 60 mGy. (Exploración: Cabeza adulto)",
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

