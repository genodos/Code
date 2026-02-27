"""
1.
===============================================================================
Fallakte - Sachgebiet: Hochschule
===============================================================================

2.
===============================================================================
Nachname - str (Nur Buchstaben evtl. Umlaute, Bindestriche - min. 2 Zeichen)
Vorname - str (-||-)
Matrikelnummer - str (== 7 Zahlen, nur Ziffern)
Credits - int (Credits >= 0)
Email - str (1x @ - keine Leerzeichen, Vor und Nach @ zeichen, Punkt muss da 
sein, darf nicht mit Punkt beginnen)
Geburtsdatum - str (TT.MM.JJJJ, nur String-Operationen)
===============================================================================
"""

#===============================================================================
# Funktionen (Validierung)
#===============================================================================

def validiere_datum(date_str):
    """
    Validiert ein Datum im Format TT.MM.JJJJ nur mit String-Operationen.
    
    Rückgabe: True, wenn gültig, sonst False.
    """
    # 1. Leerzeichen entfernen
    date_str = date_str.strip()
    
    # 2. Länge grob prüfen (z.B. 10 Zeichen: 01.01.2000)
    if len(date_str) != 10:
        print("Länge ungültig. Format muss TT.MM.JJJJ sein.")
        return False
        
    # 3. Prüfen, ob zwei Punkte vorhanden sind
    if date_str.count(".") != 2:
        print("Formatfehler: Zwei Punkte erwartet.")
        return False
    
    # 4. String am Punkt teilen
    parts = date_str.split(".") # erzeugt Liste ["TT", "MM", "JJJJ"]
    
    day_str = parts[0]
    month_str = parts[1]
    year_str = parts[2]
    
    # 5. Prüfen ob alles Zahlen sind
    if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
        print("Das Datum darf nur Zahlen und Punkte enthalten.")
        return False
        
    # 6. Konvertierung und Wertebereichsprüfung
    day = int(day_str)
    month = int(month_str)
    year = int(year_str)
    
    if month < 1 or month > 12:
        print("Monat muss zwischen 01 und 12 liegen.")
        return False
        
    if day < 1 or day > 31:
        print("Tag muss zwischen 01 und 31 liegen.")
        return False
        
    # Verfeinerung für Monate mit 30 Tagen 
    if month in [4, 6, 9, 11] and day > 30:
         print("Dieser Monat hat nur 30 Tage.")
         return False
         
    if month == 2 and day > 29:
         print("Februar hat maximal 29 Tage (vereinfacht).")
         return False
         
    if year < 1900 or year > 2100:
        print("Jahr liegt außerhalb des gültigen Bereichs.")
        return False

    return True

#===============================================================================
# Eigene Funktionen
#===============================================================================

def validiere_name(name_str):
    """
    str (Nur Buchstaben(+ Umlaute, Leerzeichen) evtl. Umlaute, Bindestriche - min. 2 Zeichen)
    Ausgabe: True o. False
    """
    name_str = name_str.strip()
    if len(name_str) < 2:
        print("X: Der Name muss mindestens 2 Zeichen lang sein.")
        return False
    
    erlaubte_zeichen = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ -"
    for n in name_str:
        if n not in erlaubte_zeichen:
            print(f"X: Ungültiges Zeichen {n}. Nur Buchstaben, Bindestriche und Leerzeichen sind erlaubt.")
            return False
        
    return True

def validiere_matrikelnummer(mat_str, dict, list):
    """
    (== 7 Zahlen, nur Ziffern)
    Ausgabe: True oder False
    """

    mat_str = mat_str.strip()
    if len(mat_str) != 7:
        print("X: Die Matrikelnummer muss genau 7 Ziffern lang sein.")
        return False
    
    if not mat_str.isdigit():
        print("X: Die Matrikelnummer darf nur aus Zahlen bestehen.")
        return False
    
    if mat_str in list:
        print("X: Diese Matrikelnummer existiert bereits in der Liste.")
        return False
    
    if mat_str in dict:
        print("X: Diese Matrikelnummer existiert bereits im Dictionary.")
        return False
    
    return True

