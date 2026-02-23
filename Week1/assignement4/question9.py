"""Write a program that takes a day of the week as input and prints 
whether it's a weekday or weekend using match conditional statements."""

day=input("Enter a day:")
match day:
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("Its a Weekday")
    case "Saturday"|"Sunday":
        print("Its a Weekeend")
    case _:
        print("Enter a Valid Day")