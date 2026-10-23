###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))
if num1 > num2:
    print(f"El primer nombre ({num1}) és més gran que el segon nombre ({num2}).")
elif num2 > num1:
    print(f"El segon nombre ({num2}) és més gran que el primer nombre ({num1}).")
else:
    print(f"Els dos nombres són iguals ({num1}).")
# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))
print("Introdueix l'operació (+, -, *, /): ")
operacio = input()
if operacio == "+":
    resultat = num1 + num2
    print(f"El resultat de {num1} + {num2} és {resultat}.")
elif operacio == "-":
    resultat = num1 - num2
    print(f"El resultat de {num1} - {num2} és {resultat}.")
elif operacio == "*":
    resultat = num1 * num2
    print(f"El resultat de {num1} * {num2} és {resultat}.")
elif operacio == "/":
    if num2 == 0:
        print("Error: No es pot dividir per zero.")
    else:
        resultat = num1 / num2
        print(f"El resultat de {num1} / {num2} és {resultat}.")
# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
any = int(input("Introdueix un any: "))
if any % 4 == 0 and (any % 100 != 0 or any % 400 == 0):
    print(f"L'any {any} és de traspàs.")
else:
    print(f"L'any {any} no és de traspàs.")
# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
edat = int(input("Introdueix una edat: "))
if edat >= 0 and edat <= 2:
    print("Nadó")
if edat >= 3 and edat <= 12:
    print("Infant")
if edat >= 13 and edat <= 17:
    print("Adolescent")
if edat >= 18 and edat <= 64:
    print("Adult")
if edat >= 65:
    print("Persona gran")
else:
    print("Introdueix una edat valida: ")
# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
senyal = int(input("Introdueix el nivell de senyal Wi-Fi (RSSI) en dBm: "))
if senyal >= -50:
    print("Cobertura excel·lent")
elif senyal >= -67:
    print("Cobertura bona")
elif senyal >= -75:
    print("Cobertura feble")
elif senyal < -75:
    print("Cobertura molt feble")
# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia = float(input("Introdueix la potència òptica rebuda en dBm: "))
if potencia >= -27 and potencia <= -8:
    print("El nivell de potència és acceptable")
elif potencia < -27:
    print("El nivell de potència és massa baix")
elif potencia > -8:
    print("El nivell de potència és massa alt")
else:
    print("Introdueix un nombre vàlid")
# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
pla = 20
consum = int(input("Introdueix el consum de dades en GB: "))
if consum > pla:
    print("S'ha superat el límit permès")
elif consum < pla:
    print("El consum està dins del límit")
# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
LOS = bool(input("Terminal òptic encès?: "))
Internet = bool(input("Indicador d'Internet encès?: "))
if LOS and Internet:
    print("La connexió sembla funcionar correctament")
elif LOS and not Internet:
    print("Cal comprovar el servei del proveïdor")
elif not LOS and Internet:
    print("Cal revisar el cable de fibra")
else:
    print("Cal revisar el cable de fibra i comprovar el servei del proveïdor")
# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
percentatge = int(input("Introdueix el percentatge de bateria disponible al SAI: "))
if percentatge < 0 or percentatge > 100:
    print("Introdueix un percentatge vàlid (0-100)")
elif percentatge < 20:
    print("El nivell de bateria és crític")
elif percentatge < 50:
    print("El nivell de bateria és baix")
else:
    print("El nivell de bateria és suficient")
# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latencia = int(input("Introdueix la latència en mil·lisegons: "))
perdua = int(input("Introdueix el percentatge de paquets perduts: "))
if latencia < 0 or perdua < 0 or perdua > 100:
    print("Introdueix valors vàlids")
elif latencia <= 30 and perdua <= 1:
    print("La connexió és excel·lent")
elif latencia <= 80 and perdua <= 3:
    print("La connexió és bona")
elif latencia <= 150 and perdua <= 5:
    print("La connexió és acceptable")
else:
    print("La connexió és deficient")
# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
pla = input("Introdueix el tipus de pla (bàsic o plus): ")
consum = int(input("Introdueix el consum mensual en GB: "))
if consum < 0:
    print("Introdueix un consum vàlid (0 o més)")
elif pla == "bàsic":
    cost_base = 10
    limit = 10
    cost_exces = 1.50
if consum > limit:
        cost_total = cost_base + (consum - limit) * cost_exces
    else:
        cost_total = cost_base
elif pla == "plus":
    cost_base = 20
    limit = 30
    cost_exces = 0.75
    if consum > limit:
        cost_total = cost_base + (consum - limit) * cost_exces
    else:
        cost_total = cost_base
else:
    print("Introdueix un tipus de pla vàlid (bàsic o plus)")

print(f"El cost total del pla és: {cost_total} €")
# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
compte = bool(input("El compte està actiu?: "))
contrasenya = bool(input("La contrasenya és correcta?: "))
codi_verificacio = bool(input("El codi de doble verificació és correcte?: "))
if not compte:
    print("Accés denegat: el compte està desactivat")
elif not contrasenya:
    print("Accés denegat: la contrasenya és incorrecta")
elif not codi_verificacio:
    print("Accés denegat: el codi de doble verificació és incorrecte")
else:
    print("Accés permès")
# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router_encès = bool(input("El router està encès?: "))
LOS = bool(input("Terminal òptic encès?: "))
Internet = bool(input("Indicador d'Internet encès?: "))
if not router_encès:
    print("Cal encendre el router")
elif LOS and Internet:
    print("La connexió sembla funcionar correctament")
elif LOS and not Internet:
    print("Cal contactar amb el proveïdor")
elif not LOS and Internet:
    print("Cal revisar el cable de fibra")
else:
    print("Cal revisar el cable de fibra i contactar amb el proveïdor")
# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
servei_critic = bool(input("La incidència afecta un servei crític?: "))
usuaris = int(input("Nombre d'usuaris afectats?: "))
if usuaris < 0:
    print("Introdueix un nombre d'usuaris vàlid (0 o més)")
else:
    alternativa = bool(input("Hi ha una alternativa de connexió disponible?: "))
    if servei_critic and not alternativa:
        print("Prioritat crítica")
    elif usuaris >= 50 and not alternativa:
        print("Prioritat crítica")
    elif usuaris >= 10 or servei_critic:
        print("Prioritat alta")
    else:
        print("Prioritat baixa")