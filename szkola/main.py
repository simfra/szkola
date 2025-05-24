from utils.menu import menu_glowne

# Funkcja wyświetlająca powitalny napis na ekranie
def wyswietl_napis_powitalny():
    print("=" * 40)  # linia złożona z 40 znaków "=" jako ramka
    print("   SYSTEM ZARZĄDZANIA SZKOŁĄ  ")  # tytuł systemu
    print("=" * 40)  # linia zamykająca ramkę
    print()  # pusta linia dla czytelności

# Główna część programu uruchamiana tylko, gdy plik jest wykonywany bezpośrednio
if __name__ == "__main__":
    wyswietl_napis_powitalny()  # wyświetla napis powitalny
    menu_glowne()  # uruchamia główne menu programu
