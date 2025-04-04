#Dictionary of 10 European countries and their capitals 
quiz = {
     "Belarus":"Minsk",
    "Austria" : "Vienna",
    "Switzerland":"Bern",
    "Serbia" : "Belgrade",
    "Bulgaria" : "Sofia",
    "Denmark" : "Copenhagen",
    "Slovakia" : "Bratislava",
    "Finland" : "Helsinki",
    "Ireland" : "Dublin",
    "Croatia" :"Zagreb",

}

# Step 2: Iterate through the countries and ask questions
for country, correct_capital in quiz.items():
#asking questions
    answer = input(f"What is the capital of {country}? ").strip().lower()
    
    # Check if the answer is correct
    if answer == correct_capital.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_capital}.")