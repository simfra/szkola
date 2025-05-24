from models.przedmiot import Przedmiot

# Lista przechowująca wszystkie przedmioty
lista_przedmiotow = []

# Funkcja dodająca nowy przedmiot do systemu
def dodaj_przedmiot():
    print("\n--- Dodawanie nowego przedmiotu ---")
    nazwa = input("Podaj nazwę przedmiotu: ").strip()
    opis = input("Podaj krótki opis przedmiotu: ").strip()
    poziom_trudnosci = input("Podaj poziom trudności (łatwy, średni, trudny) [domyślnie: średni]: ").strip()
    if poziom_trudnosci not in ["łatwy", "średni", "trudny"]:
        poziom_trudnosci = "średni"  # ustawiamy domyślny poziom trudności
    przedmiot = Przedmiot(nazwa, opis, poziom_trudnosci)
    lista_przedmiotow.append(przedmiot)
    print("Przedmiot został dodany.")

# Funkcja wyświetlająca wszystkie przedmioty w systemie
def pokaz_przedmioty():
    if not lista_przedmiotow:
        print("Brak przedmiotów w systemie.")
        return
    print("\nLista przedmiotów:")
    for i, p in enumerate(lista_przedmiotow, 1):
        print(f"{i}. {p.nazwa} - {p.opis} (Poziom trudności: {p.poziom_trudnosci})")

# Funkcja usuwająca wybrany przedmiot
def usun_przedmiot():
    pokaz_przedmioty()
    if not lista_przedmiotow:
        return
    try:
        nr = int(input("Podaj numer przedmiotu do usunięcia: "))
        if 1 <= nr <= len(lista_przedmiotow):
            usuniety = lista_przedmiotow.pop(nr - 1)
            print(f"Przedmiot '{usuniety.nazwa}' został usunięty.")
        else:
            print("Niepoprawny numer.")
    except ValueError:
        print("Musisz podać poprawny numer.")

# Funkcja edytująca dane istniejącego przedmiotu
def edytuj_przedmiot():
    pokaz_przedmioty()
    if not lista_przedmiotow:
        return
    try:
        nr = int(input("Numer przedmiotu do edycji: "))
        if 1 <= nr <= len(lista_przedmiotow):
            przedmiot = lista_przedmiotow[nr - 1]
            print(f"Edytujesz przedmiot: {przedmiot.nazwa}")
            nowa_nazwa = input(f"Nowa nazwa [{przedmiot.nazwa}]: ").strip() or przedmiot.nazwa
            nowy_opis = input(f"Nowy opis [{przedmiot.opis}]: ").strip() or przedmiot.opis
            przedmiot.nazwa = nowa_nazwa
            przedmiot.opis = nowy_opis
            print("Dane przedmiotu zostały zaktualizowane.")
        else:
            print("Niepoprawny numer.")
    except ValueError:
        print("Musisz podać poprawny numer.")

# Funkcja wyszukująca przedmioty po nazwie lub opisie
def wyszukaj_przedmiot():
    fraza = input("Podaj frazę do wyszukania: ").strip().lower()
    znalezione = [p for p in lista_przedmiotow if fraza in p.nazwa.lower() or fraza in p.opis.lower()]
    if znalezione:
        print("Znalezione przedmioty:")
        for p in znalezione:
            print(f"- {p.nazwa} - {p.opis} (Poziom trudności: {p.poziom_trudnosci})")
    else:
        print("Nie znaleziono żadnych przedmiotów.")

# Funkcja sortująca przedmioty alfabetycznie po nazwie
def sortuj_przedmioty():
    lista_przedmiotow.sort(key=lambda p: p.nazwa.lower())
    print("Lista przedmiotów została posortowana alfabetycznie.")

# Główna funkcja do zarządzania przedmiotami
def zarzadzaj_przedmiotami():
    while True:
        print("\n--- Zarządzanie przedmiotami ---")
        print("1. Dodaj przedmiot")
        print("2. Pokaż przedmioty")
        print("3. Usuń przedmiot")
        print("4. Edytuj przedmiot")
        print("5. Wyszukaj przedmiot")
        print("6. Sortuj przedmioty")
        print("0. Powrót do menu głównego")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_przedmiot()
        elif wybor == "2":
            pokaz_przedmioty()
        elif wybor == "3":
            usun_przedmiot()
        elif wybor == "4":
            edytuj_przedmiot()
        elif wybor == "5":
            wyszukaj_przedmiot()
        elif wybor == "6":
            sortuj_przedmioty()
        elif wybor == "0":
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
