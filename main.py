from radio import radio


def main() -> None:
    # sorszámok: list[radio] = []
    # with open('forrás.txt', 'r', encoding='utf-8') as file:
    #     minden_második: bool = True
    #     for sor1 in file.read().splitlines():
    #         if minden_második:
    #             rádióadatok.append(radio(sor1))
    #             rádióadatok.append(radio(sor2))
    #             minden_második = False
    #         else:
    #             minden_második = True

    rádioadatok: list[radio] = []
    sor_száma: int = 1
    with open('forrás.txt', 'r', encoding='utf-8') as file:
        sor: str = file.read()
        for e in sor.splitlines():
            sor_száma2: int = sor_száma - 1
            sor1: str = sor.splitlines()[sor_száma2]
            sor2: str = sor.splitlines()[sor_száma]
            if sor_száma % 2 != 0:
                rádioadatok.append(radio(sor1, sor2))
            sor_száma += 1
            if sor_száma == len(sor.splitlines()):
                break

    print(len(rádioadatok))


if __name__ == "__main__":
    main()
