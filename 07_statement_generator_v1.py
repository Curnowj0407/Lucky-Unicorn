def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# main routine goes here
statement_generator("welcome to the lucky unicorn game","*")
print()
statement_generator("congratulations you got a unicorn","!")