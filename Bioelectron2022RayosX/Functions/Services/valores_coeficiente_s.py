def valores_coeficiente_s(opcion):
    if(opcion=="Mo/Mo"):
        return 1
    if(opcion=="Mo/Rh"):
        return 1.017
    if(opcion=="Rh/Rh"):
        return 1.061
    if(opcion=="Rh/Al"):
        return 1.044
    if(opcion=="W/Rh"):
        return 1.042
    if(opcion=="W/Ag"):
        return 1.042
    else:
        return None
