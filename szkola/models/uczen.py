from models.osoba import Osoba

# Klasa Uczen dziedziczy po klasie Osoba i reprezentuje ucznia
class Uczen(Osoba):
    def __init__(self, imie, nazwisko, klasa):
        super().__init__(imie, nazwisko)  # Wywołanie konstruktora klasy bazowej Osoba
        self.klasa = klasa                # Przechowuje nazwę klasy, do której uczęszcza uczeń
        self.oceny = []                   # Lista ocen ucznia

    def dodaj_ocene(self, ocena):
        # Dodaje ocenę do listy ocen ucznia
        self.oceny.append(ocena)

    def pokaz_oceny(self):
        # Zwraca oceny jako tekst, lub informację, że brak ocen
        if not self.oceny:
            return "Brak ocen"
        return ", ".join([str(o) for o in self.oceny])

    def pelne_imie(self):
        # Zwraca pełne imię i nazwisko ucznia
        return f"{self.imie} {self.nazwisko}"
