#!/usr/bin/python3

import pypokedex

def dex(mon):
    print(f"\nNumber : {mon.dex}")
    print(f"Name : {mon.name.capitalize()}")
    print(f"Height : {mon.height/10}m")
    print(f"Weight : {mon.weight/10}kg")
    print("Type(s) : "+" ".join(map(str.capitalize, mon.types)))
    print("\nAbilities :")
    for a in mon.abilities:
        print(a.name.capitalize()+(" (hidden)" if a.is_hidden else ""))
    print("\nBase stats :")
    stats = mon.base_stats
    print(f" HP : {stats.hp}")
    print(f" Attack : {stats.attack}")
    print(f" Defence : {stats.defense}")
    print(f" Special Attack : {stats.sp_atk}")
    print(f" Special Defence : {stats.sp_def}")
    print(f" Speed : {stats.speed}\n")

def getmon(dex=0, name=None):
    if dex != 0:
        return pypokedex.get(dex=dex)
    elif name != None:
        return pypokedex.get(name=name)


if __name__ == "__main__":
    d = int(input("Enter the pokemon's dex number \n"))
    n = input("Enter the pokemon's name\n")
    dex(getmon(dex=d))
    dex(getmon(name=n))