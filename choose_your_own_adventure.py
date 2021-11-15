name = input("Type your name: ")
print("Welcome",name,"to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?     ")

if answer.lower() == 'left':
    answer = input("You came to a river, you can walk aroung it or swim across? Type walk to walk and swim to swim across:      ")
    if answer.lower() == 'swim':
        print("You swam across and were eaten by an alligator")
    elif answer.lower() == 'walk':
        print("You walked for 1000 miles, ran out of water and you lost the game")
    else:
        print('Not a valid option. You lose.')


elif answer.lower() == 'right':
    answer = input("You came to bridge, it looks wobbly, do you want to cross it or head back (corss/back)      ")
    if answer.lower() == 'back':
        print("You go back and loose")
    elif answer.lower() == 'cross':
       answer = input("You corss the bridge and meet a stranger. Do you talk to them?   ")
       if answer.lower() == 'yes':
            print("You talk to stanger and take the gold. You win!!")
       elif answer.lower() == 'no':
            print("You ignore the starnger and they are offended and you lose")
       else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')

print("Thank you for trying! Goodbye :)")