# Klasa Ocena przechowuje informację o ocenie ucznia z danego przedmiotu
class Ocena:
    def __init__(self, uczen_id, przedmiot_id, wartosc):
        # ID ucznia, który otrzymał ocenę
        self.uczen_id = uczen_id
        # ID przedmiotu, z którego jest ta ocena
        self.przedmiot_id = przedmiot_id
        # Wartość oceny (np. 5, 4+, 3-)
        self.wartosc = wartosc
