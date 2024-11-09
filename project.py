# from constants import map_data, user_data, moving_dice, weights, monster_list
import random
import time
import os

map_data = [
    "0",
    "A",
    "A",
    "A",
    "A",
    "T",
    "A",
    "A",
    "A",
    "A",
    "T",
    "C",
    "B",
    "B",
    "B",
    "T",
    "B",
    "B",
    "B",
    "A",
    "T",
    "C",
    "D",
    "D",
    "D",
    "T",
    "D",
    "D",
    "D",
    "D",
    "T",
    "C",
    "A",
    "A",
    "A",
    "T",
    "B",
    "B",
    "B",
    "B",
    "T",
    "A",
    "A",
    "A",
    "A",
    "T",
    "D",
    "D",
    "D",
    "D",
    "T",
    "C",
    "B",
    "B",
    "B",
    "T",
    "D",
    "D",
    "D",
    "D",
    "T",
    "E",
    "E",
    "E",
    "C",
    "T",
    "D",
    "D",
    "D",
    "D",
    "T",
    "E",
    "E",
    "E",
    "C",
    "T",
    "D",
    "D",
    "D",
    "D",
    "T",
    "E",
    "E",
    "E",
    "C",
    "F",
    "F",
    "F",
    "F",
    "E",
    "F",
    "F",
    "F",
    "F",
    "F",
    "F",
    "G",
    "G",
    "G",
    "G",
    "G",
]
# Your stats
user_data = {
    "current_HP": 40,
    "max_HP": 40,
    "level": 1,
    "exp_user": 0,
    "exp_needed": 5,
    "crit_yes": 0.1,
    "crit_no": 0.9,
    "crit_damage_min": 2.0,
    "crit_damage_max": 3.0,
    "attack_dice": [0, 1, 2, 3, 4, 5, 6],
    "inventory": {"HP_Potion": 0, "Dice_fixer": 0},
    "point": 0,
}

# Your dice
moving_dice = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# List of monster
monster_list = {
    "A": {"HP": 10, "current_HP": 10, "attack": 2, "exp": 5},
    "B": {"HP": 20, "current_HP": 20, "attack": 3, "exp": 9},
    "C": {"HP": 70, "current_HP": 70, "attack": 1, "exp": 11},
    "D": {"HP": 35, "current_HP": 35, "attack": 4, "exp": 14},
    "E": {"HP": 45, "current_HP": 45, "attack": 5, "exp": 18},
    "F": {"HP": 60, "current_HP": 60, "attack": 4, "exp": 20},
    "G": {"HP": 100, "current_HP": 100, "attack": 10, "exp": 30},
}

# Heal when finished fighting
def heal(hp):
    user_data["current_HP"] += hp
    if user_data["current_HP"] > user_data["max_HP"]:
        user_data["current_HP"] = user_data["max_HP"]

# When use the item in dictionary
def use_inventory():
    if (
        user_data["inventory"]["HP_Potion"] == 0
        and user_data["inventory"]["Dice_fixer"] == 0
    ):
        print("You have nothing in your inventory")
        return False
    want_to_use = int(input("Do you wish to view and/or use inventory? (yes:1 no:0)"))
    if want_to_use == 0:
        return False
    print(user_data["inventory"])
    # Not do anything
    item = int(input("What item do you want to use? (skip:0 potion:1 dice_fixer:2)"))
    if item != 1 and item != 2:
        return False
    # Use hp potion
    if item == 1:
        if user_data["inventory"]["HP_Potion"] <= 0:
            print("Insufficient amount of item")
            return False
        print("Use HP Potion")
        user_data["max_HP"] += 10
        user_data["current_HP"] += 10
        user_data["inventory"]["HP_Potion"] -= 1
        print(f"Your current health is now {user_data["current_HP"]}")
        time.sleep(3)
        return False

    if user_data["inventory"]["Dice_fixer"] <= 0:
        print("Insufficient amount of item")
        return False
    print(f'Your current location is {user_data["point"]}')
    move = int(input(f"Choose how far you will move {moving_dice}: "))
    user_data["inventory"]["Dice_fixer"] -= 1
    if move in moving_dice:
        user_data["point"] += move
        if user_data["point"] < 0:
            user_data["point"] = 0
        if user_data["point"] > 100:
            user_data["point"] = 100
        print(f"You are now at point {user_data["point"]}")
        return True
    return False

