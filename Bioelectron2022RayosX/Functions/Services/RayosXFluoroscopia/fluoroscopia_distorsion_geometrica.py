from Functions.Services.validacion import validacion

def fluoroscopia_distorsion_integral(element_1,element_2,element_3):
    try:
        if(float(element_2[0])*float(element_3[0]) == 0 ):
            div = 0
        else:
            div = ((float(element_1[0])/(float(element_2[0])*float(element_3[0])))-1)*100
            
        redondear = round(div,2)
        tolerancia = True

        if(redondear<=10):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])


        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+'%',
                    "estado":tolerancia
                }
            ],
            "tolerancia":"≤10%",
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

def fluoroscopia_distorsion_del_tipo_s(opcion):
    try:
        reslt = "ACEPTABLE"
        tolerancia = True

        if(opcion[0]=="No Existe"):
            tolerancia = True
            reslt = "ACEPTABLE"
        else:
            tolerancia = False
            reslt = "NO ACEPTABLE"

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":reslt,
                    "estado":tolerancia
                }
            ],
                "tolerancia":"Aceptable",
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

def fluoroscopia_distorsion_cojinete(opcion):
    try:
        reslt = "ACEPTABLE"
        tolerancia = True

        if(opcion[0]=="No"):
            tolerancia = True
            reslt = "ACEPTABLE"
        else:
            tolerancia = False
            reslt = "NO ACEPTABLE"

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":reslt,
                    "estado":tolerancia
                }
            ],
                "tolerancia":"Aceptable",
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