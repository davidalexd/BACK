from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def fluoroscopia_exactitud_tension(attribute_1,attribute_2,attribute_3,attribute_4):
        try:
                prom = promedio(validacion_null_array([attribute_2[1],attribute_3[1],attribute_4[1]]))
                if(float(attribute_1[1])==0):
                        operacion = 0
                else:
                        operacion = ((float(attribute_1[1])-prom)/float(attribute_1[1]))
                tolerancia = True
                tolerancia_1 = 10
                tolerancia_2 = -10
                abs = valor_absoluto(operacion)
                redondear = round(operacion,2)

                if(abs < tolerancia_1 or abs < tolerancia_2):
                        tolerancia = True
                else:
                        tolerancia = False
                
                        
                estado = validacion([tolerancia])

                resultado = {
                        "condicion":str(attribute_1[1])+" kV",
                        "data":[
                                {
                                        "parametros":"",
                                        "resultado":str(redondear)+" %",
                                        "estado":tolerancia
                                }
                        ],
                        "tolerancia":"Desviación con respecto al valor nominal < ±10%",
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