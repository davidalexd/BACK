from Functions.Services.promedio import promedio


def tomografia_exploracion_para_cabeza(element_1=[0],element_2=[0],attribute=[0],attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0],element_3=[0],element_4=[0],element_5=[0],element_6=[0],opcion=[""],element_7=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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


    resultado = {"data":[{"parametros":"","resultado":redondear,"condicion":tolerancia}],"tolerancia":"< 60 mGy. (Exploración: Cabeza adulto)"}

    return resultado



