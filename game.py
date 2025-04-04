# stone-paper-scissors
"""
1 -> Stone
2-> Paper
3 -> Sissor
"""
import random
User_choice_Dictionary = {1:"Stone", 2:"Paper" , 3:"scissors"}
User_choice_reverse_Dictionary = {"Stone":1,"Paper":2,"scissors":3}
NumberList = [1,2,3]
computer_score = 0
user_score = 0
draw_score = 0
    
print("Welcome To Stone paper scissors Game")
print("Rules")
print("Press 1 For Select Stone")
print("Press 2 For Select Paper")
print("Press 3 For Select scissors")
# print("You have Totel 5 chance to play")
print("For win you have to score 3 points, otherwise you will lose")

# loop_track = 0
# while(loop_track<5):
while(True):
    
    if(computer_score==3):
        print(f"The score of computer is:{computer_score}")
        print("You Lose this Stone paper scissors game")
        break
    elif(user_score==3):
        print(f"Your final score is:{user_score}")
        print("Congratulations you win this Stone paper scissors game!")
        break
        
    else:
        computer = random.choice(NumberList)
        UserChoice = int(input("Enter Number(1/2/3):"))
        
        if (computer == UserChoice):
            print("Draw")
            draw_score += 1
            print(f"Your Current score is:{user_score} and Computer Current score is:{computer_score} and Draw score is {draw_score}")
            # loop_track -= 1
        else:
            if(computer == 1 and UserChoice == 2):
                print(f"You Choose {User_choice_Dictionary[UserChoice]} And computer Choose {User_choice_Dictionary[computer]}")
                print("You Win!")
                user_score += 1
                print(f"Your Current score is:{user_score} and Computer Current score is:{computer_score} and Draw score is {draw_score}")
            elif(computer == 1 and UserChoice == 3):
                print(f"You Choose {User_choice_Dictionary[UserChoice]} And computer Choose {User_choice_Dictionary[computer]}")
                print("You Lose!")
                computer_score += 1
                print(f"Your Current score is:{user_score} and Computer Current score is:{computer_score} and Draw score is {draw_score}")
                
            elif(computer == 2 and UserChoice == 3):
                print(f"You Choose {User_choice_Dictionary[UserChoice]} And computer Choose {User_choice_Dictionary[computer]}")
                print("You Win!")
                user_score += 1
                print(f"Your Current score is:{user_score} and Computer Current score is:{computer_score} and Draw score is {draw_score}")
            elif(computer == 2 and UserChoice == 1):
                print(f"You Choose {User_choice_Dictionary[UserChoice]} And computer Choose {User_choice_Dictionary[computer]}")
                print("You Lose!") 
                computer_score += 1
                print(f"Your Current score is:{user_score} and Computer Current score is:{computer_score} and Draw score is {draw_score}")
                
            elif(computer == 3 and UserChoice == 1):
                print(f"You Choose {User_choice_Dictionary[UserChoice]} And computer Choose {User_choice_Dictionary[computer]}")
                print("You Win!")
                user_score += 1
                print(f"Your Current score is:{user_score} and Computer Current score is:{computer_score} and Draw score is {draw_score}")
            elif(computer == 3 and UserChoice == 2):
                print(f"You Choose {User_choice_Dictionary[UserChoice]} And computer Choose {User_choice_Dictionary[computer]}")
                print("You Lose!")
                computer_score += 1
                print(f"Your Current score is:{user_score} and Computer Current score is:{computer_score}and Draw score is {draw_score}")

        # loop_track += 1
        # print(loop_track)
print("Thanks for playing Game")