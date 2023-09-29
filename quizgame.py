print("Welcome to my computer quiz! Good luck")
playing=input("Do you want to play? ")
if playing.lower() != "yes":
   quit()
else:
    print("Okay great lets start this journey")
    score=0
    
       
answer=input("what does ALU stand for? ")
if answer.lower()=="arithmetic logic unit":
    print("Correct")
    score +=1
else:
    print("Incorrect try again")
    
answer=input("what does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("Correct")
    score +=1
else:
    print("Incorrect try again")
    
answer=input("what does RAM stand for? ")
if answer.lower()=="random access memory":
    print("Correct")
    score +=1
else:
    print("Incorrect try again")
    
answer=input("what does ROM stand for? ")
if answer.lower()=="read only memory":
    print("Correct")
    score +=1
else:
    print("Incorrect try again")
    
answer=input("what does py stand for? ")
if answer.lower()=="python":
    print("Correct")
    score +=1
else:
    print("Incorrect try again")      
    
print("Your final score is "+str(score)) 
print("Congratulations you scored "+str(score/4*100)+"%") 
print("game over thank you for playing")    