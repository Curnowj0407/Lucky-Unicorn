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



played_before = yes_no("have you played the game before?")


if played_before == "yes":
    print("program continues")

else:
    instructions()
