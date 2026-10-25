###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
numero = 1
suma = 0
while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(suma)
# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
numero = int(input("Introdueix un número enter positiu: "))
factorial = 1
i = 1
while i <= numero:
    factorial *= i
    i += 1
print(f"El factorial de {numero} és {factorial}")
# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
while True:
    contrasenya = input("Introdueix una contrasenya (almenys 8 caràcters): ")
    if len(contrasenya) >= 8:
        print("Contrasenya vàlida")
        break
    else:
        print("Contrasenya massa curta. Torna-ho a provar.")
# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero = int(input("Introdueix un número per veure la seva taula de multiplicar: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
numero = int(input("Introdueix un número enter positiu N: "))
i = 2
while i <= numero:
    es_primer = True
    j = 2
    while j < i:
        if i % j == 0:
            es_primer = False
            break
        j += 1
    if es_primer:
        print(i)
    i += 1
# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
suma = 0
while True:
    numero = int(input("Introdueix un número enter (0 per acabar): "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total és: {suma}")
# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
numero = int(input("Introdueix un numero enter positiu: "))
comptador = 0
while numero > 0:
    numero //= 10
    comptador += 1
print(f"Nombre de xifres: {comptador}")
# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
numero_termes = int(input("Quants termes de la seqüència de Fibonacci vols veure? "))
a, b = 0, 1
comptador = 0
while comptador < numero_termes:
    print(a)
    a, b = b, a + b
    comptador += 1
# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
numero_secret = 7
while True:
    intent = int(input("Endevina el número secret (entre 1 i 10): "))
    if intent == numero_secret:
        print("Enhorabona! Has endevinat el número secret.")
        break
    elif intent < numero_secret:
        print("El número secret és més gran.")
    else:
        print("El número secret és més petit.")