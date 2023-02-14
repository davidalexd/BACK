from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array
def fluoroscopia_umbral_sensibilidad_bajo_contraste(attribute_1,attribute_2):
    try:
        if (attribute_1[0]!=None or attribute_2[0]!=None):
            tolerancia = True
            tolerancias = [4,3.5,2.7,1.9]
            Uc = []
            validar = []
            attribute_1 = validacion_null_array(attribute_1)
            for x in range(len(attribute_1)):
                    if(float(attribute_2[x])==0):
                        operacion = 0
                    else:  
                        operacion = float(attribute_1[x])/float(attribute_2[x])
                    redondear = round(operacion,2)

                    
                    if(redondear <= tolerancias[x]):
                        tolerancia = True
                    else:
                        tolerancia = False

                    validar.append(tolerancia)

                    Uc.append({
                        "parametros":"",
                        "resultado":str(redondear)+" %",
                        "estado":tolerancia
                    })
            
            estado = validacion(validar)
            resultado = {
                "condicion":"",
                "data":Uc,
                "tolerancia":"Tamaño de campo de 36 cm ≤ 4%, de 30 cm ≤ 3.5%, de 23 cm ≤ 2.7%, de 15 cm o inferiores ≤ 1.9%",
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
    
