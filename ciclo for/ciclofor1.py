# El ciclo for ejecuta un bloque de código repetidamente hasta 
# que la condición en el ciclo for no sea válida

mascotas = ['gatos', 'perros', 'gatos', 'peces', 'perros', 'perros']

for mascota in mascotas:
    print(mascota)

contador_gatos = 0
contador_perros = 0
contador_peces = 0

for mascota in mascotas:
    if mascota == "gatos":
        contador_gatos = contador_gatos + 1
    elif mascota == "perros":
        contador_perros = contador_perros + 1
    elif mascota == "peces":
        contador_peces = contador_peces + 1

print("El número de gatos es:", contador_gatos)
print("El número de perros es:", contador_perros)
print("El número de peces es:", contador_peces)


for mascota in mascotas:
    if mascota == "gatos":
        contador_gatos = contador_gatos + 1

for mascota in mascotas:
    if mascota == "perros":
        contador_perros = contador_perros + 1

for mascota in mascotas:
    if mascota == "peces":
        contador_peces = contador_peces + 1