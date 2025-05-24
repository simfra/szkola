from models.nauczyciel import Nauczyciel
from models.przedmiot import Przedmiot

lista_nauczycieli = []
lista_przedmiotow = []

def dodaj_przedmiot_do_listy():
    nazwa = input("Podaj nazwę przedmiotu: ").strip()
    poziom = input("Podaj poziom trudności (łatwy/średni/trudny): ").strip().lower()
    if poziom not in ["łatwy", "średni", "trudny"]:
        poziom = "średni"
    przedmiot = Przedmiot(nazwa, poziom)
    if przedmiot in lista_przedmiotow:
        print("Taki przedmiot już istnieje.")
    else:
        lista_przedmiotow.append(przedmiot)
        print(f"Przedmiot '{nazwa}' dodany do listy.")

def pokaz_przedmioty():
    if not lista_przedmiotow:
        print("Brak przedmiotów w systemie.")
        return
    print("\nLista dostępnych przedmiotów:")
    for i, p in enumerate(lista_przedmiotow, 1):
        print(f"{i}. {p}")

def wybierz_przedmiot():
    if not lista_przedmiotow:
        print("Brak przedmiotów do wyboru.")
        return None
    pokaz_przedmioty()
    wybor = input("Wybierz numer przedmiotu: ").strip()
    if wybor.isdigit():
        nr = int(wybor)
        if 1 <= nr <= len(lista_przedmiotow):
            return lista_przedmiotow[nr - 1]
    print("Niepoprawny numer.")
    return None

