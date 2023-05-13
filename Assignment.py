## QUESTION 1 ##
ques1 = input("What is the capital of England?")
ans1 = "London"

## QUESTION 2 ##
ques2 = input("When did Pakistan win the World Cup?")
ans2 = "1992"

## IF ELSE STATEMENTS ##
if ques1.lower() == ans1.lower():
    print("That's the correct answer!")

    if ques2 == ans2:
        print("Great, you won!")
    else:
        print("Sorry, Pakistan did not win the World Cup in 1992.")
else:
    print("Oops, that's not correct.")
