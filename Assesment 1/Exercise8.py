#list of names
Names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#searching for Sam
Target="Sam"
#Check if the name is present or not
if Target in Names:
    print(f"{Target} found in the list!")
else:
    print(f"Oops! {Target} not found in the list")

#Optional requirements
#Allow the user to input the search
Target=input("Search for a name!")
#Check if the name is present or not
if Target in Names:
    print(f"{Target} found in the list!")
else:
    print(f"Oops! {Target} not found in the list")
