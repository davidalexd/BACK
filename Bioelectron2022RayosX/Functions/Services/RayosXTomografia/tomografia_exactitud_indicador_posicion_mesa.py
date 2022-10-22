from Functions.Services.valor_absoluto import valor_absoluto

def tomografia_exactitud_indicador_posicion_mesa(element_1=[0],element_2=[0],element_3=[0]):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    tolerancia =True
    abs = valor_absoluto(float(element_1[0])-float(element_3[0]))
    operacion = float(element_2[0])-abs

    redondear = round(operacion,2)
    
    if(redondear <= 2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado