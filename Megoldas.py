from üzenet import üzenet


class Megoldas:
    _üzenetek: list[üzenet]

    @property
    def első_utolsó_küldő(self):
        első_üzenet_rögzítője: int = self._üzenetek[0].rádióamatőr_sorszáma
        utolsó_üzenet_rögzítője: int = self._üzenetek[len(self._üzenetek) - 1].rádióamatőr_sorszáma
        return f"2. feladat:\nAz első üzenet rögzítője: {első_üzenet_rögzítője}\nAz utolsó üzenet rógzítője: {utolsó_üzenet_rögzítője}"

    def __init__(self, forrásnév: str):
        self._üzenetek: list[üzenet] = []
        sor_száma: int = 1
        with open(forrásnév, 'r', encoding='utf-8') as file:
            fájl: str = file.read()
            for sor in fájl.splitlines():
                sor_száma2: int = sor_száma - 1
                sor1: str = fájl.splitlines()[sor_száma2]
                sor2: str = fájl.splitlines()[sor_száma]
                if sor_száma % 2 != 0:
                    self._üzenetek.append(üzenet(sor1, sor2))
                sor_száma += 1
                if sor_száma == len(fájl.splitlines()):
                    break

    def melyik_üzenetben_van_a_szöveg(self, szöveg: str):
        for adat in self._üzenetek:
            if szöveg in adat.rádió_üzenet:
                print(f'{adat.nap_sorszáma}. nap {adat.rádióamatőr_sorszáma}. rádióamatőr')
