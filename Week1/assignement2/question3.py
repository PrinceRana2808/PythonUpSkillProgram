"""Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print."""
names=input("Enter comma seprated names:")
list_names=list(names.split(","))
print("List of names:", list_names)
