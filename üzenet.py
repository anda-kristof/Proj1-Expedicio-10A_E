class radio:
    nap_sorszáma: int
    rádióamatőr_sorszáma: int
    rádió_üzenet: str

    def __init__(self, sor1: str, sor2: str):
        # sor1: minden második sor az elsőtöl kezdve
        # sor2: minden második sor a másodiktól kezdve
        napsorsz, radiosorsz = sor1.split(' ')
        üzenet = sor2
        self.nap_sorszáma = int(napsorsz)
        self.rádióamatőr_sorszáma = int(radiosorsz)
        self.rádió_üzenet = üzenet
