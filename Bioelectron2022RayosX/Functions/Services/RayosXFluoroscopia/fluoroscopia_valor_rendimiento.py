from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def fluoroscopia_valor_rendimiento(element_1,attribute_1,attribute_2,attribute_3,attribute_4):
        try:
                tolerancia = True
                prom = promedio([attribute_2[0],attribute_3[0],attribute_4[0]])
                operacion = ((prom)*(float(element_1[0])**2))/float(attribute_1[0])
                redondear = round(operacion,2)
                abs = valor_absoluto(redondear)
                

                if(float(attribute_2[0])>=2.5 and float(attribute_2[0])<5):
                        if(redondear<=65 and redondear>=30):
                                tolerancia = True
                        else:
                                tolerancia = False
                else:
                        if(abs<25):
                                tolerancia = True
                        else:
                                tolerancia = False

                estado = validacion([tolerancia])         

                resultado = {
                        "condicion":"",
                        "data":[
                                {
                                        "parametros":"",
                                        "resultado":str(redondear)+" %",
                                        "estado":tolerancia
                                }
                        ],
                        "tolerancia":"A 80 kV y con una filtración estimada entre 2.5 y 5 mmAl, el rendimiento estará entre 30 y 65 µGy/mAs a 1 m del foco. En los equipos con filtración superior a 5 mm Al se tendrá en cuenta las especificaciones del fabricante.",
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