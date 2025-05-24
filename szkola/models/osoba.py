# Klasa Osoba przechowuje podstawowe dane o osobie
class Osoba:
    def __init__(self, imie, nazwisko, email=None, telefon=None):
        # Imię osoby
        self.imie = imie
        # Nazwisko osoby
        self.nazwisko = nazwisko
        # Adres e-mail (opcjonalnie)
        self.email = email
        # Numer telefonu (opcjonalnie)
        self.telefon = telefon

    def pelne_imie(self):
        # Zwraca pełne imię i nazwisko
        return f"{self.imie} {self.nazwisko}"

    def dane_kontaktowe(self):
        # Zwraca dane kontaktowe lub "brak", jeśli nie podano
        return f"Email: {self.email or 'brak'}, Telefon: {self.telefon or 'brak'}"
