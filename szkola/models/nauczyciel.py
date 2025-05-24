from models.osoba import Osoba

# Klasa Nauczyciel dziedziczy po klasie Osoba
class Nauczyciel(Osoba):
    # Konstruktor nauczyciela
    def __init__(self, imie, nazwisko, email=None, telefon=None, etat="pełny etat"):
        super().__init__(imie, nazwisko, email, telefon)  # wywołanie konstruktora klasy nadrzędnej (Osoba)
        self.etat = etat  # etat nauczyciela (np. "pełny etat", "pół etatu")
        self.przedmioty = []  # lista przedmiotów, których nauczyciel uczy (obiekty klasy Przedmiot)

    # Dodaje przedmiot do listy przedmiotów, jeśli jeszcze go tam nie ma
    def dodaj_przedmiot(self, przedmiot):
        if przedmiot not in self.przedmioty:
            self.przedmioty.append(przedmiot)

    # Usuwa przedmiot z listy, jeśli istnieje
    def usun_przedmiot(self, przedmiot):
        if przedmiot in self.przedmioty:
            self.przedmioty.remove(przedmiot)

    # Zwraca listę przedmiotów jako tekst (lub info, że brak)
    def pokaz_przedmioty(self):
        if not self.przedmioty:
            return "Brak przypisanych przedmiotów"
        return ", ".join([str(p) for p in self.przedmioty])
