from unittest import TestCase
from Uzenet import Uzenet


class TestUzenet(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.uzenet1: Uzenet = Uzenet('1 13', '#abor# #e#tun###agy#szel#2# #o##h#d#g ##rkasn#o#oka# #a#tunk e####a#akn##$#$#$##$$$$$$####')
        cls.uzenet2: Uzenet = Uzenet('1 19', 'ta###t##ertunk ##gy #zel#####ok hide##f#r##sn#omo#at ##ttu## e#y patak#al$#$$$$$###$$$$$$$')
        cls.uzenet3: Uzenet = Uzenet('6 19', '0/# a #a#akon##uli ##mb## ##l#kok jatszo#####del ####l$$$#$$$$$#$#$#$#$$###$##$$##$$$$#$$$')
        
        
    def test_napsorszám(self) -> None:
        self.assertEqual(self.uzenet1.nap_sorszáma, 1)
        self.assertEqual(self.uzenet2.nap_sorszáma, 1)
        self.assertEqual(self.uzenet3.nap_sorszáma, 6)
        
    def test_radioamator_sorszama(self) -> None:
        self.assertEqual(self.uzenet1.rádióamatőr_sorszáma, 13)
        self.assertEqual(self.uzenet2.rádióamatőr_sorszáma, 19)
        self.assertEqual(self.uzenet3.rádióamatőr_sorszáma, 19)
        
    def test_radio_uzenet(self) -> None:
        self.assertEqual(self.uzenet1.rádió_üzenet, "#abor# #e#tun###agy#szel#2# #o##h#d#g ##rkasn#o#oka# #a#tunk e####a#akn##$#$#$##$$$$$$####")
        self.assertEqual(self.uzenet2.rádió_üzenet, "ta###t##ertunk ##gy #zel#####ok hide##f#r##sn#omo#at ##ttu## e#y patak#al$#$$$$$###$$$$$$$")
        self.assertEqual(self.uzenet3.rádió_üzenet, "0/# a #a#akon##uli ##mb## ##l#kok jatszo#####del ####l$$$#$$$$$#$#$#$#$$###$##$$##$$$$#$$$")
        