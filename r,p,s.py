import random

l1=["rock","paper","scissors"]
# user=input("Rock/Paper/Sisscors what's yr choics:").lower()
def game():
    guess=0
    
    u_points=0
    c_points=0
    #print("Computer:",guess)
    
    for i in range(1,4):
        user=input("Rock/Paper/scissors what's yr choics:").lower()
        guess=random.choice(l1)
        print("Computer:",guess)
            
        if user=="rock":
            if guess=="scissors":
                u_points+=1
                print(f"Yepp!! U Win!! U get points:{u_points}")
                print(f"And Computer gets points:{c_points}")
                
            elif guess=="paper":
                c_points+=1
                print(f"aggh U Lose!! Ur points:{u_points}")
                print(f"And Computer gets points:{c_points}")
                

            elif guess=="rock":
                print(f"Tie with your points {u_points} and comps points {c_points}")
                

            else:
                print("Enter Valid word!!")
                
        elif user=="paper":
            if guess=="scissors":
                c_points+=1
                print(f"aggh U Lose!! Ur points:{u_points}")
                print(f"And Computer gets points:{c_points}")
                
            elif guess=="rock":
                u_points+=1
                print(f"Yepp!! U Win!! U get points:{u_points}")
                print(f"And Computer gets ponits:{c_points}")
                

            elif guess=="paper":
                print(f"Tie with your points {u_points} and comps points {c_points}")
            else:
                print("Enter Valid word!!")
                

        elif user=="scissors":
            if guess=="rock":
                c_points+=1
                print(f"aggh U Lose!! Ur points:{u_points}")
                print(f"And Computer gets ponits:{c_points}")
                
            elif guess=="paper":
                u_points+=1
                print(f"Yepp!! U Win!! U get points:{u_points}")
                print(f"And Computer gets points:{c_points}")
                

            elif guess=="scissors":
                print(f"Tie with your points {u_points} and comps points {c_points}")
            else:
                print("Enter Valid word!!")
                
        
        
    print(f"Thankyou!!")
    
game()