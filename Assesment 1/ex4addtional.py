#Dictionary of 10 European countries and their capitals 
question={
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
    
#asking questions
for country, capital in question.items():
    answer=input(f"What is the Capital of {country}?").strip().lower()
if answer==capital.lower():
    print(f"Correct! The capital of {country} is {capital}.")
else: 
    print(f"Wrong! The correct answer is {capital}.")