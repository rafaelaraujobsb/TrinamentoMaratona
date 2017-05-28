casos = input()
for caso in range(int(casos)):
    vMensal = input()
    ids = input().split()
    resposta = []
    resposta.append(ids[0])
    cont = 1
    for conte in ids:
        existe = False
        for  resp in resposta:
            if conte == resp:
                existe = True        
        if existe == False:
            resposta.append(conte)
            cont = cont + 1
    print("Caso "+str(caso + 1)+": "+str(cont))
