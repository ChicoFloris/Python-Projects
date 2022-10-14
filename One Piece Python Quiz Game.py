print ("Welcome to the ONE PIECE quiz game!!!")
 
playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()
print ("Okay let the games begin!! :) ")

Score = 0


answer1 = input("Q1. What does Luffy like the most? ")
if answer1.lower() == "meat":
    print("CORECT!!!")
    Score += 1
else:
    print ("WRONG!!")

answer2 = input("Q2. Can you trust Zoro with directions ? ")
if answer2.lower() == "no":
    print("CORECT!!!")
    Score += 1
else:
    print ("WRONG! You are lost man!")

answer3 = input("Q3. Who is the black leg character? ")
if answer3.lower() == "sanji":
    print("CORECT!!!")
    Score += 1
else:
    print ("WRONG!!")

answer4 = input("Q4. Which of Luffy's brothers died? ")
if answer4.lower() == "ace":
    print("CORECT!!:'(")
    Score += 1
else:
    print ("WRONG!!")

answer5 = input("Q5. Which is the best manga ever? ")
if answer5.lower() == "one piece":
    print("CORECT!!!")
    Score += 1 
else:
    print ("WRONG!!")

if Score == 5 :
    print("Score: ", Score,"/5")
    print(Score/5 * 100,"% Amazing NAKAMA!!!")
else:
    print("You finished the quiz with ",Score/5 * 100, "% correct!")

