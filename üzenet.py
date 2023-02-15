class üzenet:
    _nap_sorszáma: int
    _rádióamatőr_sorszáma: int
    _rádió_üzenet: str

    @property
    def nap_sorszáma(self):
        return self._nap_sorszáma

    @property
    def rádióamatőr_sorszáma(self):
        return self._rádióamatőr_sorszáma

    @property
    def rádió_üzenet(self):
        return self._rádió_üzenet

    def __init__(self, sor1: str, sor2: str):
        # sor1: minden második sor az elsőtöl kezdve
        # sor2: minden második sor a másodiktól kezdve
        napsorsz, radiosorsz = sor1.split(' ')
        üzenet_sor = sor2
        self._nap_sorszáma = int(napsorsz)
        self._rádióamatőr_sorszáma = int(radiosorsz)
        self._rádió_üzenet = üzenet_sor
