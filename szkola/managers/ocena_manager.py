from managers.uczen_manager import lista_uczniow

# Funkcja dodaje ocenę do wybranego ucznia
def dodaj_ocene():
    if not lista_uczniow:
        print("Brak uczniów. Najpierw dodaj uczniów.")
        return
    pokaz_uczniow()

    nr_str = input("Podaj numer ucznia, któremu chcesz dodać ocenę: ")
    if not nr_str.isdigit():
        print("Podaj poprawny numer.")
        return

    nr = int(nr_str)
    if 1 <= nr <= len(lista_uczniow):
        ocena = input("Podaj ocenę (np. 5, 4+, 3-): ")
        lista_uczniow[nr - 1].dodaj_ocene(ocena)
        print(f"Dodano ocenę {ocena} uczniowi {lista_uczniow[nr - 1].imie} {lista_uczniow[nr - 1].nazwisko}.")
    else:
        print("Niepoprawny numer.")

# Funkcja pokazuje oceny wybranego ucznia
def pokaz_oceny_ucznia():
    if not lista_uczniow:
        print("Brak uczniów.")
        return
    pokaz_uczniow()

    nr_str = input("Podaj numer ucznia, którego oceny chcesz zobaczyć: ")
    if not nr_str.isdigit():
        print("Podaj poprawny numer.")
        return

    nr = int(nr_str)
    if 1 <= nr <= len(lista_uczniow):
        oceny = lista_uczniow[nr - 1].pokaz_oceny()
        print(f"Oceny ucznia {lista_uczniow[nr - 1].imie} {lista_uczniow[nr - 1].nazwisko}: {oceny}")
    else:
        print("Niepoprawny numer.")

# Funkcja usuwa ocenę wybranego ucznia
def usun_ocene():
    if not lista_uczniow:
        print("Brak uczniów.")
        return
    pokaz_uczniow()

    nr_str = input("Podaj numer ucznia, którego ocenę chcesz usunąć: ")
    if not nr_str.isdigit():
        print("Podaj poprawny numer.")
        return
    nr_ucznia = int(nr_str)

    if 1 <= nr_ucznia <= len(lista_uczniow):
        uczen = lista_uczniow[nr_ucznia - 1]
        if not uczen.oceny:
            print("Uczeń nie ma żadnych ocen.")
            return

        print(f"Oceny ucznia {uczen.imie} {uczen.nazwisko}:")
        for i, o in enumerate(uczen.oceny, 1):
            print(f"{i}. {o}")

        nr_oceny_str = input("Podaj numer oceny do usunięcia: ")
        if not nr_oceny_str.isdigit():
            print("Podaj poprawny numer.")
            return

        nr_oceny = int(nr_oceny_str)
        if 1 <= nr_oceny <= len(uczen.oceny):
            usunieta = uczen.oceny.pop(nr_oceny - 1)
            print(f"Usunięto ocenę {usunieta}.")
        else:
            print("Niepoprawny numer oceny.")
    else:
        print("Niepoprawny numer ucznia.")

# Funkcja edytuje ocenę wybranego ucznia
def edytuj_ocene():
    if not lista_uczniow:
        print("Brak uczniów.")
        return
    pokaz_uczniow()

    nr_str = input("Podaj numer ucznia, którego ocenę chcesz edytować: ")
    if not nr_str.isdigit():
        print("Podaj poprawny numer.")
        return
    nr_ucznia = int(nr_str)

    if 1 <= nr_ucznia <= len(lista_uczniow):
        uczen = lista_uczniow[nr_ucznia - 1]
        if not uczen.oceny:
            print("Uczeń nie ma żadnych ocen.")
            return

        print(f"Oceny ucznia {uczen.imie} {uczen.nazwisko}:")
        for i, o in enumerate(uczen.oceny, 1):
            print(f"{i}. {o}")

        nr_oceny_str = input("Podaj numer oceny do edycji: ")
        if not nr_oceny_str.isdigit():
            print("Podaj poprawny numer.")
            return

        nr_oceny = int(nr_oceny_str)
        if 1 <= nr_oceny <= len(uczen.oceny):
            nowa_ocena = input("Podaj nową wartość oceny: ")
            stara = uczen.oceny[nr_oceny - 1]
            uczen.oceny[nr_oceny - 1] = nowa_ocena
            print(f"Ocenę {stara} zmieniono na {nowa_ocena}.")
        else:
            print("Niepoprawny numer oceny.")
    else:
        print("Niepoprawny numer ucznia.")

# Funkcja liczy i pokazuje średnią ocen wszystkich uczniów
def statystyki_ocen():
    if not lista_uczniow:
        print("Brak uczniów.")
        return
    suma_ocen = 0
    liczba_ocen = 0
    skala_ocen = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6}
    for uczen in lista_uczniow:
        for ocena in uczen.oceny:
            oc = ocena[0]
            if oc in skala_ocen:
                suma_ocen += skala_ocen[oc]
                liczba_ocen += 1
    if liczba_ocen == 0:
        print("Brak ocen do statystyk.")
    else:
        print(f"Średnia ocen wszystkich uczniów: {suma_ocen / liczba_ocen:.2f}")

# Funkcja pokazuje listę wszystkich uczniów
def pokaz_uczniow():
    if not lista_uczniow:
        print("Brak uczniów.")
    else:
        print("\nLista uczniów:")
        for i, u in enumerate(lista_uczniow, 1):
            print(f"{i}. {u}")

# Główne menu do zarządzania ocenami
def zarzadzaj_ocenami():
    while True:
        print("\n--- Zarządzanie ocenami ---")
        print("1. Dodaj ocenę uczniowi")
        print("2. Pokaż oceny ucznia")
        print("3. Usuń ocenę ucznia")
        print("4. Edytuj ocenę ucznia")
        print("5. Statystyki ocen")
        print("0. Powrót do menu głównego")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_ocene()
        elif wybor == "2":
            pokaz_oceny_ucznia()
        elif wybor == "3":
            usun_ocene()
        elif wybor == "4":
            edytuj_ocene()
        elif wybor == "5":
            statystyki_ocen()
        elif wybor == "0":
            break
        else:
            print("Niepoprawny wybór.")
