from radio import radio


def main() -> None:

    rádioadatok: list[radio] = []
    sor_száma: int = 1
    with open('forrás.txt', 'r', encoding='utf-8') as file:
        fájl: str = file.read()
        for sor in fájl.splitlines():
            sor_száma2: int = sor_száma - 1
            sor1: str = fájl.splitlines()[sor_száma2]
            sor2: str = fájl.splitlines()[sor_száma]
            if sor_száma % 2 != 0:
                rádioadatok.append(radio(sor1, sor2))
            sor_száma += 1
            if sor_száma == len(fájl.splitlines()):
                break


if __name__ == "__main__":
    main()
