from managers.przedmiot_manager import zarzadzaj_przedmiotami
from managers.uczen_manager import zarzadzaj_uczniami
from managers.nauczyciel_manager import zarzadzaj_nauczycielami
from managers.wychowawca_manager import zarzadzaj_wychowawcami
from managers.klasa_manager import zarzadzaj_klasami
from managers.szkola_manager import zarzadzaj_szkolą

# Funkcja wyświetlająca główne menu programu i obsługująca wybór użytkownika
def menu_glowne():
    while True:
        print("\n--- MENU GŁÓWNE ---")
        print("1. Zarządzaj uczniami")
        print("2. Zarządzaj nauczycielami")
        print("3. Zarządzaj wychowawcami")
        print("4. Zarządzaj klasami")
        print("5. Zarządzaj przedmiotami")
        print("6. Zarządzaj szkołą")
        print("0. Wyjście")

        wybor = input("Wybierz opcję: ")

        # Obsługa wyboru użytkownika - wywołanie odpowiednich funkcji zarządzania
        if wybor == "1":
            zarzadzaj_uczniami()      # Przejście do zarządzania uczniami
        elif wybor == "2":
            zarzadzaj_nauczycielami() # Przejście do zarządzania nauczycielami
        elif wybor == "3":
            zarzadzaj_wychowawcami()  # Przejście do zarządzania wychowawcami
        elif wybor == "4":
            zarzadzaj_klasami()       # Przejście do zarządzania klasami
        elif wybor == "5":
            zarzadzaj_przedmiotami()  # Przejście do zarządzania szkołą
        elif wybor == "6":
            zarzadzaj_szkolą()        # Przejście do zarządzania szkołą
        elif wybor == "0":
            print("Do widzenia!")      # Wyjście z programu
            break
        else:
            print("Niepoprawny wybór.") # Obsługa niepoprawnej opcji
