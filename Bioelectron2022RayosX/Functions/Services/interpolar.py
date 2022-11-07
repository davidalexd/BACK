def interpolar(element_1,element_2,attributes_1,attributes_2,attributes_3):
    nElementos_X = len(attributes_1)
    nElementos_Y = len(attributes_2)
    for x in range(nElementos_X):
        for y in range(nElementos_Y):
            if (element_1 == attributes_1[x] and element_2 == attributes_2[y]):
                matriz_resultado=(attributes_3[x:y])

            if (element_2 == attributes_2[y] and element_1 > attributes_1[x] and attributes_1[x] < attributes_1[y + 1]):
                ax = attributes_1[x]
                bx = attributes_1[x + 1]
                m = matriz_resultado[x:y]
                n = matriz_resultado[x+1:y]
                x = element_1
                y = element_2
                return (m + (((x - ax) / (bx - ax)) * (n - m)))

            if (element_1 == attributes_1[x] and element_2 > attributes_2[x] and element_2 < attributes_2[y + 1]):
                ax = attributes_2[y]
                bx = attributes_2[y + 1]
                m = matriz_resultado[x,y]
                n = matriz_resultado[x,y+1]
                x = element_1
                y = element_2
                return (m + (((y - ay) / (by - ay)) * (n - m)))

            if (element_1 > attributes_1[x] and element_1 > attributes_1[x+1] and element_2 < attributes_2[y] and element_2 < attributes_2[y + 1]):
                ax = attributes_1[x]
                bx = attributes_1[x + 1]
                ay = attributes_2[y]
                by = attributes_2[y + 1]
                m = matriz_resultado[x,y]
                m2 = matriz_resultado[x + 1, y]
                n = matriz_resultado[x,y+1]
                n2 = matriz_resultado[x+1,y+1]
                x = element_1
                y = element_2
                int1 = m + (((y - ay) / (by - ay)) * (n - m))
                int2 = m2 + (((y - ay) / (by - ay)) * (n2 - m2))
                return (int1 + (((x - ax) / (bx - ax)) * (int2 - int1)))