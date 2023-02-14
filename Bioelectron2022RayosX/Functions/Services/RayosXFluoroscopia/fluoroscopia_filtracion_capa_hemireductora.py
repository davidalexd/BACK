from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def fluoroscopia_filtracion_capa_hemireductora(element,attributes):
        try:    
                resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

                prom = promedio(validacion_null_array(attributes))
                redondear = round(prom,2)
                tolerancia=True
                tolerancia_1=2.9

                if(float(element[0])==70):
                        tolerancia_1=2.5
                else:
                        tolerancia_1=2.9

                if(redondear>tolerancia_1):
                        tolerancia=True
                else:
                        tolerancia=False
                        
                        
                estado = validacion([tolerancia])
                resultado = {
                        "condicion":"",
                        "data":[
                                {
                                        "parametros":"",
                                        "resultado":str(redondear)+" mmAl",
                                        "estado":tolerancia
                                }
                        ],
                                "tolerancia":"> 2.5 mmAl (a 70 kVp) y >2.9 mmAl (a 80 kVp)",
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