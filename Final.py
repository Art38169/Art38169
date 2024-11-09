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


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Monster:
    def __init__(self, name, hp, attack, exp):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.exp = exp

    def monster_attack(self):
        return self.attack


monsters = {
    "A": Monster("A", 20, 3, 5),
    "B": Monster("B", 40, 4, 9),
    "C": Monster("C", 100, 1, 11),
    "D": Monster("D", 60, 5, 14),
    "E": Monster("E", 65, 7, 18),
    "F": Monster("F", 80, 7, 20),
    "G": Monster("G", 150, 10, 30),
}


class Map:
    map_data = map_data

    def map_event(self, player):
        print(f"You are at location {player.position}")
        event = self.map_data[player.position]
        if event == "0":
            print("There are no monsters here.")
            input("Press enter to end your turn.")
            return True

        if event == "T":
            self.treasure_event(player)
            return True

        return self.monster_event(player, event)

    def treasure_event(self, player):
        print("You found treasure")
        time.sleep(1)
        treasure_box = [
            ("You found HP Potion", player.inventory.add_hp_potion),
            ("You found Critical Damage max + 1.0", player.increase_crit_damage_max_1),
            (
                "You found max health + 10 and your health + 10",
                player.increase_max_hp_10,
            ),
            ("You found critical chance + 5%", player.increase_crit_rate_5),
            ("You found Dice fixer", player.inventory.add_dice_fixer),
            ("You gain 10 exp", player.add_exp_10),
            ("You get nothing?!?! Lol", player.nothing),
        ]
        treasure = random.choice(treasure_box)
        print(treasure[0])
        treasure[1]()
        input("Press enter to continue")
        return

    def monster_event(self, player, event):
        monster = monsters[event]
        print(f"Found monster {monster.name}")
        print(f"Monster's health: {monster.hp} |\
            Monster's damage: {monster.attack} |\
            Monster's EXP: {monster.exp}")
        player_hp = player.current_HP
        monster_hp = monster.hp
        while True:
            # Player Attack
            attack_type = input(
                "\n\nYour turn: Press s to strike, any key to normal attack: "
            )
            defend_type = random.choices(["c", "a"])[0]
            if defend_type == "c":
                print("Monster has chosen counter.")
            else:
                print("Monster has chosen defend")
            dmg_player = player.player_attack()
            player_hp, monster_hp = self.attack_defend(
                attack_type, defend_type, dmg_player, player_hp, monster_hp
            )
            time.sleep(0.5)
            if monster_hp <= 0:
                print("You kill the monster!")
                input("Press any key to continue")
                break
            if player_hp <= 0:
                print("You die!")
                input("Press any key to continue")
                return False
            # Monster attack
            dmg_monster = monster.monster_attack()
            defend_type = input(
                "\n\nMonster's turn: Monster has chosen.\
                \nYour turn: Press c to counter, any key to normal defend: "
            )
            attack_type = random.choices(["s", "a"])[0]
            if attack_type == "s":
                print("Monster has chosen strike!")
            else:
                print("Monster has chosen attack.")
            monster_hp, player_hp = self.attack_defend(
                attack_type, defend_type, dmg_monster, monster_hp, player_hp
            )
            time.sleep(0.5)
            if monster_hp <= 0:
                print("You kill the monster!")
                input("Press enter to continue")
                break
            if player_hp <= 0:
                print("You die!")
                input("Press enter to continue")
                return False

        player.change_current_hp(player_hp + 10) 
        if player.position == 100:
            return True
        clear_screen()
        player.add_exp(monster.exp)
        return True

    @staticmethod
    def attack_defend(attack_type, defend_type, dmg, attacker_hp, defender_hp):
        if attack_type == "s" and defend_type == "c":
            attacker_hp -= dmg * 2
            print("Counter success!!")
            print(
                f"Receive {round(dmg * 2, 2)} dmg, hp left {round(max(attacker_hp,0),2)}"
            )
        elif attack_type == "s":
            defender_hp -= dmg * 3
            print(f"Deal {round(dmg*3, 2)} dmg, hp left {round(max(defender_hp,0),2)}")
        elif defend_type == "c":
            defender_hp -= dmg
            print("Counter failed!!")
            print(f"Deal {round(dmg, 2)} dmg, hp left {round(max(defender_hp,0),2)}")
        else:
            defender_hp -= dmg * 0.5
            print("Defend success!!")
            print(
                f"Deal {round(dmg * 0.5, 2)} dmg, hp left {round(max(defender_hp,0),2)}"
            )
        return attacker_hp, defender_hp


