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


if __name__ == "__main__":
    main()
