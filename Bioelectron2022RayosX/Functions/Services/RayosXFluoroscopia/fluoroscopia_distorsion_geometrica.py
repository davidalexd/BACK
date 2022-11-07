from Functions.Services.validacion import validacion

def fluoroscopia_distorsion_integral(element_1=[0],element_2=[0],element_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

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

def fluoroscopia_distorsion_del_tipo_s(opcion=[""]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
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

def fluoroscopia_distorsion_cojinete(opcion=[""]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
    reslt = "ACEPTABLE"
    tolerancia = True

    if(opcion[0]=="Si"):
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