# Rolling the dice
def dice_move():
    input("Roll the dice to see what you get.(Press enter to continue)")
    move = random.choice(
        moving_dice
    )
    print(f"You get {move}.")
    time.sleep(0.75)
    print(f"Move {move} squares")
    user_data["point"] += move
    if user_data["point"] < 0:
        user_data["point"] = 0
    if user_data["point"] > 100:
        user_data["point"] = 100
    print(f"You are now at point {user_data["point"]}")

# Level up and gaining exp
def add_exp(exp):
    user_data["exp_user"] += exp
    while user_data["exp_user"] >= user_data["exp_needed"]:
        print("You level up!!")
        time.sleep(1)
        user_data["level"] += 1
        user_data["exp_user"] -= user_data["exp_needed"]
        user_data["exp_needed"] += 1
        print("You have gained 5 more health")
        time.sleep(0.5)
        user_data["max_HP"] += 5
        user_data["current_HP"] += 5

        if user_data["level"] % 5 == 0:
            print("Special!! You have gained critical chance + 5%")
            user_data["crit_yes"] += 0.05
            user_data["crit_no"] -= 0.05

        if user_data["level"] % 3 == 0:
            print(
                "You can choose 1 of these 3 stats.\n 1. Critical Chance + 5%\
                \n 2. Add a better attack number\n 3. Delete your least attack number"
            )
            num_boost = input("Choose a boost by typing the number: ")
            if num_boost == "1":
                print("You have chosen critical chance + 5%")
                user_data["crit_yes"] += 0.05
                user_data["crit_no"] -= 0.05
            elif num_boost == "2":
                print("You have chosen to add a better attack number.")
                user_data["attack_dice"].append(max(user_data["attack_dice"]) + 1)
            elif num_boost == "3":
                print("You have decided to delete your least attack number.")
                user_data["attack_dice"].remove(min(user_data["attack_dice"]))
            else:
                print("You fucker. You gain nothing for that.")

        if user_data["level"] % 3 != 0:
            print(
                "You can choose 1 of these 2 stats.\n 1. Critical Chance + 5%\
                \n 2. Add a better attack number"
            )
            num_boost = input("Choose a boost by typing the number: ")
            if num_boost == "1":
                print("You have chosen critical chance + 5%")
                user_data["crit_yes"] += 0.05
                user_data["crit_no"] -= 0.05
            elif num_boost == "2":
                print("You have chosen to add a better attack number.")
                user_data["attack_dice"].append(max(user_data["attack_dice"]) + 1)
            else:
                print("You fucker. You gain nothing for that.")
    input(f"Your current stats\
        \n Current health: {user_data["current_HP"]}\
        \nMaximum HP: {user_data["max_HP"]}\
        \nAttack possibilies: {user_data["attack_dice"]}\
        \nCritical Chance: {round(user_data["crit_yes"], 2)}\
        \nCritical range: {user_data['crit_damage_min']} - {user_data['crit_damage_max']}\
        \nLevel: {user_data["level"]}\
        \nExp: {user_data["exp_user"]}/{user_data["exp_needed"]} ")        
        

# Treasure box
def treasure_event():
    print("You found treasure")
    time.sleep(1)
    treasure_box = [
        "HP Potion",
        "Critical Damage max + 1.0",
        "Max health and your health + 10",
        "Critical chance + 5%",
        "Item to fix your dice for 1 turn",
        "Gain 10 experience points",
        "nothing",
    ]
    input("Let's see what you get. (Click any key to continue)")
    treasure_get = random.choice(range(len(treasure_box)))
    if treasure_get == 0:
        print("You found HP Potion")
        user_data["inventory"]["HP_Potion"] += 1
    elif treasure_get == 1:
        print("You found Critical Damage max + 1.0")
        user_data["crit_damage_max"] += 1.0
        print(f"Your new critical range is {user_data["crit_damage_min"]} -\
         {user_data["crit_damage_max"]}")
    elif treasure_get == 2:
        print("You found max health + 10 and your health + 10")
        user_data["max_HP"] += 10
        user_data["current_HP"] += 10
        print(f"Your current health is now {user_data["current_HP"]}")
    elif treasure_get == 3:
        print("You found critical chance + 5%")
        user_data["crit_yes"] += 0.05
        user_data["crit_no"] -= 0.05
        print(f"Your critical chance is now {round(user_data["crit_yes"], 2)}")
    elif treasure_get == 4:
        print("You found Dice fixer")
        user_data["inventory"]["Dice_fixer"] += 1
    elif treasure_get == 5:
        print("You gain 10 exp")
        add_exp(10)
    else:
        print("You get nothing?!?! Lol")
    input("Press enter to continue")
    return

