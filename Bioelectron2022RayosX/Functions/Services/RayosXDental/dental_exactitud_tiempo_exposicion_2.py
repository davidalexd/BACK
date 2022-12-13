from Functions.Services.validacion import validacion

def dental_exactitud_tiempo_exposicion_2(element_1,element_2,opcion):
    try:
        # llama a TIEMPO DE EXPOSICIÓN (s) y luego a TIEMPO (s) in range 1
        resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
        element_a = float(element_1[0])
        element_b = float(element_2[0])

        operacion = ((element_a-element_b)/element_a)*100
        redondeo = round(operacion,2)
        tolerancia = True

        if(opcion[0]=="EQUIPO MONOFÁSICO"):
            tolerancia_1 = 20
            tolerancia_2 = -20
            if (redondeo <= tolerancia_1 or redondeo <=tolerancia_2):
                tolerancia = True
            else:
                tolerancia = False
        else:
            tolerancia_1 = 10
            tolerancia_2 = -10
            if (redondeo <= tolerancia_1 or redondeo <=tolerancia_2):
                tolerancia = True
            else:
                tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"Tiempo "+str(element_1)+" s",
            "data":[
                {
                    "parametros":"",
                    "resultado":"Desviación "+str(redondeo)+"%",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Desviación ≤± "+str(tolerancia_1)+"% ",
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