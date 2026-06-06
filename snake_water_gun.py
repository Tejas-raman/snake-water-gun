# to create a game snake water gun 
'''
1 = water 
0 = gun 
-1 = snake 

'''
def game(computer,choice):


    if (choice == 1) and (computer== 0 ) or (choice == -1) and (computer==1) or (choice == 0) and (computer== -1):
        print("you win !")
        return "user"
    

    elif(choice==0)and(computer==0) or (choice==1)and(computer==1) or (choice==-1)and(computer==-1):
        print("tie...")
        return"tie"

    else:
        print("computer wins")
        return "computer"
    
         
dict = {"snake" : -1,
        "gun" : 0 ,
        "water" : 1}
r_dict = {-1 :"snake" ,
        0 :"gun"  ,
        1 : "water"}


import random
  
user_counter = 0
computer_counter= 0

while True :
    choice = input("Enter your choice : ").lower()
    if choice not in dict :
        print("Invalid choice..")
        continue
    choice = dict[choice]
    computer_ = random.choice([-1,0,1])
    computer = r_dict[computer_]
    print(f" computer choice  : {computer}")
    
    result = game(computer_,choice)
    if result== "user":
        user_counter += 1
    elif result == "computer":
        computer_counter +=1
    
    print(f"user : {user_counter}\ncomputer : {computer_counter}")

    play_again = input("do you want to play again y/n : ").lower()
    if play_again != "y":
        break
print(f"final score = you : {user_counter}, computer : {computer_counter}")