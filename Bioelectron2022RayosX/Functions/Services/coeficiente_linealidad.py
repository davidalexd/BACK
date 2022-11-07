def coeficiente_linealidad(attribute):
    if(attribute[0] < attribute[-1]):
        return (attribute[-1] - attribute[0]) / (attribute[0] + attribute[-1])
    else:
        return (attribute[0] - attribute[-1]) / (attribute[0] + attribute[-1])

