from mlist import MList
poprawnalista = False

rozmiar = int(input("Podaj poczatkowy rozmiar listy:"))
while poprawnalista is False:

    try:
        mlist = MList(rozmiar)
        poprawnalista = True
    except ValueError as e:
        print(e)
        rozmiar = int(input("Podaj poczatkowy rozmiar listy:"))

while True:
    print("Wybierz polecenie (pisz, dodaj_element,")
    print("znajdz, pobierz, rozmiar, pojemnosc, usun_powtorzenia")
    print("odwroc, zwieksz_pojemnosc, zmniejsz_pojemnosc, wyjscie):")
    wybor = input()

    if "pisz" == wybor:
        mlist.pisz()
    elif "dodaj_element" == wybor:
        warosc = int(input("Podaj wartosc elementu: "))
        if not mlist.dodaj_element(warosc):
            print("Blad. nie udało sie dodac elementu do listy")
    elif "znajdz" == wybor:
        warosc = int(input("Podaj szukanką wartosc: "))
        indeks = mlist.znajdz(warosc)
        if indeks >= 0:
            print("Szukany element znajduje sie pod indeksem: ", indeks)
        else:
            print("Nie znaleziono szukanego elementu")
    elif "pobierz" == wybor:
        warosc = int(input("Podaj indeks: "))
        try:
            print(mlist.pobierz(warosc))
        except IndexError as e:
            print(e)
    elif "rozmiar" == wybor:
        print(mlist.rozmiar())
    elif "pojemnosc" == wybor:
        print(mlist.pojemnosc())
    elif "usun_powtorzenia" == wybor:
        warosc = int(input("Podaj wartosc: "))
        mlist.usun_powtorzenia(warosc)
    elif "odwroc" == wybor:
        mlist.odwroc()
    elif "zwieksz_pojemnosc" == wybor:
        if not mlist.zwieksz_pojemnosc(warosc):
            print("Wystapil blad.")
    elif "zmniejsz_pojemnosc" == wybor:
        warosc = int(input("Podaj wartosc: "))
        if not mlist.zmniejsz_pojemnosc(warosc):
            print("Wystapil blad.")
    elif "wyjscie" == wybor:
        exit(0)
