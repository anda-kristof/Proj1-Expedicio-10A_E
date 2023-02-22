from üzenet import üzenet


class Megoldas:
    _üzenetek: list[üzenet]

    @property
    def első_utolsó_küldő(self):
        első_üzenet_rögzítője: int = self._üzenetek[0].rádióamatőr_sorszáma
        utolsó_üzenet_rögzítője: int = self._üzenetek[len(self._üzenetek) - 1].rádióamatőr_sorszáma
        első_utsó = [első_üzenet_rögzítője, utolsó_üzenet_rögzítője]
        return első_utsó

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

    @property
    def napok_száma(self) -> int:
        napok: list[int] = []
        for nap in self._üzenetek:
            if nap.nap_sorszáma not in napok:
                napok.append(nap.nap_sorszáma)
        return len(napok)

    @property
    def üzenet_helyreállítása(self):
        napszám: int = 1
        üzenetek_helyreállítva: list[str] = []
        while napszám <= self.napok_száma:
            naphoz_tartozó_üzenetek: list[str] = []
            for uzenet in self._üzenetek:
                if uzenet.nap_sorszáma == napszám:
                    naphoz_tartozó_üzenetek.append(uzenet.rádió_üzenet)
            nap_üzenete: str = ''
            for i, e in enumerate(naphoz_tartozó_üzenetek[0]):
                index = 1
                while e == "#":
                    e = naphoz_tartozó_üzenetek[index][i]
                    index += 1
                    if index > len(naphoz_tartozó_üzenetek) - 1:
                        break
                if e != '#':
                    nap_üzenete += e
            üzenetek_helyreállítva.append(nap_üzenete)
            napszám += 1
        return üzenetek_helyreállítva

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

    def fájl_írás(self, fájlnév: str):
        with open(fájlnév, 'w', encoding='utf-8') as file:
            for sor in self.üzenet_helyreállítása:
                file.write(f'{sor}\n')

    def szame(self, szo: str) -> bool:
        valasz: bool = False
        if szo.isdigit():
            valasz = True
        return valasz

    def megadott_üzenet(self, megadott_nap_sorszáma: int, megadott_amatőr_sorszáma: int) -> str:
        valasz: str = ''
        for e in self._üzenetek:
            if megadott_nap_sorszáma == e.nap_sorszáma and megadott_amatőr_sorszáma == e.rádióamatőr_sorszáma:
                valasz: str = e.rádió_üzenet
        if valasz == '':
            return valasz
        else:
            return valasz

    def egyedek_száma(self, megadott_üzenet: str) -> str:
        valasz: str = ''
        if megadott_üzenet == '':
            valasz = 'Nincs ilyen feljegyzés'
        elif self.szame(megadott_üzenet[0]) and self.szame(megadott_üzenet[2]):
            valasz = f'A megfigyelt egyedek száma: {int(megadott_üzenet[0]) + int(megadott_üzenet[2])}'
        else:
            valasz = 'Nincs információ'
        return valasz
