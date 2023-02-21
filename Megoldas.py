from üzenet import üzenet


class Megoldas:
    _üzenetek: list[üzenet]

    @property
    def első_utolsó_küldő(self):
        első_üzenet_rögzítője: int = self._üzenetek[0].rádióamatőr_sorszáma
        utolsó_üzenet_rögzítője: int = self._üzenetek[len(self._üzenetek) - 1].rádióamatőr_sorszáma
        return f"2. feladat:\nAz első üzenet rögzítője: {első_üzenet_rögzítője}\nAz utolsó üzenet rógzítője: {utolsó_üzenet_rögzítője}"

    @property
    def mennyi_üzenet(self) -> dict[int, int]:
        üzenet_db: dict[int, int] = {}
        for e in self._üzenetek:
            if e.nap_sorszáma in üzenet_db:
                üzenet_db[e.nap_sorszáma] += 1
            else:
                üzenet_db[e.nap_sorszáma] = e.nap_sorszáma
                üzenet_db[e.nap_sorszáma] = 1
        return üzenet_db

    @property
    def mennyi_üzenet_kiírás(self) -> str:
        vissza: str = ''
        for key, value in sorted(self.mennyi_üzenet.items()):
            if value > 0:
                vissza += f'{key}. nap: = {value} rádióamatőr\n'
            else:
                vissza += f'{key}. nap: = 0 rádióamatőr\n'
        return vissza

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
