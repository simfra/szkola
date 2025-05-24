# Importujemy funkcje zarządzające klasami, wychowawcami i uczniami
from managers.klasa_manager import zarzadzaj_klasami
from managers.wychowawca_manager import zarzadzaj_wychowawcami
from managers.uczen_manager import zarzadzaj_uczniami

# Zmienna globalna, w której przechowujemy nazwę szkoły
nazwa_szkoly = None

# Funkcja do ustawiania lub edytowania nazwy szkoły
def ustaw_lub_edytuj_nazwe_szkoly():
    global nazwa_szkoly  # pozwala modyfikować globalną zmienną
    if nazwa_szkoly:
        # Jeśli nazwa już istnieje, pokazujemy ją
        print(f"Aktualna nazwa szkoły: {nazwa_szkoly}")
        # Pytamy użytkownika o nową nazwę
        nowa_nazwa = input("Wpisz nową nazwę szkoły (enter = brak zmian): ").strip()
        if nowa_nazwa:
            # Jeśli użytkownik coś wpisał, zmieniamy nazwę
            nazwa_szkoly = nowa_nazwa
            print(f"Nazwa szkoły została zmieniona na: {nazwa_szkoly}")
        else:
            print("Nazwa szkoły nie została zmieniona.")
    else:
        # Jeśli nazwa jeszcze nie została ustawiona
        nazwa_szkoly = input("Wpisz nazwę szkoły: ").strip()
        if nazwa_szkoly:
            print(f"Nazwa szkoły ustawiona na: {nazwa_szkoly}")
        else:
            nazwa_szkoly = None
            print("Nie podano nazwy szkoły.")

# Funkcja pokazująca aktualną nazwę szkoły
def pokaz_nazwe_szkoly():
    if nazwa_szkoly:
        print(f"\n*** Aktualna nazwa szkoły: {nazwa_szkoly} ***\n")
    else:
        print("\n*** Nazwa szkoły nie została jeszcze ustawiona ***\n")

# Główna funkcja zarządzająca szkołą – menu główne
def zarzadzaj_szkolą():
    while True:
        print("=== Zarządzanie szkołą ===")
        print("1. Ustaw/edytuj nazwę szkoły")
        print("2. Pokaż nazwę szkoły")
        print("3. Zarządzaj klasami")
        print("4. Zarządzaj wychowawcami")
        print("5. Zarządzaj uczniami")
        print("0. Wyjdź do menu głownego")

        wybor = input("Wybierz opcję: ").strip()

        # Wywołujemy odpowiednią funkcję w zależności od wyboru
        if wybor == "1":
            ustaw_lub_edytuj_nazwe_szkoly()
        elif wybor == "2":
            pokaz_nazwe_szkoly()
        elif wybor == "3":
            zarzadzaj_klasami()
        elif wybor == "4":
            zarzadzaj_wychowawcami()
        elif wybor == "5":
            zarzadzaj_uczniami()
        elif wybor == "0":
            print("Do widzenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
