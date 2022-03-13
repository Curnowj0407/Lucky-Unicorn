

def num_check(question):

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


# Main routine goe here
how_much = num_check(" how much would you like to play with? ", 0, 10)


print ("you will be spending ${}".format(how_much))
#Print the