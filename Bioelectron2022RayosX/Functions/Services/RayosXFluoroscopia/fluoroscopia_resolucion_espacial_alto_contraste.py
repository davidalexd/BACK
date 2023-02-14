from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def fluoroscopia_resolucion_espacial_alto_contraste(attribute):
    print(attribute,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    try: 
        if (attribute[0]!=None):
            reversed_data = validacion_null_array(attribute)
            # for i in reversed(attribute):
            #     reversed_data.append(i)

            tolerancia = True
            tolerancias = [0.9,1.12,1.2,1.6]
            Uc = []
            validar = []
            for x in range(len(reversed_data)):
                    operacion = float(reversed_data[x])
                    redondear = round(operacion,2)

                    if(redondear >= tolerancias[x]):
                        tolerancia = True
                    else:
                        tolerancia = False

                    validar.append(tolerancia)

                    Uc.append({
                        "parametros":"",
                        "resultado":str(redondear)+" pl/mm",
                        "estado":tolerancia
                    })


            estado = validacion(validar)
            print(estado)

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