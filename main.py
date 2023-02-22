from Megoldas import Megoldas


def main() -> None:

    üzenet_adatok: Megoldas = Megoldas("veetel.txt")

    # 2.feladat

    print(f"2. feladat:\nAz első üzenet rögzítője: {üzenet_adatok.első_utolsó_küldő[0]}\nAz utolsó üzenet rógzítője: {üzenet_adatok.első_utolsó_küldő[1]}")

    # 3.feladat
    print("\n3.Feladat:")
    üzenet_adatok.melyik_üzenetben_van_a_szöveg("farkas")

    # 4. feladat
    print("\n4. feladat:")
    print(üzenet_adatok.mennyi_üzenet_kiírás)

    # 5. feladat
    üzenet_adatok.fájl_írás('adaas.txt')

    # 7.feladat
    print("7. feladat")
    megadott_nap_sorszáma: int = int(input("Adja meg a nap sorszámát! "))
    megadott_amatőr_sorszáma: int = int(input("Adja meg a rádióamatőr sorszámát! "))
    print(üzenet_adatok.egyedek_száma(üzenet_adatok.megadott_üzenet(megadott_nap_sorszáma, megadott_amatőr_sorszáma)))


if __name__ == "__main__":
    main()
