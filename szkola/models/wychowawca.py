from models.nauczyciel import Nauczyciel

# Klasa Wychowawca dziedziczy po klasie Nauczyciel i reprezentuje wychowawcę klasy
class Wychowawca(Nauczyciel):
    def __init__(self, imie, nazwisko, przedmioty, klasa_wychowawcza):
        # Wywołanie konstruktora klasy nadrzędnej Nauczyciel z imieniem, nazwiskiem i przedmiotami
        super().__init__(imie, nazwisko, przedmioty)
        self.klasa_wychowawcza = klasa_wychowawcza  # Przechowuje nazwę klasy, której wychowawcą jest ta osoba

    def pelne_imie(self):
        # Zwraca pełne imię i nazwisko wychowawcy
        return f"{self.imie} {self.nazwisko}"
