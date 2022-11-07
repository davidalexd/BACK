from Functions.Services.validacion import validacion

def fluoroscopia_alineacion_rayos_x_haz_luminoso(attribute=[0],element=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
    parametro = ["L1 - "+str(attribute[0])+"% , L2 - "+str(attribute[1])+"%, L3 - "+str(attribute[2])+"% , L4 - "+str(attribute[3])+"%"]
    variante = element[0]
    operacion = sum(attribute)
    redondear = round(operacion,2)
    tolerancia = True
    tolerancia_1 = (3*float(variante)/100)
    tolerancia_2 = (2*float(variante)/100)
    if (redondear <= tolerancia_1 and redondear <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":str(variante)+" cm al foco",
        "data":[
            {
                "parametros":parametro,
                "resultado":"Suma total = "+str(redondear)+"cm",
                "estado":tolerancia
                }
        ],
        "tolerancia":"Suma de las desviaciones en los bordes inferiores 2.0% de la distancia entre el foco y el maniquí de colimación para cada dirección principal. La suma total de las desviaciones no excederá el 3% de la distancia entre el foco y el maniquí de colimación.",
        "estado":estado
        }
        
    return resultado