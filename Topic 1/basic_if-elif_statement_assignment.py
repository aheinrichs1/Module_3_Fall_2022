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
else:  # Also exits program with invalid input message
    print("Invalid user input, exiting program")
