from models.wychowawca import Wychowawca  # Import klasy Wychowawca

# Lista przechowująca wychowawców
lista_wychowawcow = []


def zarzadzaj_wychowawcami():
    # Główna pętla zarządzania wychowawcami
    while True:
        print("\n--- Zarządzanie wychowawcami ---")
        print("1. Dodaj wychowawcę")
        print("2. Pokaż wychowawców")
        print("3. Edytuj wychowawcę")
        print("4. Usuń wychowawcę")
        print("5. Wyszukaj wychowawcę")
        print("0. Powrót do menu")

        wybor = input("Wybierz opcję: ").strip()

        # Obsługa wyboru użytkownika
        if wybor == "1":
            dodaj_wychowawce()
        elif wybor == "2":
            pokaz_wychowawcow()
        elif wybor == "3":
            edytuj_wychowawce()
        elif wybor == "4":
            usun_wychowawce()
        elif wybor == "5":
            wyszukaj_wychowawce()
        elif wybor == "0":
            break
        else:
            print("Niepoprawny wybór")


def dodaj_wychowawce():
    # Funkcja dodająca nowego wychowawcę
    imie = input("Imię wychowawcy: ").strip()
    if not imie:
        print("Imię nie może być puste.")
        return
    nazwisko = input("Nazwisko wychowawcy: ").strip()
    if not nazwisko:
        print("Nazwisko nie może być puste.")
        return
    przedmioty = input("Przedmioty (oddziel przecinkiem): ").strip()
    if przedmioty:
        przedmioty = [p.strip() for p in przedmioty.split(",")]  # Zamiana na listę
    else:
        przedmioty = []
    klasa_wychowawcza = input("Klasa wychowawcza (lub pozostaw puste): ").strip()
    wychowawca = Wychowawca(imie, nazwisko, przedmioty, klasa_wychowawcza if klasa_wychowawcza else None)
    lista_wychowawcow.append(wychowawca)
    print("Wychowawca dodany.")


def pokaz_wychowawcow():
    # Wyświetla wszystkich wychowawców
    if not lista_wychowawcow:
        print("Brak wychowawców.")
        return
    print("\nLista wychowawców:")
    for i, w in enumerate(lista_wychowawcow, 1):
        klasa = w.klasa_wychowawcza if w.klasa_wychowawcza else "brak"
        przedmioty = ", ".join(w.przedmioty) if w.przedmioty else "brak"
        print(f"{i}. {w.pelne_imie()} | Klasa wychowawcza: {klasa} | Przedmioty: {przedmioty}")


def usun_wychowawce():
    # Usuwa wychowawcę z listy
    pokaz_wychowawcow()
    if not lista_wychowawcow:
        return
    nr = int(input("Numer wychowawcy do usunięcia: "))
    if 1 <= nr <= len(lista_wychowawcow):
        usuniety = lista_wychowawcow.pop(nr - 1)
        print(f"Wychowawca {usuniety.pelne_imie()} został usunięty.")
    else:
        print("Niepoprawny numer.")


def edytuj_wychowawce():
    # Edytuje dane wybranego wychowawcy
    pokaz_wychowawcow()
    if not lista_wychowawcow:
        return
    nr = int(input("Numer wychowawcy do edycji: "))
    if 1 <= nr <= len(lista_wychowawcow):
        wych = lista_wychowawcow[nr - 1]
        print(f"Edytujesz: {wych.pelne_imie()}")

        # Można zostawić puste, żeby nie zmieniać
        nowe_imie = input(f"Nowe imię (enter = bez zmian) [{wych.imie}]: ").strip()
        if nowe_imie:
            wych.imie = nowe_imie

        nowe_nazwisko = input(f"Nowe nazwisko (enter = bez zmian) [{wych.nazwisko}]: ").strip()
        if nowe_nazwisko:
            wych.nazwisko = nowe_nazwisko

        nowe_przedmioty = input(
            f"Nowe przedmioty, oddzielone przecinkiem (enter = bez zmian) [{', '.join(wych.przedmioty)}]: ").strip()
        if nowe_przedmioty:
            wych.przedmioty = [p.strip() for p in nowe_przedmioty.split(",")]

        nowa_klasa = input(
            f"Nowa klasa wychowawcza (enter = bez zmian) [{wych.klasa_wychowawcza if wych.klasa_wychowawcza else 'brak'}]: ").strip()
        if nowa_klasa:
            wych.klasa_wychowawcza = nowa_klasa

        print("Dane wychowawcy zostały zaktualizowane.")
    else:
        print("Niepoprawny numer.")


def wyszukaj_wychowawce():
    # Wyszukuje wychowawcę po imieniu, nazwisku lub przedmiocie
    if not lista_wychowawcow:
        print("Brak wychowawców w systemie.")
        return
    fraza = input("Podaj imię, nazwisko lub przedmiot do wyszukania: ").strip().lower()
    wyniki = []
    for w in lista_wychowawcow:
        if (fraza in w.imie.lower() or
                fraza in w.nazwisko.lower() or
                any(fraza in p.lower() for p in w.przedmioty)):
            wyniki.append(w)
    if not wyniki:
        print("Nie znaleziono wychowawców pasujących do wyszukiwania.")
        return
    print(f"Znaleziono {len(wyniki)} wychowawców:")
    for i, w in enumerate(wyniki, 1):
        klasa = w.klasa_wychowawcza if w.klasa_wychowawcza else "brak"
        przedmioty = ", ".join(w.przedmioty) if w.przedmioty else "brak"
        print(f"{i}. {w.pelne_imie()} | Klasa wychowawcza: {klasa} | Przedmioty: {przedmioty}")

