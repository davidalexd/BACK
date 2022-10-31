from Functions.Services.valor_absoluto import valor_absoluto


def mamografia_coincidencia_campo_radiacion_receptor_imagen(element=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    
    tolerancia = True
    abs = valor_absoluto(int(element[0]))

    if(abs<=5 or abs<=-5):
        tolerancia = True
    else:
        tolerancia = False


    resultado = {"data":[
        {"parametros":"","resultado":"El campo de radiación cubre todo el área del detector sobrepasando "+abs+" mm el lado que corresponde a la pared del tórax","tolerancia":"≤±5mm","condicion":tolerancia},
        ]
        ,"tolerancia":""}
    

    return resultado