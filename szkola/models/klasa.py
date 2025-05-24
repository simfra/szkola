class Klasa:
    # Konstruktor klasy Klasa
    def __init__(self, nazwa, wychowawca=None):
        self.nazwa = nazwa  # nazwa klasy, np. "3A"
        self.wychowawca = wychowawca  # wychowawca przypisany do klasy (może być None)
        self.uczniowie = []   # lista uczniów w klasie (obiekty klasy Uczen)
        self.nauczyciele = [] # lista nauczycieli przypisanych do klasy (obiekty klasy Nauczyciel)

    # Dodaje ucznia do klasy, jeśli nie jest już dodany
    def dodaj_ucznia(self, uczen):
        if uczen not in self.uczniowie:
            self.uczniowie.append(uczen)

    # Usuwa ucznia z klasy, jeśli istnieje
    def usun_ucznia(self, uczen):
        if uczen in self.uczniowie:
            self.uczniowie.remove(uczen)

    # Dodaje nauczyciela do klasy, jeśli nie jest już przypisany
    def dodaj_nauczyciela(self, nauczyciel):
        if nauczyciel not in self.nauczyciele:
            self.nauczyciele.append(nauczyciel)

    # Usuwa nauczyciela z klasy, jeśli jest przypisany
    def usun_nauczyciela(self, nauczyciel):
        if nauczyciel in self.nauczyciele:
            self.nauczyciele.remove(nauczyciel)

    # Zwraca listę uczniów w klasie jako tekst
    def pokaz_uczniow(self):
        if not self.uczniowie:
            return "Brak uczniów w tej klasie."
        return ", ".join([f"{u.imie} {u.nazwisko}" for u in self.uczniowie])

    # Zwraca listę nauczycieli przypisanych do klasy jako tekst
    def pokaz_nauczycieli(self):
        if not self.nauczyciele:
            return "Brak nauczycieli przypisanych do tej klasy."
        return ", ".join([f"{n.imie} {n.nazwisko}" for n in self.nauczyciele])

