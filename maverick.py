import random
import sys
print("this game can be played for eternity you will get 8 chances to guess a number and\n after that you will be provided with a new  number and so oon the game is not going to end")
while True:
    random_number = round(random.uniform(0,999),2)
    print(random_number)
    counter = 0
    #print("number = ",generated_number) for testing uncomment this
    
    while(counter<9):
        try:
            guess_number = float(input("enter your guess    "))
            counter +=1
            absolute=(  (  abs(random_number-guess_number)  )*100)/1000
            if guess_number == random_number:
                print("you won")
                sys.exit(0)
            if(counter<5):
                if(random_number>guess_number):
                    print("Your guess is too low")
                else:
                    print("Your guess is too high")
            
           
            elif (counter == 5):
                if(absolute <10):
                    raise Exception("You are approx 10% near")
            elif (counter == 6):
                if(absolute <5):
                    raise Exception("You are approx 5% near")
                
            elif (counter == 7):
                if(absolute <1):
                    raise Exception("You are approx 1% near")
            else:
                print("try again ")
                break
                '''sys.exit(0)'''
        except Exception as e:
            print(e)
            '''sys.exit(0)'''
