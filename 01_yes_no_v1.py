show_instructions = input("have you played this game before? ").lower()

if show_instructions == "yes" or show_instructions =="y": 
       show_instruction = "yes"
       print("program continues")

elif show_instructions == "y":
       print ("program continues")

elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("display instructions")

else:
       print("please answer yes / no")

       print("you chose {}".format (show_instructions))