map = Map()


class Dice:
    def __init__(self):
        self.move = range(-3, 17)

    def move_dice(self):
        return random.choices(self.move)[0]


class Inventory:
    def __init__(self):
        self.hp_potion = 0
        self.dice_fixer = 0

    def __str__(self):
        return f"HP Potion: {self.hp_potion}, Dice Fixer: {self.dice_fixer}"

    def check_inventory(self):
        return not (self.hp_potion == 0 and self.dice_fixer == 0)

    def add_hp_potion(self):
        self.hp_potion += 1

    def add_dice_fixer(self):
        self.dice_fixer += 1

    def remove_hp_potion(self):
        if self.hp_potion <= 0:
            return False
        self.hp_potion -= 1
        return True

    def remove_dice_fixer(self):
        if self.dice_fixer <= 0:
            return False
        self.dice_fixer -= 1
        return True


class Player:
    def __init__(self, name):
        self.name = name
        self.current_HP = 40
        self.max_HP = 40
        self.level = 1
        self.exp = 0
        self.exp_max = 5
        self.crit_rate = 0.1
        self.crit_damage_min = 2.0
        self.crit_damage_max = 3.0
        self.attack_dice = [0, 1, 2, 3, 4, 5, 6]
        self.inventory = Inventory()
        self.dice = Dice()
        self.position = 0

    def action(self, k):
        clear_screen()
        print(f"{self.name}'s turn {k+1}")
        print(f"level: {self.level} | location: {self.position}")
        print(f"Your current health: {round(self.current_HP,2)}/{self.max_HP}")
        print(f"Your current critical rate: {round(self.crit_rate,2)}")
        print(f"Your attack dice: {self.attack_dice}")
        print(f"Your critical range: [{self.crit_damage_min},{self.crit_damage_max}]")
        if not self.use_inventory():
            self.move()
        time.sleep(0.5)
        survive = map.map_event(self)
        if not survive:
            clear_screen()
            print(f"{self.name} survives for {k} rounds")
            print(f"level: {self.level} | location: {self.position}")
            input("Press enter to continue.")
            return True
        k += 1

        if self.position == 100:
            clear_screen()
            print(f"You win in {k} rounds")
            print(f"level: {self.level}")
            input("Congratulations, press enter to continue.")
            return True
        return False

    def use_inventory(self):
        if not self.inventory.check_inventory():
            print("You have nothing in your inventory")
            return False
        want_to_use_str = (
            input("Do you wish to view and/or use inventory? (yes:1 no:0)")
        )
        try:
            want_to_use = int(want_to_use_str)
        except ValueError:
            print("You choose to not see your inventory.")
        if want_to_use == 0:
            return False
        print(self.inventory)

        item_str = (
            input("What item do you want to use? (skip:0 potion:1 dice_fixer:2)")
        )
        try:
            item = int(item_str)
        except ValueError:
            print("Don't worry, we will skip for you.")
        if item != 1 and item != 2:
            return False
        if item == 1:
            msg = self.use_hp_potion()
            print(msg)
            return False
        move_str = input(f"Choose how far to move {self.dice.move}:")
        try:
            move = int(move_str)
        except ValueError:
            print("Invalid input we will choose for you :)")
            move = random.choices(self.dice.move)[0]
        msg = self.use_dice_fixer(move)
        print(msg)
        return msg != "Invalid move"

    def use_hp_potion(self):
        if not self.inventory.remove_hp_potion():
            return "Insufficient amount of item"
        self.current_HP += 10
        if self.current_HP > self.max_HP:
            self.current_HP = self.max_HP
        return "Used HP Potion"

    def use_dice_fixer(self, move):
        if not self.inventory.remove_dice_fixer():
            return "Insufficient amount of item"
        if move in self.dice.move:
            self.position += move
            self.check_position()
            return "Used Dice Fixer"
        return "Invalid move"

    def move(self):
        move = self.dice.move_dice()
        print(f"Move {move} blocks.")
        self.position += move
        self.check_position()

    def check_position(self):
        if self.position < 0:
            self.position = 0
        if self.position > 100:
            self.position = 100

    def add_exp(self, exp):
        self.exp += exp
        while self.exp >= self.exp_max:
            self.level_up()

    def add_exp_10(self):
        self.add_exp(10)

    def increase_crit_damage_max_1(self):
        self.crit_damage_max += 1

    def increase_crit_rate_5(self):
        self.crit_rate += 0.05
        if self.crit_rate > 1:
            self.crit_rate = 1

    def increase_max_hp_10(self):
        self.max_HP += 10
        self.current_HP += 10

    def nothing(self):
        pass

    def player_attack(self):
        attack = random.choices(self.attack_dice)[0]
        crit_list = [True, False]
        crit_bool = random.choices(
            crit_list, weights=[self.crit_rate, 1 - self.crit_rate]
        )
        if crit_bool:
            crit_multiply = random.uniform(self.crit_damage_min, self.crit_damage_max)
            return attack * crit_multiply
        return attack

    def change_current_hp(self, hp):
        self.current_HP = hp
        if self.current_HP > self.max_HP:
            self.current_HP = self.max_HP

    def level_up(self):
        print("You level up!!")
        time.sleep(1)
        self.level += 1
        self.exp -= self.exp_max
        self.exp_max += 1
        print("You have gained 5 more health")
        time.sleep(0.5)
        self.max_HP += 5
        self.current_HP += 5

        if self.level % 5 == 0:
            print("Special!! You have gained critical chance + 5%")
            self.crit_rate += 0.05

        if self.level % 3 == 0:
            print(
                "You can choose 1 of these 3 stats.\n 1. Critical Chance + 5%\
                    \n 2. Add a better attack number\n 3. Delete your least attack number"
            )
            try:
                num_boost = int(input("Choose a boost by typing the number: "))
            except ValueError:
                print("Invalid input we will choose for you :)")
                num_boost = random.choices([1, 2, 3])[0]
            if num_boost == 1:
                print("You have chosen critical chance + 5%")
                self.crit_rate += 0.05
            elif num_boost == 2:
                print("You have chosen to add a better attack number.")
                self.attack_dice.append(max(self.attack_dice) + 1)
            else:
                print("You have decided to delete your least attack number.")
                self.attack_dice.remove(min(self.attack_dice))
            time.sleep(1)
        else:
            print(
                "You can choose 1 of these 2 stats.\n 1. Critical Chance + 5%\
                    \n 2. Add a better attack number"
            )
            try:
                num_boost = int(input("Choose a boost by typing the number: "))
            except ValueError:
                print("Invalid input we will choose for you :)")
                num_boost = random.choices([1, 2])[0]
            if num_boost == 1:
                print("You have chosen critical chance + 5%")
                self.crit_rate += 0.05
            else:
                print("You have chosen to add a better attack number.")
                self.attack_dice.append(max(self.attack_dice) + 1)
            time.sleep(1)


