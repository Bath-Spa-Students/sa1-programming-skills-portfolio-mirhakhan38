#advanced requirement
# Prompt the user for their name, hometown, and age
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# Handle multiple words for age input and validate it
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")

# Output the collected information
print(f"Name: {name}")
print(f"Hometown: {hometown}")
print(f"Age: {age}")