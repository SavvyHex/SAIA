#!/usr/bin/python3

import periodictable as pt
import pypokedex as pyd
import random
import math
import click

# Utility Methods
# Converting to superscript
def to_super(string):
    superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
    "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
    "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
    "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
    "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
    "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}

    trans = str.maketrans(
        ''.join(superscript_map.keys()),
        ''.join(superscript_map.values()))

    return string.translate(trans)

# Getting the row of a pascal triangle
def p_row(r):
    r -= 1
    n = 0
    nums = []
    while r >= n:
        nums.append(math.comb(r, n))
        n += 1
    return nums

# Usable Functions
@click.group()
def cli():
    pass

# Calculator
@cli.command(help="A simple calculator")
@click.argument("expression")
def calc(expression):
    click.echo(eval(expression))

# Values of Trignometric Functions
@cli.group(help="To find the values of trignometric functions")
def trig():
    pass

@trig.command(help="Used to find the sine of a decimal number")
@click.argument("value")
def sin(value):
    click.echo(math.sin(math.radians(float(value))))

@trig.command(help="Used to find the cosine of a decimal number")
@click.argument("value")
def cos(value):
    click.echo(math.cos(math.radians(float(value))))

@trig.command(help="Used to find the tangent of a decimal number")
@click.argument("value")
def tan(value):
    click.echo(math.tan(math.radians(float(value))))

@trig.command(help="Used to find the cotangent of a decimal number")
@click.argument("value")
def cot(value):
    click.echo(math.cot(math.radians(float(value))))

@trig.command(help="Used to find the secant of a decimal number")
@click.argument("value")
def sec(value):
    click.echo(math.sec(math.radians(float(value))))

@trig.command(help="Used to find the cosecant of a decimal number")
@click.argument("value")
def cosec(value):
    click.echo(math.cosec(math.radians(float(value))))

# Permutations
@cli.command(help="Find the number of permutations")
@click.argument("n")
@click.argument("r")
def perm(n, r):
    click.echo(math.perm(n, r))

# Combinations
@cli.command(help="Find the number of combinations")
@click.argument("n")
@click.argument("r")
def comb(n, r):
    click.echo(math.comb(n, r))

# Pascal's Triangle
@cli.command(help="Find the numbers on the nth row of the Pascal's Triangle")
@click.argument("row_number")
def ptr(row_number):
    r = p_row(int(row_number))
    row = ""
    for n in r:
        row += str(n) + "\t"
    click.echo(row)

# Binomial Theorem
@cli.command(help="Displays the formula for (a+b)\u207F")
@click.argument("row_number")
def bino(row_number):
    r = abs(int(row_number)) + 1
    if r != 0:
        expression = ""
        p_nos = p_row(r)
        for x in range(r):
            expression += str(p_nos[x])+"a"+to_super(str(r-1-x))+"b"+to_super(str(x))+" + "
        click.echo(expression[:-3])
    else:
        click.echo("0")

# Elements of the Periodic Table
@cli.command(help="Find basic information about elements of the periodic table")
@click.option("--num", default=-1, help="Element number")
@click.option("--sym", default="", help="Symbol of the element")
@click.option("--name", default="", help="Name of the element")
def element(num, sym, name):
    d = False
    if num != -1:
        d = True
        for e in pt.elements:
            if e.number == num:
                click.echo(f"{e.number}. {e.name.capitalize()} ({e.symbol})")
                click.echo(f"Mass = {e.mass}")
                click.echo(f"Density = {e.density}")
    if sym != "":
        d = True
        for e in pt.elements:
            if e.symbol == sym:
                click.echo(f"{e.number}. {e.name.capitalize()} ({e.symbol})")
                click.echo(f"Mass = {e.mass}")
                click.echo(f"Density = {e.density}")
    if name != "":
        d = True
        for e in pt.elements:
            if e.name == name.casefold():
                click.echo(f"{e.number}. {e.name.capitalize()} ({e.symbol})")
                click.echo(f"Mass = {e.mass}")
                click.echo(f"Density = {e.density}")
    if not d:
        sn = random.randint(1, 118)
        for e in pt.elements:
            if e.number == sn:
                click.echo(f"{e.number}. {e.name.capitalize()} ({e.symbol})")
                click.echo(f"Mass = {e.mass}")
                click.echo(f"Density = {e.density}")

@cli.command(help="To help you to catch 'em all")
@click.option("--num", default=-1, help="National Dex number of the pokemon")
@click.option("--name", default="", help="Name of the pokemon")
def pokedex(num, name):
    mon = (pyd.get(dex=num) if num != -1 else pyd.get(name=name)) if name != "" and num != -1 else pyd.get(dex=random.randint(1, 898))
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

if __name__ == "__main__":
    cli()