

def fluoroscopia_distorsion_geometrica(element_1,element_2,element_3):
    resultado = [{"resultado":0}]
    div = ((float(element_1[0])/(float(element_2[0])*float(element_3[0])))-1)*100
    redondear = round(div,2)
    resultado = [{"resultado":str(redondear)+'%',"decorador":"%"}]
    return resultado