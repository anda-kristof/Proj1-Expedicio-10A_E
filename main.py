from Megoldas import Megoldas


def main() -> None:

    üzenet_adatok: Megoldas = Megoldas("veetel.txt")

    # 2.feladat
    print(üzenet_adatok.első_utolsó_küldő)

    # 3.feladat
    print("\n3.Feladat:")
    üzenet_adatok.melyik_üzenetben_van_a_szöveg("farkas")


if __name__ == "__main__":
    main()
