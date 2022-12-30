from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def tomografia_perfiles_sensibilidad(attribute_1,attribute_2):
    try:
        tolerancia_1 = 1
        tolerancia_2 = -1
        Uc = []
        validar = []
        for x in range(len(attribute_1)):
            operacion = float(attribute_1[x])-float(attribute_2[x])
            abs = valor_absoluto(operacion)
            redondear = round(abs,2)


            if(redondear <= tolerancia_1 or redondear <= tolerancia_2):
                tolerancia = True
            else:
                tolerancia = False

            validar.append(tolerancia)
            
            Uc.append({
                "parametros":["Espesor de corte medido (EM):"+str(attribute_1[x]),"Espesor de corte medido (EM):"+str(attribute_2[x])],
                "resultado":"EM – EN = "+str(redondear)+" mm",
                "estado":tolerancia
            })
        
        estado = validacion(validar)

        resultado = {
            "condicion":"Modo Axial",
            "data":Uc,
            "tolerancia":"En modo axial EM – EN ≤ ±1 mm, para EN ≥ 2mm y EM – EN ≤ 50%, para EN < 2mm. En modo helicoidal según especificaciones de fabricante del fabricante y < ±1 mm del valor de referencia",
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