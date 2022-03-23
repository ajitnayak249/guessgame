print("!!!welcome to number guessing game.!!! ")
winning_number = 24
number_of_guess = 1
print("number of guesses is limited to only 9 time:")

while number_of_guess <=9:
    x = int(input("Guess the number: \n"))
    if x < 24: print("you have enter lesser number kindly guess the greater number:")

    elif x > 24 : print("you have enter greater number kindly go little slow")
    else:
        print("congratulation!!! you are the winner")
        print(number_of_guess, "you took to finish")
        break
    print(9-number_of_guess,"number of guess are left")
    number_of_guess = number_of_guess + 1
if (number_of_guess > 9):
    print("Game Over")