def validiere_credits(cred_int):
    """
    (Credits >= 0)
    """
    try:
        cred_int = int(cred_int)
    except:
        print("X: Creditscores müssen Zahlen sein.")
        return False

    if cred_int < 0:
        print("X: Man kann nicht weniger als 0 Credits haben.")
        return False
    
    return True

def validiere_email(email_str):
    """
    min. 5 Zeichen, keine Leerzeichen, genau 1x @, Zeichen Vor und nach @ (bzw. domain), 
    Nicht mit Punkt anfangen oder aufhören
    """

    email_str = email_str.strip()
    if len(email_str) < 5:
        print("X: Die E-Mail-Adresse ist zu kurz (mindestens 5 Zeichen).")
        return False

    if " " in email_str:
        print("X: Die E-Mail-Adresse darf keine Leerzeichen enthalten.")
        return False

    if email_str.count("@") != 1:
        print("X: Die E-Mail-Adresse muss genau ein @ enthalten.")
        return False

    # Aufteilen am @
    teile = email_str.split("@")
    lokaler_teil = teile[0]
    domain_teil = teile[1]

    if len(lokaler_teil) < 1:
        print("X: Vor dem @ muss mindestens ein Zeichen stehen.")
        return False

    if "." not in domain_teil:
        print("X: Nach dem @ muss ein Punkt in der Domain vorhanden sein.")
        return False

    if domain_teil.startswith(".") or domain_teil.endswith("."):
        print("X: Die Domain darf nicht mit einem Punkt beginnen oder enden.")
        return False

    return True


#===============================================================================
# Fallakte erfassen
#===============================================================================

def erfasse_neue_fallakte(dict, list):
    print("\n--- Neue Fallakte anlegen ---")
    
    # Feld 1
    while True:
        nachname = input("\n Nachname: ")
        if validiere_name(nachname):
            nachname = nachname.strip()
            break
        print("X: Bitte erneut eingeben. \n")

    # Feld 2
    while True:
        vorname = input("\n Vorname: ")
        if validiere_name(vorname):
            vorname = vorname.strip()
            break
        print("X: Bitte erneut eingeben. \n")

    # Feld 3
    while True:
        matrikelnummer = input("\n Matrikelnummer (7 Ziffern): ")
        if validiere_matrikelnummer(matrikelnummer, dict, list):
            matrikelnummer = matrikelnummer.strip()
            break
        print("X: Bitte erneut eingeben. \n")

    # Feld 4
    while True:
        credits = input("\n Anzahl der gesammelten Credits: ")
        if validiere_credits(credits):
            credits = credits.strip()
            break
        print("X: Bitte erneut eingeben. \n")

    #Feld 5
    while True:
        email = input("\n Email-Adresse eingeben: ")
        if validiere_email(email):
            email = email.strip()
            break
        print("X: Bitte erneut eingeben. \n")

    # Feld 6 - Geburtsdatum
    while True:
        geburtsdatum = input("\n Geburtsdatum (TT.MM.JJJJ): ")
        if validiere_datum(geburtsdatum):
            geburtsdatum = geburtsdatum.strip()
            break
        print("X: Bitte erneut eingeben. \n")


    # Erstellen Sie das Dictionary für diesen Fall
    fall_dict = {
        "nachname": nachname,
        "vorname": vorname,
        "matrikelnummer": matrikelnummer,
        "credits": credits,
        "email": email,
        "geburtsdatum": geburtsdatum
        
    }
    
    print("Fall wurde lokal erfasst:")
    print(fall_dict)
    print("-------------------------")
    return fall_dict

# Speichern
def speichere_fall_dict(fall_dict, dict):
   
   schluessel = fall_dict["matrikelnummer"]
   dict[schluessel] = fall_dict
   print(fall_dict)
   print(f" In Dictionary gespeichert (Schlüssel: {schluessel})")

def speichere_fall_liste(fall_dict, liste):
   
   liste.append(fall_dict)
   print(fall_dict)
   print("-------------------------")
   print(f" In Liste gespeichert ( Positione: {len(liste)})")


