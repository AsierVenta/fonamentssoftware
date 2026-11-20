# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Barcelona", "Madrid", "València", "Sevilla", "Bilbao")
print(ciutats[1])
print(ciutats[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantas vegades apareix el número 3 a la tupla.
numeros = (1, 2, 3, 4, 3, 5, 3)
comptador = numeros.count(3)
print(f"El número 3 apareix {comptador} vegades.")

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla):
    return tuple(sorted(tupla))
print(ordenar_tupla((5, 2, 9, 1, 5, 6)))