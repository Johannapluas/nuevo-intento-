op = 1
valor = 0
victorias = derrotas = empates = 0; 

while op != 0:
    print('<1> Jugar')
    print('<2> Resultados')
    print('<0> Salir')

    op = int(input('Ingrese opcion: '))

    if op == 1:

        while valor<1 or valor>3:
            valor = int(input('Ingrese valor: 1. piedra, 2. papel, 3. tijera: '))
        
        num = random.randint(1, 3)

        if valor == num:
            print('Empate: ', valor, ' vs ', num)
            empates += 1
        elif valor == 1:
            if num == 2:
                print('Pierdo: ', valor, ' vs ', num)
                derrotas += 1
            elif num == 3:
                print('Gano: ', valor, ' vs ', num)
                victorias += 1
        elif valor == 2:
            if num == 1:
                print('Gano: ', valor, ' vs ', num)
                victorias += 1
            elif num == 3:
                print('Pierdo: ', valor, ' vs ', num)
                derrotas += 1
        elif valor == 3:
            if num == 1:
                print('Pierdo: ', valor, ' vs ', num)
                derrotas += 1
            elif num == 2:
                print('Gano: ', valor, ' vs ', num)
                victorias += 1
    elif op == 2:
        print('Empates:', empates)
        print('Victorias:', victorias)
        print('Derrotas:', derrotas)
        


        # while valor != 1 and valor!=2 and valor!=3:
        #     valor = int(input('Ingrese valor: 1. piedra, 2. papel, 3. tijera: '))
        
        # while not(valor == 1 or valor == 2 or valor == 3):
        #     valor = int(input('Ingrese valor: 1. piedra, 2. papel, 3. tijera: '))
        
        # while not(valor>=1 and valor<=3):
        #     valor = int(input('Ingrese valor: 1. piedra, 2. papel, 3. tijera: '))