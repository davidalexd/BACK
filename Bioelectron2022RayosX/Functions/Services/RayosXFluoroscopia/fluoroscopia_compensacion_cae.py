from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def fluoroscopia_compensacion_cae(opcion,attribute_1,attribute_2,attribute_3):
    
    try: 
        if(opcion[0]!=None or attribute_1[0]!=None or attribute_2[0]!=None or attribute_3[0]!=None):
            operacion_3 = 0
            prom_3 = promedio([attribute_1[0],attribute_2[0],attribute_3[0]])

                    
            prom_1= promedio([attribute_1[1],attribute_2[1],attribute_3[1]])
            prom_2 = promedio([attribute_1[2],attribute_2[2],attribute_3[2]])

            if(float(attribute_1[0])==0):
                operacion_1 = 0
                operacion_2 = 0
            else:
                operacion_1 = (float(attribute_1[0])-prom_1)/float(attribute_1[0])
                operacion_2 = (float(attribute_1[0])-prom_2)/float(attribute_1[0])


            
            if(opcion[0]=="Medidas Indice de Exposicion"):
                operacion_3 = prom_3-prom_2
            else:
                if(prom_3==0):
                    operacion_3=0
                else:
                    operacion_3 = (prom_3-prom_2)*100/prom_3
                
            redondear_1 = round(operacion_1,2)
            redondear_2 = round(operacion_2,2)
            redondear_3 = round(operacion_3,2)


            abs_1 = valor_absoluto(operacion_1)
            abs_2 = valor_absoluto(operacion_2)
            abs_3 = valor_absoluto(operacion_3)

            if(opcion[0]=="Medidas Indice de Exposicion"):
                tolerancia_a_1 = 0.2
                tolerancia_b_1 = -0.2
                if(abs_1<=tolerancia_a_1 or abs_1<=tolerancia_b_1):
                    tolerancia_1 = True
                else:
                    tolerancia_1  = False
                if(abs_2<=tolerancia_a_1 or abs_2<=tolerancia_b_1):
                    tolerancia_2 = True
                else:
                    tolerancia_2  = False
                if(abs_3<=tolerancia_a_1 or abs_3<=tolerancia_b_1):
                    tolerancia_3 = True
                else:
                    tolerancia_3  = False
            else:
                tolerancia_a_1 = 15
                tolerancia_b_1 = -15
                if(abs_1<=tolerancia_a_1 or abs_1<=tolerancia_b_1):
                    tolerancia_1 = True
                else:
                    tolerancia_1  = False
                if(abs_2<=tolerancia_a_1 or abs_2<=tolerancia_b_1):
                    tolerancia_2 = True
                else:
                    tolerancia_2  = False
                if(abs_3<=tolerancia_a_1 or abs_3<=tolerancia_b_1):
                    tolerancia_3 = True
                else:
                    tolerancia_3  = False

            estado = validacion([tolerancia_1,tolerancia_2,tolerancia_3])

            resultado = {
                "condicion":"",
                "data":[
                    {
                        "parametros":"",
                        "resultado":redondear_1,
                        "estado":tolerancia_1
                    },
                    {
                        "parametros":"",
                        "resultado":redondear_2,
                        "estado":tolerancia_2
                    },
                    {
                        "parametros":"",
                        "resultado":redondear_3,
                        "estado":tolerancia_3
                    }
                ],
                "tolerancia":"Desviación ± "+str(tolerancia_a_1)+"%",
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