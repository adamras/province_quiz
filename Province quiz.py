province_capitals_dict = {
"Alberta":"Edmonton",
"British Columbia":"Victoria",
"Manitoba":"Winnipeg",
"New Brunswick":"Fredericton",
"Newfoundland and Labrador":"St. John's",
"Nova Scotia":"Halifax",
"Ontario":"Toronto",
"Prince Edward Island":"Charlottetown",
"Quebec":"Quebec City",
"Saskatchewan":"Regina",
"Yukon":"Whitehorse",
"Nunavut":"Iqaluit",
"Northwest Territories":"Yellowknife"
}

import random

while True:
    user_input = raw_input ("Do you want to play this totally awesome game? Yes or No: ")
    if user_input == "No":
        print "Fine.  I don't even care."
        quit()
    else:
        print("That's cool and you're cool.  YAY KNOWLEDGE!")
        break

provinces = list(province_capitals_dict.keys())
print("Type 'quit' to stop playing")
while True:
    province = random.choice(provinces)
    capital = province_capitals_dict[province]
    capital_guess = raw_input("What is the capital of " + province + "? ")

    if capital_guess == "quit":
        break
    elif capital_guess == capital:
        print ("Correct.  You are a knowledge wizard.")
    else:
        print ("That ain't right, pleb.  The capital of " + province + " is " + capital + ".")
		
print ("This ends the line of questioning.  You are now free to experience your life..")

