casos = input()
for caso in range(int(casos)):
    resp = []
    existe =False
    lista = input().split()
    numeroCandidatos = int(lista[0])
    notaCorte = int(lista[1])
    vagas = lista[2]
    notas = input().split()
    aprovados = int(0)
    for nota in notas:
        if int(nota) >= notaCorte:
            aprovados = aprovados + 1
            existe = True
    notas.sort()
    notas.reverse()
    if existe == False:
        notas.sort()
        notas.reverse()
        resp.append(notas[0]) 
    else:
        for v in range(int(vagas)):
            resp.append(notas[v])
        resp.reverse()
    print("Caso "+str(caso + 1)+": "+str(aprovados)+" "+str(resp[0]))
    
                
