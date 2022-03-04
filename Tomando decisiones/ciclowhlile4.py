d = 0
m = 0
a = 0

s_d = 0
s_m = 0
s_a = 0

m31 = (1,3,5,7,8,10)
m30 = (4,6,9,11)

while True:
    print("INGRESA UNA FECHA")
    print("Dia: ", end = " ")
    d = int(input())
    print("Mes: ", end = " ")
    m = int(input())
    print("Año: ", end = " ")
    a = int(input())

    s_d = d + 1
    s_m = m

    if m == 12 and d == 31:
        s_d = 1
        s_m = 1
        s_a = a + 1
    else:
        s_a = a

    for i in range(len(m31)):
            if d == 31 and m == m31[i]:
                s_d = 1
                s_m = m + 1

    for i in range(len(m30)):
        if d == 30 and m == m[i]:
            s_d = 1
            s_d = m + 1

    if m == 2 and d == 28:
        s_d = 1
        s_m = m + 1
    a_b = a % 4

    if d == 29 and m == 2 and a_b == 0:
        s_d = 1
        s_m = m + 1

    if d >= 32 or m >= 13:
        print("Ingresaste una fecha INVALIDA, porfavor escribe una fecha nuevamente")
    else:
        print("Dia Ingresado: ", d, "/", m, "/", a)
        print("Siguiente dia: ", s_d, "/", s_m, "/", s_a)