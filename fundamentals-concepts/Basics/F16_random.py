import random

low = 1
high = 100

# choose number between range of low - high
number = random.randint(low, high)
print(number)

# choose number between 0 to 1 in floating value
number1 = random.random()
print(number1)

#choose number from given options
options = ["rock", "paper","scissor"]
option = random.choice(options)
print(option)

#shuffle from the given sequence
card = ["1","3","5","6","7","8","9"]  # only  list is allowed
random.shuffle(card)
print(card)
