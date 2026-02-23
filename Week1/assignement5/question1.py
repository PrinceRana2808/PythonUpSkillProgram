"""Define a function calculate_area that calculates the area of a rectangle and return the result. 
If no width is provided, it defaults to 10."""

def calculate_area(length,width=10):
    return length*width

len=int(input("Enter length of rectangle:"))
wth=input("Enter width of rectangle:")
if wth == "":
    area = calculate_area(len)
else:
    area = calculate_area(len, int(wth))

print(f"Area of Rectangle is {area}")