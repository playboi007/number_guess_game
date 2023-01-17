import random

maximum_number = input("give a maximum number for your range: \n")

if maximum_number.isdigit():
    maximum_number = int(maximum_number)
    if maximum_number <= 0:
        print("Enter a number above 0")
        quit()

r = random.randint(1,maximum_number)
guesses = 0
while True:
    guesses += 1
    answer = int(input("make a guess: "))

    if answer == r:
        print("you got it correct!")
        break
    else:
        print("Not it!")

print(f"you got it in {guesses} tries")


