#return a message indicating whether the number is even or odd.
def even_or_odd (n):
    return "Even" if n % 2==0 else "odd"

def main():
#asking the user for a number within the main function
    number= int(input("Enter a number:"))
    if number %2==0:
        print (f"{number} is an even number")
    else:
        print(f"{number} is and odd number")
#call main()
main()