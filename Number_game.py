import random as rd

num = rd.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    a = input("Guess any number from 1 to 100: ")
    attempts += 1

    if not a.isdigit():
        print("Enter only numbers ❌")
        continue

    a = int(a)

    if a > num:
        print("Too high 📈")
    elif a < num:
        print("Too low 📉")
    else:
        print("🎉 You guessed it right!")
        print(f"The number was: {num}")
        print(f"Attempts taken: {attempts}")
        break
else:
    print("❌ Game Over! You used all attempts.")
    print(f"The number was: {num}")