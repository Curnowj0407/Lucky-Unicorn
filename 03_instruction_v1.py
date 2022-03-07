def yes_no(question):
    valid = False
    while not valid:
        response  = input(question).lower()

    
    
        if response == "yes" or response =="y": 
                return "yes"

        elif response == "no" or response == "n":
            return "no" 
        else:
            print("please answer yes / no")

def instructions():
    print("**** how to play ****")
    print()
    print("the rules of the game go here")
    print()
    return ""



played_before = yes_no("do you want to See instructions?")


if played_before == "no":
    print("program continues")

else:
    instructions()


