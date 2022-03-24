import random


# checks for yes / no responses
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


# checks for an integer between low and high
def num_check(question, low, high):

    error = "Please enter an integer between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# shows instructions when needed
def instructions():
    print()
    statement_generator("**** how to play ****", "*")
    print()
    print("the rules of the game go here")
    print()
    return ""


# decorate print statements
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# ******** Main Routine starts here *******

statement_generator("Welcome to the LU Game", "-")

# show instructions...
played_before = yes_no("do you want to See instructions?")


if played_before == "no":
    print("program continues")

else:
    instructions()

print()

# Ask user how much they to play with...
how_much = num_check("how much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("press<Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)
    print()
    # adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # the token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:

        # adjust the balance
        # if it's even, choose horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # if it's odd, choose a zebra
        else:
            chosen = "zebra"

        balance -= 0.5

    print("you got a {}, balance: ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("press Enter to play again or 'xxx' to quit")


print()
end_statement = "Thank you for playing.  Your final balance is ${:.2f}".format(balance)
statement_generator(end_statement, "*")
