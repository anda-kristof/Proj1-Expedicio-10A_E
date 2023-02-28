from unittest import TestCase
from Megoldas import Megoldas


class TestMegoldas(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.üzenet_adatok: Megoldas = Megoldas("veetel.txt")

    def írott_fájl(self):
        with open("adaas.txt", "r", encoding="utf-8") as file:
            return file.read()

    def minta_fájl(self):
        with open("adaas_minta.txt", "r", encoding="utf-8") as file:
            return file.read()

    def test_első_és_utolsó_üzenet(self) -> None:
        self.assertEqual(self.üzenet_adatok.első_utolsó_küldő[0], 13)
        self.assertEqual(self.üzenet_adatok.első_utolsó_küldő[1], 18)

    def test_nap_rádióamatőr_feljegyzés(self) -> None:
        self.assertEqual(self.üzenet_adatok.mennyi_üzenet[1], 13)

    def test_adaas_fájl(self) -> None:
        self.assertEqual(self.írott_fájl(), self.minta_fájl())

    def egyedek_szama(self) -> None:
        self.assertEqual(self.üzenet_adatok.egyedek_száma(self.üzenet_adatok.megadott_üzenet(6, 19)), "Nincs információ")
        self.assertEqual(self.üzenet_adatok.egyedek_száma(self.üzenet_adatok.megadott_üzenet(3, 10)), 5)
