import unittest
from mlist import MList


class MListTest(unittest.TestCase):

    def setUp(self):
        self.mlist = MList(5)

    def test_m_pojemnosc_zwraca_wartosc_10_dla_nowej_listy_10elementowej(self):
        self.assertEqual(self.mlist.pojemnosc(), 5)

    def test_m_rozmiar_zwraca_wartosc_0_dla_nowe_10lementowej_listy(self):
        self.assertEqual(self.mlist.rozmiar(), 0)

    def test_tworzenie_listy_z_ujemna_wartoscia_konczy_sie_błedem(self):
        with self.assertRaises(ValueError):
            newmlist = MList(-1)

    def test_nowy_element_zwieksza_rozmiar_o_1_pojemnoscZostajeBezZmian_(self):
        self.assertEqual(self.mlist.pojemnosc(), 5)
        self.assertEqual(self.mlist.rozmiar(), 0)

        self.assertTrue(self.mlist.dodaj_element(20))
        self.assertEqual(self.mlist.pojemnosc(), 5)
        self.assertEqual(self.mlist.rozmiar(), 1)

    def test_dod_now_ele_do_zapelnionej_lis_nie_zm_jej_roz_i_zwr_false(self):
        mlist = MList(1)
        self.assertEqual(mlist.pojemnosc(), 1)
        self.assertEqual(mlist.rozmiar(), 0)

        mlist.dodaj_element(3)
        self.assertEqual(mlist.pojemnosc(), 1)
        self.assertEqual(mlist.rozmiar(), 1)

        self.assertFalse(mlist.dodaj_element(99))
        self.assertEqual(mlist.pojemnosc(), 1)
        self.assertEqual(mlist.rozmiar(), 1)

    def test_wywolanie_metody_znajdz_z_wartoscia_5_zwroci_index_2(self):
        self.mlist.dodaj_element(4)
        self.mlist.dodaj_element(2)
        self.mlist.dodaj_element(5)
        self.mlist.dodaj_element(65)
        self.mlist.dodaj_element(3)

        self.assertEqual(self.mlist.znajdz(5), 2)

    def test_wyw_me_znajdz_z_wart_ktr_nie_znaj_sie_w_lisc_zwr_m1(self):
        self.mlist.dodaj_element(4)
        self.mlist.dodaj_element(2)
        self.mlist.dodaj_element(5)
        self.mlist.dodaj_element(65)

        self.assertEqual(self.mlist.znajdz(6), -1)

    def test_metoda_pobierz_zwrace_element_o_indeksie_x(self):
        mlist = MList(5)
        mlist.dodaj_element(3)
        mlist.dodaj_element(2)

        self.assertEqual(mlist.pobierz(0), 3)
        self.assertEqual(mlist.pobierz(1), 2)

    def test_odwol_sie_do_nieistn_indexu_rzuci_wyjatekiem_IndexError(self):
        mlist = MList(2)
        mlist.dodaj_element(3)
        with self.assertRaises(IndexError):
            mlist.pobierz(1)

    def test_metoda_usun_powtorzenia(self):
        self.mlist.dodaj_element(1)
        self.mlist.dodaj_element(2)
        self.mlist.dodaj_element(3)
        self.mlist.dodaj_element(1)
        self.mlist.dodaj_element(2)
        self.mlist.dodaj_element(1)
        self.mlist.usun_powtorzenia(1)
        self.assertEqual(self.mlist.pobierz(0), 1)
        self.assertEqual(self.mlist.pobierz(3), 2)
        self.assertEqual(self.mlist.rozmiar(), 4)

    def test_metoda_odwroc_odwraca_kolejnosc_elementow_na_liscie(self):
        mlista = MList(3)
        mlista.dodaj_element(2)
        mlista.dodaj_element(6)
        mlista.dodaj_element(4)

        self.assertEqual(mlista.pobierz(0), 2)
        self.assertEqual(mlista.pobierz(1), 6)
        self.assertEqual(mlista.pobierz(2), 4)

        mlista.odwroc()

        self.assertEqual(mlista.pobierz(0), 4)
        self.assertEqual(mlista.pobierz(1), 6)
        self.assertEqual(mlista.pobierz(2), 2)

        mlista.odwroc()

        self.assertEqual(mlista.pobierz(0), 2)
        self.assertEqual(mlista.pobierz(1), 6)
        self.assertEqual(mlista.pobierz(2), 4)

    def test_me_zwieksz_pojemnosc_zwiek_capacity_listy_i_zwrTrue(self):
        mlista = MList(1)
        mlista.dodaj_element(99)
        self.assertEqual(mlista.pojemnosc(), 1)
        self.assertEqual(mlista.rozmiar(), 1)

        self.assertTrue(mlista.zwieksz_pojemnosc(2))
        self.assertEqual(mlista.pojemnosc(), 3)
        self.assertEqual(mlista.rozmiar(), 1)

        mlista.dodaj_element(77)
        mlista.dodaj_element(88)
        self.assertEqual(mlista.pojemnosc(), 3)
        self.assertEqual(mlista.rozmiar(), 3)
        self.assertEqual(mlista.pobierz(1), 77)
        self.assertEqual(mlista.pobierz(2), 88)

    def test_m_zw_poj_wywolana_z_ujemna_wart_nie_zmienia_poje_i_zwrFalse(self):
        mlista = MList(1)
        self.assertEqual(mlista.pojemnosc(), 1)
        self.assertEqual(mlista.rozmiar(), 0)

        self.assertFalse(mlista.zwieksz_pojemnosc(-1))
        self.assertEqual(mlista.pojemnosc(), 1)
        self.assertEqual(mlista.rozmiar(), 0)

    def test_zmiejsz_pojemnosc_dla_poprawnych_danych_wjesciowych(self):
        mlista = MList(5)
        self.assertTrue(mlista.zmniejsz_pojemnosc(2))
        self.assertEqual(mlista.pojemnosc(), 3)

    def test_podanie_ujemnej_warosci_jako_arg_nie_zmienia_poj_i_zwrFalse(self):
        mlista = MList(5)
        self.assertFalse(mlista.zmniejsz_pojemnosc(-2))
        self.assertEqual(mlista.pojemnosc(), 5)

    def test_proba_zmniej_poje_poni_liosci_elem_nie_zm_poje_i_zwrFalse(self):
        mlista = MList(4)
        mlista.dodaj_element(99)
        mlista.dodaj_element(88)

        self.assertFalse(mlista.zmniejsz_pojemnosc(3))
        self.assertEqual(mlista.pojemnosc(), 4)

        self.assertTrue(mlista.zmniejsz_pojemnosc(2))
        self.assertEqual(mlista.pojemnosc(), 2)
