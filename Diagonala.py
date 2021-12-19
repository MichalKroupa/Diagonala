# Projekt na vytváření dvourozměrného pole a nulování hlavní a vedlejší diagonály 
import random
# Deklarace pole (listu)
pole = []

# Naplnění dvourozměrného pole náhodnými hodnotami
for i in range(4):
    temp = []
    for j in range(4):
        temp.append(random.randint(1, 9))
    pole.append(temp)

# Výpis pole
for prvek in pole:
    print(prvek, end="\n")

input("stisknutim libovolne klavesy vynulujete hlavni diagonalu")

# Cyklus který vynuluje hlavní diagonálu
for i in range(4):
    for j in range(4):
        # pokud se indexy rovnají, jde o hlavní diagonálu
        if i == j:
            pole[i][j] = 0

# Výpis pole
for prvek in pole:
    print(prvek, end="\n")

input("stisknutim libovolne klavesy vynulujete vedlejsi diagonalu")

#Cyklus který vynuluje vedlejší diagonálu
for i in range(4):
    # i musí označovat číslo řádku, k používáme jako pomocnou proměnnou pro poslední index, který postupně snižujeme
    k = 3-i
    for j in range(4):
        # Pokud se sloupec a poslední pozice shodují, od k odečteme 1, aby se na dalším řádku vynulovala hodnota o sloupec vedle
        if j == k:
            k = k-1
            pole[i][j] = 0
#Výpis pole
for prvek in pole:
    print(prvek, end="\n")