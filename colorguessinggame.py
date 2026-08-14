import random
import time

def greet():
    print("=============================")
    print("     color guessing game     ")
    print("=============================")
    
def startgame(playernam): 
    try: 
        colors=["red", "blue", "green", "yellow", "orange",
                "purple", "pink", "brown", "black", "white",
                "gray", "cyan", "magenta", "lime", "maroon"]

        print("\nDifficulty level\n")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        
        colorcount=0
        choice=int(input("Enter your choice: "))
        if choice==1:
            colorcount=5
        elif choice==2:
            colorcount=10
        elif choice==3:
            colorcount=15
        else:
            print("please enter 1-3") 
            return 0  

        availablecolors=colors[:colorcount]    
        print("\nAvailable colors:\n")
        for i in availablecolors:
            print(i) 

        comp=random.choice(availablecolors)
        wrong=0
        score=0
        
        print("\nyou have 25 seconds to guess the color\n")
        print("5 wrong attempts allowed \n")
        start_time=time.time()
        
        while True:
            if time.time()-start_time > 25:
                print("Times up!  Game Over ")
                print(f"the computer color was {comp}")
                break
                
            guess=input("Enter your guess: ").lower().strip()
            
            if guess not in availablecolors:
                print("please enter a color from above mention colors")
                continue
                
            if guess!=comp:
                wrong+=1
                if wrong==5:
                    print("wrong guess you have 0 lives left. game over")
                    print(f"the computer color was {comp}")
                    break 
                else:
                    print(f"wrong guess. you have {5-wrong} lives left")    
            elif guess==comp:
                score+=1
                print(f"correct guess your score is {score}")  
                
                comp=random.choice(availablecolors)
                print("new color is picked to guess so keep guessing")
                start_time=time.time()
                
      
        return score    
        
    except Exception as err: 
        print(f"an error occured as {err}")
        return 0 
        
greet() 
playername=input("Enter your name: ")
highscore=0

while True:
    print("\n===GAME MENU===\n")
    print("1. START GAME")
    print("2. HIGH SCORE")
    print("3. QUIT GAME") 
    try:
        mainchoice=int(input("Enter your choice: "))
        
        if mainchoice==1:
            currentscore=startgame(playername)
            print(f"\n GAME OVER \n ")
            if currentscore > highscore:
                highscore=currentscore
                print(f"New High Score: {highscore}!")
                
        elif mainchoice==2:
            print(f"High score is {highscore}")        
            
        elif mainchoice==3:
            print(f"Thanks for playing the game {playername}")         
            break
            
        else:
            print("please select from above 1-3 options")
            continue
            
    except Exception as err:
        print(f"An error occured as {err}")