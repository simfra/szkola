from models.klasa import Klasa
from managers.wychowawca_manager import lista_wychowawcow
from managers.uczen_manager import lista_uczniow

lista_klas = []  # lista klas w systemie

def dodaj_klase():
    nazwa = input("Podaj nazwę klasy (np. 1A): ").strip()
    if any(k.nazwa == nazwa for k in lista_klas):
        print("Taka klasa już istnieje.")
        return
    klasa = Klasa(nazwa)  # tworzymy nową klasę
    lista_klas.append(klasa)  # dodajemy do listy
    print(f"Klasa {nazwa} została dodana.")

def pokaz_klasy():
    if not lista_klas:
        print("Brak klas w systemie.")
        return
    print("\nLista klas:")
    for i, k in enumerate(lista_klas, 1):
        wych = k.wychowawca.imie + " " + k.wychowawca.nazwisko if k.wychowawca else "brak"
        print(f"{i}. {k.nazwa} | Wychowawca: {wych} | Liczba uczniów: {len(k.uczniowie)}")

def usun_klase():
    pokaz_klasy()
    if not lista_klas:
        return
    nr = int(input("Podaj numer klasy do usunięcia: "))
    if 1 <= nr <= len(lista_klas):
        usunieta = lista_klas.pop(nr - 1)  # usuwamy klasę
        print(f"Klasa {usunieta.nazwa} została usunięta.")
    else:
        print("Niepoprawny numer.")

def edytuj_klase():
    pokaz_klasy()
    if not lista_klas:
        return
    nr = int(input("Podaj numer klasy do edycji: "))
    if 1 <= nr <= len(lista_klas):
        klasa = lista_klas[nr - 1]
        print(f"Edytujesz klasę: {klasa.nazwa}")
        nowa_nazwa = input("Podaj nową nazwę klasy (enter = brak zmian): ").strip()
        if nowa_nazwa:
            if any(k.nazwa == nowa_nazwa for k in lista_klas):
                print("Klasa o takiej nazwie już istnieje.")
            else:
                klasa.nazwa = nowa_nazwa  # zmieniamy nazwę
                print("Nazwa klasy została zmieniona.")
        else:
            print("Nazwa klasy nie zmieniona.")
    else:
        print("Niepoprawny numer.")

def wybierz_klase():
    if not lista_klas:
        print("Brak klas do wyboru.")
        return None
    pokaz_klasy()
    nr = int(input("Wybierz numer klasy: "))
    if 1 <= nr <= len(lista_klas):
        return lista_klas[nr - 1]
    else:
        print("Niepoprawny numer.")
        return None

def przypisz_wychowawce():
    if not lista_klas:
        print("Brak klas w systemie.")
        return
    if not lista_wychowawcow:
        print("Brak wychowawców w systemie.")
        return
    klasa = wybierz_klase()
    if not klasa:
        return
    print("Wybierz wychowawcę do przypisania:")
    for i, w in enumerate(lista_wychowawcow, 1):
        print(f"{i}. {w.imie} {w.nazwisko}")
    nr = int(input("Numer wychowawcy: "))
    if 1 <= nr <= len(lista_wychowawcow):
        klasa.wychowawca = lista_wychowawcow[nr - 1]  # przypisujemy wychowawcę
        print(f"Wychowawca {klasa.wychowawca.imie} {klasa.wychowawca.nazwisko} został przypisany do klasy {klasa.nazwa}.")
    else:
        print("Niepoprawny numer.")

def przypisz_ucznia():
    if not lista_klas:
        print("Brak klas w systemie.")
        return
    if not lista_uczniow:
        print("Brak uczniów w systemie.")
        return
    klasa = wybierz_klase()
    if not klasa:
        return
    print("Wybierz ucznia do przypisania:")
    for i, u in enumerate(lista_uczniow, 1):
        print(f"{i}. {u.imie} {u.nazwisko}")
    nr = int(input("Numer ucznia: "))
    if 1 <= nr <= len(lista_uczniow):
        uczen = lista_uczniow[nr - 1]
        klasa.dodaj_ucznia(uczen)  # dodajemy ucznia do klasy
        print(f"Uczeń {uczen.imie} {uczen.nazwisko} został przypisany do klasy {klasa.nazwa}.")
    else:
        print("Niepoprawny numer.")

def usun_ucznia_z_klasy():
    if not lista_klas:
        print("Brak klas w systemie.")
        return
    klasa = wybierz_klase()
    if not klasa:
        return
    if not klasa.uczniowie:
        print("Ta klasa nie ma przypisanych uczniów.")
        return
    print("Uczniowie w klasie:")
    for i, u in enumerate(klasa.uczniowie, 1):
        print(f"{i}. {u.imie} {u.nazwisko}")
    nr = int(input("Podaj numer ucznia do usunięcia: "))
    if 1 <= nr <= len(klasa.uczniowie):
        usuniety = klasa.uczniowie.pop(nr - 1)  # usuwamy ucznia
        print(f"Uczeń {usuniety.imie} {usuniety.nazwisko} został usunięty z klasy {klasa.nazwa}.")
    else:
        print("Niepoprawny numer.")

def pokaz_uczniow_w_klasie():
    klasa = wybierz_klase()
    if not klasa:
        return
    if not klasa.uczniowie:
        print("Ta klasa nie ma przypisanych uczniów.")
        return
    print(f"Uczniowie w klasie {klasa.nazwa}:")
    for u in klasa.uczniowie:
        print(f"- {u.imie} {u.nazwisko}")

def zarzadzaj_klasami():
    while True:
        print("\n--- Zarządzanie klasami ---")
        print("1. Pokaż klasy")
        print("2. Dodaj klasę")
        print("3. Edytuj klasę")
        print("4. Usuń klasę")
        print("5. Przypisz wychowawcę do klasy")
        print("6. Przypisz ucznia do klasy")
        print("7. Usuń ucznia z klasy")
        print("8. Pokaż uczniów w klasie")
        print("0. Powrót do menu głównego")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_klasy()
        elif wybor == "2":
            dodaj_klase()
        elif wybor == "3":
            edytuj_klase()
        elif wybor == "4":
            usun_klase()
        elif wybor == "5":
            przypisz_wychowawce()
        elif wybor == "6":
            przypisz_ucznia()
        elif wybor == "7":
            usun_ucznia_z_klasy()
        elif wybor == "8":
            pokaz_uczniow_w_klasie()
        elif wybor == "0":
            break
        else:
            print("Niepoprawny wybór.")
