#dictionary to map the month numbers
month_days={
    1:31, 2:28, 3:30, 4:31, 5:30, 6:31,
    7:30, 8:31, 9:30, 10:31, 11:30, 12:31

}
#get users input
month=int(input("Enter any month number:"))
if 1<= month <= 12:
    print(f"Month {month} has {month_days[month]} days")
else:
    print("Invalid month number! Please enter a valid number")    
