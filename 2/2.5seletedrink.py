import random
menu = ["coffee", "tea", "water", "milk"]
name = input("Your name please:")
drink = random.choice(menu)
print(name + ", Your drink is " + drink + ".")