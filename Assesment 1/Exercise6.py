passcode = "12345"
#while loop to repeatedly ask the user for the password until the correct one is entered
while True:
    passcode_entered = input("Enter the passcode: ")
#print message when the correct password is entered
    if passcode_entered == passcode:
        print("correct! Access granted!")
#break loop once correct passcode is entered
        break
    else:
        print("Incorrect! Please try again.")