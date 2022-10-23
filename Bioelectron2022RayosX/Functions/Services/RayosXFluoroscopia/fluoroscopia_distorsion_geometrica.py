



def fluoroscopia_distorsion_integral(element_1=[0],element_2=[0],element_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    div = ((float(element_1[0])/(float(element_2[0])*float(element_3[0])))-1)*100
    redondear = round(div,2)
    tolerancia = true

    if(redondear<=10):
        tolerancia = true
    else:
        tolerancia = false

    resultado = {"data":[
            {
                "parametros":"",
                "resultado":str(redondear)+'%',
                "condicion":tolerancia
            }
            ],
            "tolerancia":"≤10%"
        }
    return resultado

def fluoroscopia_distorsion_del_tipo_s(opcion=[""]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
    reslt = "ACEPTABLE"
    tolerancia = true

    if(opcion[0]=="No Existe"):
        tolerancia = true
        reslt = "ACEPTABLE"
    else:
        tolerancia = false
        reslt = "NO ACEPTABLE"

    resultado = {"data":[
            {
                "parametros":"",
                "resultado":reslt,
                "condicion":tolerancia
            }
            ],
            "tolerancia":reslt
        }

    return resultado

def fluoroscopia_distorsion_cojinete(opcion=[""]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
    reslt = "ACEPTABLE"
    tolerancia = true

    if(opcion[0]=="Si"):
        tolerancia = true
        reslt = "ACEPTABLE"
    else:
        tolerancia = false
        reslt = "NO ACEPTABLE"

    resultado = {"data":[
            {
                "parametros":"",
                "resultado":reslt,
                "condicion":tolerancia
            }
            ],
            "tolerancia":reslt
        }

    return resultado