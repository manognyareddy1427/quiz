print("wel to the quiz")
play = input("do u want to play")
x = print(play)
score = 0 
if play == "no":
    quit()
elif play== "yes":
    print("okay , lets play")
    q1 = input("full form of cpu")
    if q1 == "central processing unit":#in lower case
       print("correct")
       score = score + 1 
       print(score)
    else:
       print("incorrect")
    q2 = input("subtract 99 from 100")
    if q2 == "1":
        print("correct")
        score+=1
        print("score:",score )
    else :
        print("incorrect")
    q3 = input("is karnataka a state ")
    if q3 == "yes":
        print("correct")
        score+=1
        print("score:",score )
    else :
        print("incorrect")
    q4 = input("capital of maharastra")
    if q2 == "mumbai":
        print("correct")
        score+=1
        print("score:",score )
    else :
        print("incorrect")
    print(score)
    if score <=1:
        print("need to improve")
    else:
        print("congrats")






