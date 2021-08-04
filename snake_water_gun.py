import random
sample_space =['Snake','Water','Gun']

user_count = 0
computer_count = 0

i = a = 5
while i>0:
    user_choice = input("Please take your guess:\n")
    choice = random.choice(sample_space)
    print("The computer's choice was:\n",choice)
    if(user_choice==choice):
        print("Uh! Oh it's a tie\n")
        print("You have",i-1," games left.")

    elif(user_choice=='Snake'):
        if(choice=='Water'):
            print("Voilaa!! You won!!")
            user_count+=1
            print("You have",i-1," games left.")
        elif(choice=='Gun'):
            print("Oops! You lost")
            computer_count+=1
            print("You have",i-1," games left.")

    elif (user_choice == 'Water'):
        if (choice == 'Gun'):
            print("Voilaa!! You won!!")
            user_count+=1
            print("You have", i - 1, " games left.")
        elif (choice == 'Snake'):
            print("Oops! You lost")
            computer_count+=1
            print("You have", i - 1, " games left.")

    elif (user_choice == 'Gun'):
        if (choice == 'Snake'):
            print("Voilaa!! You won!!")
            user_count+=1
            print("You have", i - 1, " games left.")
        elif (choice == 'Water'):
            print("Oops! You lost")
            computer_count+=1
            print("You have", i - 1, " games left.")
    i-=1

print(f"Dear user you won {user_count} times")
print(f"Computer won {computer_count} times")
print("And it was a tie for %d times"%(a-(user_count+computer_count)))
print("Hope you had a lot of fun *o* ")