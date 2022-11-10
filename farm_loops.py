#!usr/bin/env python3

"""Script it peek into farms"""

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    NE_animals = farms[0]["agriculture"]

    for animal in NE_animals:
        print(animal)

    for farm in farms:
        print("-", farm["name"])

    choice = input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for animal in farm["agriculture"]:
                print(animal)


    yuck = ["carrots", "celery"]

    for farm in farms:
        print("-", farm["name"])

    choice = input("Pick a farm!\n")
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for animal in farm["agriculture"]:
                if animal not in yuck:
                    print(animal)

if __name__ == "__main__":
    main()
