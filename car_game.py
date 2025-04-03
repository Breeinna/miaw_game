print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⣆⠀⠀⠀⠀⠀⣠⡀ ᶻ 𝗓 𐰁 .ᐟ ⣼⣿⡗⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠀⠘⠷⠶⠶⠶⠾⠉⢳⡄⠀⠀⠀⠀⠀⣧⣿⠀⠀⠀⠀⠀
⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣤⣤⣤⣤⣤⣿⢿⣄⠀⠀⠀⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠙⣷⡴⠶⣦
⠀⠀⢱⡀⠀⠉⠉⠀⠀⠀⠀⠛⠃⠀⢠⡟⠀⠀⠀⢀⣀⣠⣤⠿⠞⠛⠋
⣠⠾⠋⠙⣶⣤⣤⣤⣤⣤⣀⣠⣤⣾⣿⠴⠶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀
⠛⠒⠛⠉⠉⠀⠀⠀⣴⠟⢃⡴⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

print ("Someone just sent you a goofy lazy ass black car")
print ("Your mission is to make it likes you")

choice1 = input ('It miaws on you 3 times in row. What to do? "kick" or "pat".\n').lower()
if choice1 == "pat":
    # continue the game
    choice2 = input ('It started to get confortable around you. Unfortunately it tries to throw attack on u. Type "pat" to pat it ofc. Type "dodge" to forecasting and dodge the attack.\n').lower()
    if choice2 == "dodge":
        # continue the game
       choice3 = input('You dodged the attack. *Lmao stupid ass negro car*. The car seems like started to get exhausted so you should probably feed it. Theres car food, watermelon, and burger. Which food you gonna feed it with?\n').lower()
       if choice3 == "car food":
           print ("the car thinks youre those normies and leaves you. Game over...")
       elif choice3 == "burger":
           print ("the car poisoned and dies. Game over...")
       elif choice3 == "watermelon":
        #good game
           print ("the car likes it sooooooooooo much and it wnts to be you pet. You win!")
       else: print ("you choose the food that doesnt exist. Game over...")
    else:
     print ("It crawls and chopped ur head off. Game over...")
else:
    print ("It crawls the sh*t on you. Game over...")
