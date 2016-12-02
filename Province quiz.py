#I don't know how this works.

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

provinces = list(province_capitals_dict.keys())
for i in [1,2,3,4,5]:
    province = random.choice(provinces)
    capital = province_capitals_dict[province]
    capital_guess = raw_input("What is the capital of " + province + "? ")
	
    if capital_guess == capital:
        print ("Correct.  You are a knowledge wizard.")
    else:
        print ("That ain't right, pleb.  The capital of " + province + " is " + capital + ".")
		
print ("Query state ended.  Proceed with your life.")

