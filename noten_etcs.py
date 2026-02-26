faecher = []


def fach_hinzufuegen():
    name = input("Fachname: ")
    ects = float(input("ECTS-Punkte: "))
    note = float(input("Note: "))

    fach = {
        "name": name,
        "ects": ects,
        "note": note
    }

    faecher.append(fach)
    print("Fach gespeichert.")


def durchschnitt_berechnen():
    summe_ects = 0
    summe_gewichtet = 0

    for fach in faecher:
        summe_ects += fach["ects"]
        summe_gewichtet += fach["note"] * fach["ects"]

    if summe_ects == 0:
        print("Keine Fächer vorhanden.")
        return

    durchschnitt = summe_gewichtet / summe_ects
    print("Gewichteter Durchschnitt:", durchschnitt)


def fach_suchen():
    suchname = input("Welches Fach suchen? ")

    for fach in faecher:
        if fach["name"].lower() == suchname.lower():
            print("Gefunden:")
            print("ECTS:", fach["ects"])
            print("Note:", fach["note"])
            return

    print("Fach nicht gefunden.")


# -------- Menü (Applikation) --------

while True:
    print("\n1 - Fach hinzufügen")
    print("2 - Durchschnitt berechnen")
    print("3 - Fach suchen")
    print("4 - Beenden")

    wahl = input("Auswahl: ")

    if wahl == "1":
        fach_hinzufuegen()
    elif wahl == "2":
        durchschnitt_berechnen()
    elif wahl == "3":
        fach_suchen()
    elif wahl == "4":
        break
    else:
        print("Ungültige Eingabe.")

