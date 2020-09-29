# -*- coding: cp1252 -*-
# Varmistetaan, ett� k�ytt�j� antaa luvun
def otanumero():
    while True:
        try:
            luku = int(input("Anna luku: "))
            return luku
        except Exception:
            print("Virheellinen sy�te!")
# T�ss� on main.
def main():
    import math

    luku1 = otanumero()
    luku2 = otanumero()

    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(luku1/luku2)\n(6) cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")
        print("Valitut luvut:",luku1,luku2)
        valinta = int(input("Tee valinta (1-8): "))
        if valinta == 1:
            print("Tulos on:", luku1+luku2)
        elif valinta == 2:
            print("Tulos on:", luku1-luku2)
        elif valinta == 3:
            print("Tulos on:", luku1*luku2)
        elif valinta == 4:
            print("Tulos on:", luku1/luku2)
        elif valinta == 5:
            print("Tulos on:", math.sin(luku1/luku2))
        elif valinta == 6:
            print("Tulos on:", math.cos(luku1/luku2))
        elif valinta == 7:
            luku1 = otanumero()
            luku2 = otanumero()
        elif valinta == 8:
            break
        else:
            print("Valintaa ei tunnistettu.")
if __name__ == "__main__":
    main()
