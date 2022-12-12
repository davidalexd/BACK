from Functions.Services.validacion import validacion
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.mediciones import mediciones
from Functions.Services.raiz import raiz

def mamografia_compensacion_cae_espesor_composición_mama(element_1,element_2,attribute,attribute_1,attribute_2,attribute_3,attribute_4):
    try:
        tolerancia = True
        Uc = []
        validar = []
        for x in range(len(attribute_1)):
            abs_1 = valor_absoluto(attribute_1[x])
            abs_2 = valor_absoluto(attribute_3[x])
            part_1 = (abs_1-abs_2)
            part_2 = raiz(((attribute_2[x]**2)+(attribute_4[x]**2))/2,2)

            operacion = (float(element_1[0])*part_1/part_2)/float(element_2[0])

            tolerancia_valor = mediciones(attribute[x])
            
            if(operacion < tolerancia_valor):
                tolerancia = True
            else:
                tolerancia = False

            validar.append(tolerancia)

            Uc.append({
                "parametros":"",
                "resultado":str(tolerancia_valor)+" %",
                "estado":tolerancia
            })
        
        estado = validacion(validar)

        resultado = {
            "condicion":"",
            "data":Uc,
            "tolerancia":"Para cada espesor, desviación entre la RCR medida y la obtenida en las pruebas iniciales < 10%.",
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