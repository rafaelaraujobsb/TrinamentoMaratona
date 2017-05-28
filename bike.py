casos = input()
turistas = input()
assentos = input()
for teste in casos:
    assentos = assentos -1
    lugares = turista%assentos
    if lugares == 0:
        lugares = turistas/assentos
    else:
        lugares = turistas/assentos
        lugares = int(lugares) + 1
    print("Caso "+teste+": " +lugares)
        
            
