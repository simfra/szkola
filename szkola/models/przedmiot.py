# Klasa Przedmiot reprezentuje przedmiot szkolny, np. matematyka, historia itp.
class Przedmiot:
    def __init__(self, nazwa, opis, poziom_trudnosci="średni"):
        # Nazwa przedmiotu (np. "Matematyka")
        self.nazwa = nazwa
        # Opis przedmiotu (np. "Przedmiot naukowy")
        self.opis = opis
        # Poziom trudności (np. "łatwy", "średni", "trudny")
        self.poziom_trudnosci = poziom_trudnosci
