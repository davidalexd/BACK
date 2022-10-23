from Functions.Services.valor_absoluto import valor_absoluto

def tomografia_perfiles_sensibilidad(attribute_1=[0],attribute_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    tolerancia_1 = 1
    tolerancia_2 = -1
    Uc = []
    
    for x in range(len(attribute_1)):
        operacion = float(attribute_1[x])-float(attribute_2[x])
        abs = valor_absoluto(operacion)
        redondear = round(abs,2)


        if(redondear <= tolerancia_1 or redondear <= tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False
        
        Uc.append({
            "parametros":"",
            "resultado":redondear,
            "condicion":tolerancia
        })
    
    resultado = {"data":Uc,"tolerancia":"En modo axial EM – EN ≤ ±1 mm, para EN ≥ 2mm y EM – EN ≤ 50%, para EN < 2mm. En modo helicoidal según especificaciones de fabricante del fabricante y < ±1 mm del valor de referencia"}
    
    return resultado