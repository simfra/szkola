# Importujemy klasę Uczen z folderu models
from models.uczen import Uczen

# Lista przechowująca wszystkich uczniów
lista_uczniow = []

# Dodawanie nowego ucznia
def dodaj_ucznia():
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    klasa = input("Podaj klasę ucznia (np. 3A): ")
    uczen = Uczen(imie, nazwisko, klasa)  # tworzymy nowy obiekt Uczen
    lista_uczniow.append(uczen)  # dodajemy go do listy
    print("Uczeń został dodany.")

# Wyświetlanie listy uczniów
def pokaz_uczniow():
    if not lista_uczniow:
        print("Brak uczniów.")
    else:
        print("\nLista uczniów:")
        for i, u in enumerate(lista_uczniow, 1):
            print(f"{i}. {u.imie} {u.nazwisko} (klasa: {u.klasa})")

# Usuwanie ucznia z listy
def usun_ucznia():
    pokaz_uczniow()
    if not lista_uczniow:
        return
    nr = int(input("Podaj numer ucznia do usunięcia: "))
    if 1 <= nr <= len(lista_uczniow):
        usuniety = lista_uczniow.pop(nr - 1)
        print(f"Uczeń {usuniety.imie} {usuniety.nazwisko} został usunięty.")
    else:
        print("Niepoprawny numer.")

# Edycja danych ucznia
def edytuj_ucznia():
    pokaz_uczniow()
    if not lista_uczniow:
        return
    nr = int(input("Numer ucznia do edycji: "))
    if 1 <= nr <= len(lista_uczniow):
        uczen = lista_uczniow[nr - 1]
        print(f"Edytujesz: {uczen.imie} {uczen.nazwisko} (klasa: {uczen.klasa})")
        imie = input(f"Nowe imię [{uczen.imie}]: ") or uczen.imie
        nazwisko = input(f"Nowe nazwisko [{uczen.nazwisko}]: ") or uczen.nazwisko
        klasa = input(f"Nowa klasa [{uczen.klasa}]: ") or uczen.klasa
        uczen.imie = imie
        uczen.nazwisko = nazwisko
        uczen.klasa = klasa
        print("Dane ucznia zostały zaktualizowane.")
    else:
        print("Niepoprawny numer.")

# Wyświetlanie ocen konkretnego ucznia
def pokaz_oceny_ucznia():
    pokaz_uczniow()
    if not lista_uczniow:
        return
    nr = int(input("Podaj numer ucznia, którego oceny chcesz zobaczyć: "))
    if 1 <= nr <= len(lista_uczniow):
        uczen = lista_uczniow[nr - 1]
        print(f"Oceny ucznia {uczen.imie} {uczen.nazwisko}: {uczen.pokaz_oceny()}")
    else:
        print("Niepoprawny numer.")

# Dodawanie oceny uczniowi
def dodaj_ocene_uczniowi():
    pokaz_uczniow()
    if not lista_uczniow:
        return
    nr = int(input("Numer ucznia do dodania oceny: "))
    if 1 <= nr <= len(lista_uczniow):
        ocena = input("Podaj ocenę: ")
        uczen = lista_uczniow[nr - 1]
        uczen.dodaj_ocene(ocena)
        print(f"Ocenę {ocena} dodano uczniowi {uczen.imie} {uczen.nazwisko}.")
    else:
        print("Niepoprawny numer.")

# Usuwanie jednej oceny uczniowi
def usun_ocene_uczniowi():
    pokaz_uczniow()
    if not lista_uczniow:
        return
    nr = int(input("Numer ucznia do usunięcia oceny: "))
    if 1 <= nr <= len(lista_uczniow):
        uczen = lista_uczniow[nr - 1]
        if not uczen.oceny:
            print("Uczeń nie ma ocen.")
            return
        print(f"Oceny ucznia: {', '.join(uczen.oceny)}")
        ocena_do_usuniecia = input("Podaj ocenę do usunięcia: ")
        if ocena_do_usuniecia in uczen.oceny:
            uczen.oceny.remove(ocena_do_usuniecia)
            print(f"Ocenę {ocena_do_usuniecia} usunięto.")
        else:
            print("Uczeń nie ma takiej oceny.")
    else:
        print("Niepoprawny numer.")

# Wyszukiwanie ucznia po nazwisku lub klasie
def wyszukaj_ucznia():
    fraza = input("Podaj frazę do wyszukania w nazwisku lub klasie: ").lower()
    znalezieni = [u for u in lista_uczniow if fraza in u.nazwisko.lower() or fraza in u.klasa.lower()]
    if znalezieni:
        print("Znalezieni uczniowie:")
        for u in znalezieni:
            print(f"{u.imie} {u.nazwisko} (klasa: {u.klasa})")
    else:
        print("Nie znaleziono uczniów.")

# Sortowanie uczniów po nazwisku i imieniu
def sortuj_uczniow():
    lista_uczniow.sort(key=lambda u: (u.nazwisko.lower(), u.imie.lower()))
    print("Lista uczniów posortowana po nazwisku i imieniu.")

# Obliczanie średniej ocen ucznia
def srednia_ocen_ucznia():
    pokaz_uczniow()
    if not lista_uczniow:
        return
    nr = int(input("Numer ucznia do obliczenia średniej: "))
    if 1 <= nr <= len(lista_uczniow):
        uczen = lista_uczniow[nr - 1]
        oceny = []
        for o in uczen.oceny:
            oc = float(o)
            oceny.append(oc)
        if not oceny:
            print("Uczeń nie ma ocen.")
        else:
            srednia = sum(oceny) / len(oceny)
            print(f"Średnia ocen ucznia {uczen.imie} {uczen.nazwisko}: {srednia:.2f}")
    else:
        print("Niepoprawny numer.")

# Menu do zarządzania uczniami
def zarzadzaj_uczniami():
    while True:
        print("\n--- Zarządzanie uczniami ---")
        print("1. Dodaj ucznia")
        print("2. Pokaż uczniów")
        print("3. Usuń ucznia")
        print("4. Edytuj ucznia")
        print("5. Pokaż oceny ucznia")
        print("6. Dodaj ocenę uczniowi")
        print("7. Usuń ocenę uczniowi")
        print("8. Wyszukaj ucznia")
        print("9. Sortuj uczniów")
        print("10. Oblicz średnią ocen ucznia")
        print("0. Powrót do menu głównego")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_ucznia()
        elif wybor == "2":
            pokaz_uczniow()
        elif wybor == "3":
            usun_ucznia()
        elif wybor == "4":
            edytuj_ucznia()
        elif wybor == "5":
            pokaz_oceny_ucznia()
        elif wybor == "6":
            dodaj_ocene_uczniowi()
        elif wybor == "7":
            usun_ocene_uczniowi()
        elif wybor == "8":
            wyszukaj_ucznia()
        elif wybor == "9":
            sortuj_uczniow()
        elif wybor == "10":
            srednia_ocen_ucznia()
        elif wybor == "0":
            break
        else:
            print("Niepoprawny wybór.")
