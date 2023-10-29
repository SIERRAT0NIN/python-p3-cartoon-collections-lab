dwarves_list = ["Dopey", "Grumpy", "Bashful", "Doc", "Dopey", "Bashful", "Grumpy"]


def roll_call_dwarves(dwarves):
    for i, dwarves in enumerate(dwarves, start=1):
        print(f"{i}. {dwarves}")


print(roll_call_dwarves(dwarves_list))

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]


def summon_captain_planet(planeteer_calls):
    planeteer_list = []
    for planeteer in planeteer_calls:
        planeteer_list.append(f"{planeteer.title()}!")
    return planeteer_list


print(summon_captain_planet(planeteer_calls))

short_words = ["puff", "go", "two"]


def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)


print(long_planeteer_calls(short_words))

cheese_type = ["cheddar", "gouda", "cambert"]
snacks = ["crackers", "gouda", "thyme"]


def find_the_cheese(snacks):
    for snack in snacks:
        if snack in cheese_type:
            return snack
    return None


print(find_the_cheese(snacks))
