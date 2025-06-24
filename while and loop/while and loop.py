import random

weather_list = ["cold", "hot", "nice", "windy"]
score = 0

print("Weather Guessing Game!")
print("Guess if the weather matches!")
print()

while True:
    # Pick random weather
    real_weather = random.choice(weather_list)
    guess_weather = random.choice(weather_list)

    print(f"Is it {guess_weather}?")
    answer = input("Type true or false: ")

    if answer == "quit":
        break

    # Check if guess matches real weather
    if guess_weather == real_weather:
        correct = True
    else:
        correct = False

    # Check player answer
    if answer == "true" and correct:
        print("Right!")
        score = score + 1
    elif answer == "false" and not correct:
        print("Right!")
        score = score + 1
    else:
        print("Wrong!")

    print(f"Real weather was: {real_weather}")
    print(f"Score: {score}")
    print()