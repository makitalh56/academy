#THe program generate random number between 1-20. Then user try to guess it. User have 3 change.
import random

def main():
    rightNumber = random.randint(1,20)
    print(rightNumber)
    for x in range(3):
        number = input('Guess number: ')

        if rightNumber == int(number): 
            break
        elif rightNumber > int(number):
            print('Number is greater')
        elif rightNumber < int(number):
            print('Number is smaller')

    if rightNumber == int(number):
        print('You won! The number was '+ str(rightNumber))
    else:
        print('You lost the game! The right number was ' + str(rightNumber))

if __name__ == "__main__":
    main()