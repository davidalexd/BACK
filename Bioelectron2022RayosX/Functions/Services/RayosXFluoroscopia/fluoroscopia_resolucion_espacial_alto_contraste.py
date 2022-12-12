from Functions.Services.validacion import validacion

def fluoroscopia_resolucion_espacial_alto_contraste(attribute=[0]):
    try: 
        ordenador = [0,1,2,3]
        tolerancia = True
        tolerancias = [0.9,1.12,1.2,1.6]
        Uc = []
        validar = []
        for x in ordenador:
            operacion = float(attribute[x])
            redondear = round(operacion,2)

            if(redondear >= tolerancias[x]):
                tolerancia = True
            else:
                tolerancia = False

            validar.append(tolerancia)

            Uc.append({
                "parametros":"",
                "resultado":redondear+" pl/mm",
                "estado":tolerancia
            })

        estado = validacion(validar)

        resultado = {
            "condicion":"",
            "data":Uc,
            "tolerancia":"Tamaño de campo de 36 cm ≥ 0,9-1 pl/mm; de 30 cm ≥ 1,12 pl/mm; de 23 cm ≥ 1,2 pl/mm; de 15 cm o inferiores ≥ 1,6 pl/mm",
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