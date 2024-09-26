import random

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

moving_dice = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]



def dice_move():
    move = random.choice(moving_dice)
    print(f"Move {move} squares")
    user_data["point"] += move
    if user_data["point"] < 0:
        user_data["point"] = 0
    if user_data["point"] > 100:
        user_data["point"] = 100
    print(f"You are now at point {user_data['point']}")


def map_event():
    event = map_data[user_data["point"]]
    if event == "0":
        return True


k = 0
while True:
    dice_move()

    map_event()
    k += 1

    if user_data["point"] == 100:
        print("You win")
        print(k)
        break