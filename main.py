import random

names = input("Give me everybody's names, separated by a comma.\n ").capitalize()
name_string = names.split(", ")

print(name_string)

index_of_name = random.randint(0, len(name_string) - 1)
print(f"{name_string[index_of_name]} is going to buy the meal today!")