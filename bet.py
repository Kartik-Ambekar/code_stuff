import random
#function. 
def bet(balance):
    bet_amount = int(input("Enter the amount you want to bet: "))
    if bet_amount > balance:
        print("You don't have enough balance.")
        return balance

    i = 10
    for j in range(i):
        guess = input("Enter your guess (0-10): ")
        if guess.isnumeric() and 0 <= int(guess) <= 10:
            guess = int(guess)
            random_number = random.randint(0, 10)
            if guess == random_number:
                print("You have hit the jackpot!")
                balance += bet_amount
                break

            else:
                print(
                    f"The computer guessed {random_number}, you guessed {guess}. Please try again.")
                if j == 9:
                    balance -= bet_amount
                else:
                    continue
        else:
            print("Invalid input. Please enter a number between 0 and 10.")
            return balance

    print(f"Current balance: {balance}")
    if balance>1000000:
        print("congratulations you have made it!!")
    choice = input("Do you wish to continue the bet? (y/n) ")
    if choice.lower() == 'y':
        return bet(balance)
    return balance


balance = 500
print(f"Your current balance: {balance}")
print("Make $1000000 as soon as possible!!")
answer = input("Are you ready to make millions? (y/n) ")
if answer.lower() == 'y':
    balance = bet(balance)
print("Come back when you wish to make a fortune!")
