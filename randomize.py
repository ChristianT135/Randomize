import random

pips = random.randint(1, 6)
print(" You rolled", pips)

prizes = ["a car", "Money", "a pet"]
prize_won = random.choice(prizes)
print(" You won", prize_won)

cards= [1,2,3,4,5,6,7,8,]
random.shuffle(cards)
print(cards)

