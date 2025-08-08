print("Welcom to the Number Guessing game! \nJust don't look at the code ;)")
print("\n\nLet's get started then!")
print("I'm thinking of a number between 1 and 10. Can u guess it?")

num = (int(input("Enter your guess ")))

if num < 7:
    print("Too low, try again :o")

elif num > 7:
    print("Too high, try again ;]")

else:
    print("Correct! You guessed it right! Congratulations ^_^")