# Anzeigen
def zeige_alle_faelle_dict(dict):

    if len(dict) == 0:
        print("\n  Keine Fallakten im Dictionary vorhanden.")
        return
    
    for fall in dict.values():
        print(f"| Nachname      : {fall['nachname']}")
        print(f"| Vorname       : {fall['vorname']}")
        print(f"| Matrikelnummer: {fall['matrikelnummer']}")
        print(f"| Credits       : {fall['credits']}")
        print(f"| Email         : {fall['email']}")
        print("-------------------------")

def zeige_alle_faelle_liste(list):
    
    if len(list) == 0:
        print("\n  Keine Fallakten in der Liste vorhanden.")
        return
    
    for fall in list:
        print(f"| Position      : {list.index(fall)}")
        print(f"| Nachname      : {fall['nachname']}")
        print(f"| Vorname       : {fall['vorname']}")
        print(f"| Matrikelnummer: {fall['matrikelnummer']}")
        print(f"| Credits       : {fall['credits']}")
        print(f"| Email         : {fall['email']}")
        print("-------------------------")

def zeige_fall_aus_dict(dict, matrikelnummer):
    if matrikelnummer in dict:
        fall = dict[matrikelnummer]
        print(f"| Nachname      : {fall['nachname']}")
        print(f"| Vorname       : {fall['vorname']}")
        print(f"| Matrikelnummer: {fall['matrikelnummer']}")
        print(f"| Credits       : {fall['credits']}")
        print(f"| Email         : {fall['email']}")
        print("-------------------------")
    else:
        print(f"X: Keine Fallakte mit Matrikelnummer {matrikelnummer} gefunden.")

def zeige_fall_aus_liste(list, Listenposition):
    if 0 <= Listenposition < len(list):
        fall = list[Listenposition]
        print(f"| Nachname      : {fall['nachname']}")
        print(f"| Vorname       : {fall['vorname']}")
        print(f"| Matrikelnummer: {fall['matrikelnummer']}")
        print(f"| Credits       : {fall['credits']}")
        print(f"| Email         : {fall['email']}")
        print("-------------------------")
        return
    print(f"X: Keine Fallakte mit Listenposition {Listenposition} gefunden.")

#===============================================================================
# Programm:
#===============================================================================


# leere Fallaktenliste
fallakten_liste = []
# leeres Fallakten Dict
fallakten_dict = {}

while True:
    print("===============================")
    print("1. Neuen Fall erfassen")
    print("2. Alle Fälle anzeigen (Liste)")
    print("3. Alle Fälle anzeigen (Dictionary)")
    print("4. Zeige Fall aus Liste")
    print("5. Zeige Fall aus Dictionary")
    print("6. Beenden")
    
    auswahl = input("\nIhre Auswahl: ")
    
    if auswahl == "1":
        # Datenerfassung
        neuer_fall = erfasse_neue_fallakte(fallakten_liste, fallakten_dict)
        # Speicherung
        speichere_fall_dict(neuer_fall, fallakten_dict)
        speichere_fall_liste(neuer_fall, fallakten_liste)
        
    elif auswahl == "2":
        zeige_alle_faelle_liste(fallakten_liste)
        
    elif auswahl == "3":
        zeige_alle_faelle_dict(fallakten_dict)

    elif auswahl == "4":
        List_pos = input("\nGeben Sie die Listenposition des gesuchten Falls ein: ")
        try:
            List_pos = int(List_pos)
        except ValueError:
            print("Ungültige Listenposition. Bitte geben Sie eine Zahl ein.")
            continue
        zeige_fall_aus_liste(fallakten_liste, List_pos)

    elif auswahl == "5":
        mat_num = input("\nGeben Sie die Matrikelnummer des gesuchten Falls ein: ")
        zeige_fall_aus_dict(fallakten_dict, mat_num)
        
    elif auswahl == "6":
        print("Auf Wiedersehen!")
        break
    else:
        print("Ungültige Auswahl. Bitte erneut versuchen.")

