with open ("napisy.txt") as plik:
    dane = plik.read()
    lista = dane.split("\n")

    # zad a
    suma = 0
    for i in lista:
        for j in i.split(" "):
            if len(j) % 2 == 0:
                suma = suma + 1
    print("Liczba napisów o parzystej długości: ", suma)

    #zad b
    sumab = 0;
    for i in lista:
        for j in i.split(" "):
            if j.count("0") == j.count("0") & j.count("1") == j.count("1"):
                sumab = sumab + 1
    print("Liczba napisów zawierające taką samą ilość zer i jedynek: ", sumab)

    #zad c
    sumaZera = 0
    sumaJeden = 0
    for i in lista:
        for j in i.split(" "):
            if j.count("1") == 0:
                sumaZera = sumaZera + 1
            elif j.count("0") == 0:
                sumaJeden = sumaJeden + 1
    print("Liczba napisów posiadające same zera: ", sumaZera)
    print("Liczba napisów posiadające same jedynki: ", sumaJeden)

    #zad d
    sumad = 0
    for i in lista:
        for j in i.split(" "):
            if j.endswith("1"):
                sumad = sumad + 1
    print("Liczba napisów kończących się jedynką: ",sumad)

    #zad f
    suma2 = 0
    suma3 = 0
    suma4 = 0
    suma5 = 0
    suma6 = 0
    suma7 = 0
    suma8 = 0
    suma9 = 0
    suma10 = 0
    suma11 = 0
    suma12 = 0
    suma13 = 0
    suma14 = 0
    suma15 = 0
    suma16 = 0
    suma17 = 0
    for i in lista:
        for j in i.split(" "):
            if len(j) == 2:
                suma2 = suma2 + 1
            elif len(j) == 3:
                suma3 = suma3 + 1
            elif len(j) == 4:
                suma4 = suma4+1
            elif len(j) == 5:
                suma5 = suma5+1
            elif len(j) == 6:
                suma6 = suma6 + 1
            elif len(j) == 7:
                suma7 = suma7+1
            elif len(j) == 8:
                suma8 = suma8+1
            elif len(j) == 9:
                suma9 = suma9 + 1
            elif len(j) == 10:
                suma10 = suma10+1
            elif len(j) == 11:
                suma11 = suma11+1
            elif len(j) == 12:
                suma12 = suma12+1
            elif len(j) == 13:
                suma13 = suma13 + 1
            elif len(j) == 14:
                suma14 = suma14+1
            elif len(j) == 15:
                suma15 = suma15+1
            elif len(j) == 16:
                suma16 = suma16 + 1
    print("2: ",suma2)
    print("3: ",suma3)
    print("4: ",suma4)
    print("5: ",suma5)
    print("6: ",suma6)
    print("7: ",suma7)
    print("8: ",suma8)
    print("9: ",suma9)
    print("10: ",suma10)
    print("11: ",suma11)
    print("12: ",suma12)
    print("13: ",suma13)
    print("14: ", suma14)
    print("15: ",suma15)
    print("16: ",suma16)