"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Autor: Bc. Martin Novák
Email: m.novak44@seznam.cz
"""

import random


def pozdrav():
    print("Ahoj, vítej v mojí hře!")
    print("-----------------------------------------------")
    print("Vygeneroval jsem 4 náhodná čísla.")
    print("Tak začneme hrát Bulls and Cows.")
    print("-----------------------------------------------")


def generovani_cisla():
    cislice = list("123456789")
    prvni = random.choice(cislice)
    zbytek = list("0123456789")
    zbytek.remove(prvni)
    random.shuffle(zbytek)
    return prvni + ''.join(zbytek[:3])


def overeni_vstupu(vstup):
    if not vstup.isdigit():
        print("Vstup musí být číslice.")
        return False
    if len(vstup) != 4:
        print("Musíš zadat přesně 4 číslice.")
        return False
    if vstup[0] == '0':
        print("Číslo nesmí začínat nulou.")
        return False
    if len(set(vstup)) != 4:
        print("Číslice se nesmí opakovat.")
        return False
    return True


def spocitej_bulls_a_cows(tajne, tip):
    bulls = sum(t == h for t, h in zip(tajne, tip))
    cows = sum(min(tajne.count(c), tip.count(c)) for c in set(tip)) - bulls
    return bulls, cows


def vyhodnot_vystup(bulls, cows):
    bull_slovo = "bull" if bulls == 1 else "bulls"
    cow_slovo = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_slovo}, {cows} {cow_slovo}"


def hraj_hru():
    pozdrav()
    tajne_cislo = generovani_cisla()
    pokusy = 0

    while True:
        print("Zadej číslo:")
        print("-----------------------------------------------")
        tip = input(">>> ").strip()

        if not overeni_vstupu(tip):
            continue

        pokusy += 1
        bulls, cows = spocitej_bulls_a_cows(tajne_cislo, tip)

        if bulls == 4:
            print(f"Správně, uhodl jsi číslo\nna {pokusy} pokusů!")
            print("-----------------------------------------------")
            print("To je úžasné!")
            break
        else:
            print(vyhodnot_vystup(bulls, cows))
            print("-----------------------------------------------")



if __name__ == "__main__":
    hraj_hru()
