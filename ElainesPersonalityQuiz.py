cat = 0
rat = 0

print("Are you a cat or a rat?")
def q1():
    global cat, rat
    ques = input("Question 1: Do you hate people? A: yes  B: no \n")
    if ques.lower() == "a":
        cat+=1
    elif ques.lower() == "b":
        rat+=1
    else:
        print("answer with A or B.")
        return q1()
    
def q2():
    global cat, rat
    ques = input("Question 2: Pizza or steak? A: pizza  B: steak \n")
    if ques.lower() == "a":
        rat+=1
    elif ques.lower() == "b":
        cat+=1
    else:
        print("answer with A or B.")
        return q2()

def q3():
    global cat, rat
    ques = input("Question 3: Is hamster so cool? A: yeah  B: yeah \n")
    if ques.lower() == "a":
        rat+=1
    elif ques.lower() == "b":
        rat+=1
    else:
        print("answer with A or B.")
        return q3()

q1()
q2()
q3()

if rat > cat:
    print("congrats you are rat")
if cat> rat:
    print("u r cat...")
