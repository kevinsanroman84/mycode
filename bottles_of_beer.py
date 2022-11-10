#!/usr/bin/env python3

"""Script to print 99 bottles of beer song"""

def main():
    beers = input("How many bottles are on the wall? ")

    if beers.isdigit():
        beers = int(beers)
    else:
        print("Not a number you ruined the party...")
        print("Go home.")
        input()

    for i in range(beers, -1, -1):
        print(str(i) +" bottles of beer on the wall!")
        print(str(i) + " bottles of beer on the wall! " + str(i) + " bottles of beer! You take one down, pass it around!")
main()
