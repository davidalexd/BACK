def constantes_calculo_tolerancia_chr(element):
    if(element == "Mo/Mo"):
        return 0.12
    if(element == "Mo/Rh"):
        return 0.19
    if(element == "Rh/Rh"):
        return 0.22
    if(element == "W/Rh"):
        return 0.30
    if(element == "W/Ag"):
        return 0.32
    if(element == "W/Al"):
        return 0.25
    else:
        return None