#Battle Phase
def monster_event(event):
    monster = monster_list[event].copy()
    print(f"Found monster {event}")
    print(monster)
    time.sleep(1)
    while True:
        # Player Attack
        input("\n\nYour turn: Press enter to Attack")
        attack = random.choice(user_data["attack_dice"])
        crit_list = ["yes", "no"]
        crit_bool = random.choices(
            crit_list, weights=[user_data["crit_yes"], user_data["crit_no"]]
        )
        crit_multiply = random.uniform(
            user_data["crit_damage_min"], user_data["crit_damage_max"]
        )
        if crit_bool == ["no"]:
            dmg_player = attack
        else:
            dmg_player = attack * crit_multiply
        monster["current_HP"] -= dmg_player
        print(
            f"You deal {round(dmg_player, 2)} dmg, Monster's hp is {round(monster["current_HP"],2)}"
        )
        time.sleep(0.5)
        if monster["current_HP"] <= 0:
            print("You kill the monster!")
            input("Press enter to continue")
            break
        # Monster attack
        dmg_monster = monster["attack"]
        user_data["current_HP"] -= dmg_monster
        print("Monster turn")
        print(f"Monster deals {dmg_monster} dmg, Your hp is now {user_data["current_HP"]}")
        time.sleep(0.5)
        if user_data["current_HP"] <= 0:
            print("You die!")
            input("Press enter to continue")
            return False
    heal(10)  # Finished fighting
    input("You have recovered 10 health. (Press enter to continue.)")
    if user_data["point"] == 100:
        return True
    os.system("cls" if os.name == "nt" else "clear")
    add_exp(monster["exp"])
    return True


def map_event():
    event = map_data[user_data["point"]]
    if event == "0":
        return True

    if event == "T":
        treasure_event()
        return True

    return monster_event(event)

# Intro to the game
intro_game = input("Welcome to the game.\nPlease enter your name: ")
print("Hi, " + intro_game)
print("Welcome to the game. Type 's' to start the game")

start = input()
os.system("cls" if os.name == "nt" else "clear")
if start == "s":
    # Greeting message
    print("You are trapped inside a dimension by a witch in a place called LUCK ISLAND.")
    print("This place was once a dream for gamblers, but now it's a living hell.")
    print("In order to escape this place, you have to defeat the boss monsters.")
    print("Will you continue? (Press 'c' to continue)")
    # Choose whether to continue or not
    con_tinue = input()
    os.system("cls" if os.name == "nt" else "clear")
    
    if con_tinue == "c":
        # How to play the game
        print("How to play")
        print("You will roll the moving dice. ")
        print("You will then fight monsters, gain levels, and beat the boss monster.")
        input("Press enter to continue")
        
        os.system("cls" if os.name == "nt" else "clear")
        k = 0
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            # Check if use dice fixer or not
            use_dice_fixer = use_inventory() 
            if not use_dice_fixer: # if didn't use dice fixer
                dice_move()
            time.sleep(0.5)
            # You win or lose
            survive = map_event()
            if not survive: # If you die
                os.system("cls" if os.name == "nt" else "clear")
                print(f"You survive for {k} rounds")
                print(f'level: {user_data["level"]} | location: {user_data["point"]}')
                break
            k += 1 # Count turn

            if user_data["point"] == 100: # If you win
                os.system("cls" if os.name == "nt" else "clear")
                print(f"You win in {k} rounds")
                print(f"level: {user_data["level"]}")
                break

            
            
    
    
    
    
