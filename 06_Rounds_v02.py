import random


balance = 5

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
print("final balance",
      balance)
