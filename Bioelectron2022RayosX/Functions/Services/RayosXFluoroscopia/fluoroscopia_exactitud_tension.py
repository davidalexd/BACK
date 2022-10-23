from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
def fluoroscopia_exactitud_tension(attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0]):
        resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
        prom = promedio([attribute_2[1],attribute_3[1],attribute_4[1]])
        operacion = ((float(attribute_1[1])-prom)/float(attribute_1[1]))*100
        tolerancia = True
        tolerancia_1 = 10
        tolerancia_2 = -10
        abs = valor_absoluto(operacion)
        redondear = round(abs,2)

        if(redondear < tolerancia_1 or redondear < tolerancia_2):
                tolerancia = True
        else:
                tolerancia = False
        
        resultado = {"data":[
                {"parametros":"","resultado":redondear,"condicion":tolerancia}
        ],"tolerancia":"Desviación con respecto al valor nominal < ±10%"}

        return resultado