marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
def marvel_questions():
    ask_again = True
    while ask_again:
        char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ").title() 
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ").lower()

        if char_name in marvelchars and char_stat in marvelchars[char_name]:
          if char_stat == "real name": 
            print(char_name + "'s " + char_stat + " is: " + marvelchars[char_name][char_stat].title())
          else:
            print(char_name + "'s " + char_stat + " is: " + marvelchars[char_name][char_stat])
        else:
          print("Invalid Input...")

        again = input("Would you like to go again? [y] or [n] ")
        
        if again == "n":
          ask_again = False

marvel_questions()