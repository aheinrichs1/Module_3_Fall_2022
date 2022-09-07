"""
Docstring pulled from blackboard
In the shell or in a text editor, write a program that asks
for the user to sign up for Programmer's Toolkit
Monthly Subscription Box. They must select level
of membership they want. Each month is something
different, t-shirts, stickers, figurines, even
programming books!
The levels are the following:
Platinum
Gold
Silver
Bronze
Free Trial
Write an if statement that prints the cost
for each of the level. Platinum is $60,
each level below is 10 dollars cheaper,
and the free trial is free.
Submit your .py file.
"""

# pseudocode pulled from /main/lecture/topic1assignmentexample.py
# Print some details to the screen
# talk about the Prog Toolkit Month
# talk about what it could include
# list out the levels
print("Please sign up for Programmer's Tookit Monthly Subscription Box! "
      "\nWe offer something different each month: t-shirts, stickers,"
      "\nfigurines, even programming books, exciting! "
      "\nThere are four different levels to choose from:"
      "\n     Platinum"
      "\n     Gold"
      "\n     Silver"
      "\n     Bronze"
      "\nAnd we offer a free trial!"
      "\nPlease enter what you would like to hear more about:")

# please select a level to hear the price
# Get some sort of input from the user
user_input = input("Type 1 for Platinum"
                   "\n     2 for Gold"
                   "\n     3 for Silver"
                   "\n     4 for Bronze"
                   "\n     5 for our free trial"
                   "\n  or 6 if you would like to exit"
                   "\n")

# figure which level the user selected; the hw wants us to use an if statement
# if the user selected platinum then print 'the cost is $60'
# if the user selected gold then print 'the cost is $10'
# ...
if user_input == "1":  # Platinum
    print("The price of the platinum membership is $60")
elif user_input == "2":  # Gold
    print("The price of the Gold membership is $50")
elif user_input == "3":  # Silver
    print("The price of the Silver membership is $40")
elif user_input == "4":  # Bronze
    print("The price of the Bronze membership is $30")
elif user_input == "5":  # Free trial
    print("The free trial has no cost!")
elif user_input == "6":  # Exits program
    print("Exiting program")
else:  # Also exits program with invalid input message,
    # catches any other input including other types!)
    print("Invalid user input, exiting program")

# test cases
# input: 1
# expected: print("The price of the platinum membership is $60")
# actual: print("The price of the platinum membership is $60")
# input: 7
# expected: print("Invalid user input, exiting program")
# actual: print("Invalid user input, exiting program")
# input: hello
# expected: print("Invalid user input, exiting program")
# actual: print("Invalid user input, exiting program")
# input: 5
# expected: print("The free trial has no cost!")
# actual: print("The free trial has no cost!")