def start_game():
    clear_screen()
    print("Welcome to the game.")
    player1_name = input("Please enter your name (Player 1): ")
    print("Hi, " + player1_name)
    player2_name = input("Please enter your name (Player 2): ")
    print("Hi, " + player2_name)
    input("Welcome to the game. Press enter to start the game")
    clear_screen()
    print(
        "You are trapped inside a dimension by a witch in a place called LUCKY LAND."
    )
    print("This place was once a dream for gamblers, but now it's a living hell.")
    print("In order to escape this place, you have to defeat the boss monsters.")
    input("Press enter to continue")
    clear_screen()
    print("How to play")
    print("You will roll the moving dice. ")
    print("You will then fight monsters, gain levels, and beat the boss monster.")
    input("Press any key to continue")
    clear_screen()

    return player1_name, player2_name


player1_name, player2_name = start_game()

player1 = Player(player1_name)
player2 = Player(player2_name)

is_end1 = False
is_end2 = False

k = 0
turn = 1
while True:
    if is_end1 and is_end2:
        break
    if turn == 1 and not is_end1:
        is_end1 = player1.action(k)
        if not is_end2:
            turn = 2
    if turn == 2 and not is_end2:
        is_end2 = player2.action(k)
        if not is_end1:
            turn = 1
    k += 1