def dodaj_nauczyciela():
    imie = input("Podaj imię nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    email = input("Podaj email (opcjonalnie): ").strip() or None
    telefon = input("Podaj telefon (opcjonalnie): ").strip() or None
    etat = input("Podaj etat (pełny etat/część etatu, domyślnie pełny etat): ").strip().lower()
    if etat not in ["pełny etat", "część etatu"]:
        etat = "pełny etat"
    nauczyciel = Nauczyciel(imie, nazwisko, email, telefon, etat)
    lista_nauczycieli.append(nauczyciel)
    print("Nauczyciel został dodany.")

def pokaz_nauczycieli():
    if not lista_nauczycieli:
        print("Brak nauczycieli.")
        return
    print("\nLista nauczycieli:")
    for i, n in enumerate(lista_nauczycieli, 1):
        print(f"{i}. {n.imie} {n.nazwisko} {n.etat} | {n.dane_kontaktowe()} | Przedmioty: {n.pokaz_przedmioty()}")

def usun_nauczyciela():
    pokaz_nauczycieli()
    if not lista_nauczycieli:
        return
    wybor = input("Podaj numer nauczyciela do usunięcia: ").strip()
    if wybor.isdigit():
        nr = int(wybor)
        if 1 <= nr <= len(lista_nauczycieli):
            usuniety = lista_nauczycieli.pop(nr - 1)
            print(f"Nauczyciel {usuniety.imie} {usuniety.nazwisko} został usunięty.")
            return
    print("Niepoprawny numer.")

def edytuj_nauczyciela():
    pokaz_nauczycieli()
    if not lista_nauczycieli:
        return
    wybor = input("Podaj numer nauczyciela do edycji: ").strip()
    if wybor.isdigit():
        nr = int(wybor)
        if 1 <= nr <= len(lista_nauczycieli):
            nauczyciel = lista_nauczycieli[nr - 1]
            print(f"Edytujesz: {nauczyciel.imie} {nauczyciel.nazwisko}")
            nowe_imie = input("Podaj nowe imię (enter = brak zmian): ").strip()
            nowe_nazwisko = input("Podaj nowe nazwisko (enter = brak zmian): ").strip()
            email = input("Podaj nowy email (enter = brak zmian): ").strip()
            telefon = input("Podaj nowy telefon (enter = brak zmian): ").strip()
            etat = input("Podaj etat (pełny etat/część etatu, enter = brak zmian): ").strip().lower()
            if nowe_imie:
                nauczyciel.imie = nowe_imie
            if nowe_nazwisko:
                nauczyciel.nazwisko = nowe_nazwisko
            if email:
                nauczyciel.email = email
            if telefon:
                nauczyciel.telefon = telefon
            if etat in ["pełny etat", "część etatu"]:
                nauczyciel.etat = etat
            print("Dane nauczyciela zostały zaktualizowane.")
            return
    print("Niepoprawny numer.")

def przypisz_przedmiot():
    if not lista_nauczycieli:
        print("Brak nauczycieli.")
        return
    pokaz_nauczycieli()
    wybor = input("Podaj numer nauczyciela, któremu chcesz przypisać przedmiot: ").strip()
    if wybor.isdigit():
        nr = int(wybor)
        if 1 <= nr <= len(lista_nauczycieli):
            nauczyciel = lista_nauczycieli[nr - 1]
            przedmiot = wybierz_przedmiot()
            if przedmiot:
                nauczyciel.dodaj_przedmiot(przedmiot)
                print(f"Przedmiot '{przedmiot.nazwa}' został przypisany do nauczyciela {nauczyciel.imie} {nauczyciel.nazwisko}.")
            return
    print("Niepoprawny numer.")

def usun_przedmiot_od_nauczyciela():
    if not lista_nauczycieli:
        print("Brak nauczycieli.")
        return
    pokaz_nauczycieli()
    wybor = input("Podaj numer nauczyciela, od którego chcesz usunąć przedmiot: ").strip()
    if wybor.isdigit():
        nr = int(wybor)
        if 1 <= nr <= len(lista_nauczycieli):
            nauczyciel = lista_nauczycieli[nr - 1]
            if not nauczyciel.przedmioty:
                print("Ten nauczyciel nie ma przypisanych przedmiotów.")
                return
            print("Przedmioty:")
            for i, p in enumerate(nauczyciel.przedmioty, 1):
                print(f"{i}. {p}")
            wybor_p = input("Podaj numer przedmiotu do usunięcia: ").strip()
            if wybor_p.isdigit():
                nr_p = int(wybor_p)
                if 1 <= nr_p <= len(nauczyciel.przedmioty):
                    usuniety = nauczyciel.przedmioty.pop(nr_p - 1)
                    print(f"Usunięto przedmiot '{usuniety}'.")
                    return
    print("Niepoprawny numer.")

def pokaz_nauczycieli_po_przedmiocie():
    nazwa = input("Podaj nazwę przedmiotu: ").strip()
    znalezieni = []
    for nauczyciel in lista_nauczycieli:
        for p in nauczyciel.przedmioty:
            if p.nazwa.lower() == nazwa.lower():
                znalezieni.append(nauczyciel)
                break
    if not znalezieni:
        print(f"Brak nauczycieli uczących przedmiot '{nazwa}'.")
    else:
        print(f"Nauczyciele uczący przedmiot '{nazwa}':")
        for n in znalezieni:
            print(f"- {n.imie} {n.nazwisko}")

def pokaz_szczegoly_nauczyciela():
    pokaz_nauczycieli()
    if not lista_nauczycieli:
        return
    wybor = input("Podaj numer nauczyciela do wyświetlenia szczegółów: ").strip()
    if wybor.isdigit():
        nr = int(wybor)
        if 1 <= nr <= len(lista_nauczycieli):
            n = lista_nauczycieli[nr - 1]
            print(f"\nSzczegóły nauczyciela:")
            print(f"Imię i nazwisko: {n.imie} {n.nazwisko}")
            print(f"Email: {n.email or 'brak'}")
            print(f"Telefon: {n.telefon or 'brak'}")
            print(f"Etat: {n.etat}")
            print("Przedmioty:")
            for p in n.przedmioty:
                print(f"- {p}")
            return
    print("Niepoprawny numer.")

def zarzadzaj_nauczycielami():
    while True:
        print("\n--- Zarządzanie nauczycielami ---")
        print("1. Dodaj nauczyciela")
        print("2. Pokaż nauczycieli")
        print("3. Edytuj nauczyciela")
        print("4. Usuń nauczyciela")
        print("5. Przypisz przedmiot")
        print("6. Usuń przedmiot od nauczyciela")
        print("7. Pokaż nauczycieli po przedmiocie")
        print("8. Pokaż szczegóły nauczyciela")
        print("0. Powrót do menu głównego")

        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dodaj_nauczyciela()
        elif wybor == "2":
            pokaz_nauczycieli()
        elif wybor == "3":
            edytuj_nauczyciela()
        elif wybor == "4":
            usun_nauczyciela()
        elif wybor == "5":
            przypisz_przedmiot()
        elif wybor == "6":
            usun_przedmiot_od_nauczyciela()
        elif wybor == "7":
            pokaz_nauczycieli_po_przedmiocie()
        elif wybor == "8":
            pokaz_szczegoly_nauczyciela()
        elif wybor == "0":
            break
        else:
            print("Niepoprawny wybór.")
