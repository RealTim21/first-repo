import math

def menu():
    print("====================")
    print(" Area Calculator 📐 ")
    print("====================")
    print(
        "1 Triangle",
        "2 Rectangle",
        "3 Square",
        "4 Circle",
        "5 Exit",
    )
    choice = int(input("Enter your choice: "))
    if choice == 1:
        traingle()
    elif choice == 2:
        rectangle()
    elif choice == 3:
        square()
    elif choice == 4:
        circle()
    elif choice == 5:
        exit()
    else:
        print("Invalid choice try again")
        menu()

def traingle():
    print("Enter the base and height of the triangle")
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = (base * height) / 2
    print(f"Area of the triangle is {area}")
    menu()

def rectangle():
    print("Enter the length and width of the rectangle")
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    print(f"Area of the rectangle is {area}")
    menu()

def square():
    print("Enter the side of the square")
    side = float(input("Side: "))
    area = side * side
    print(f"Area of the square is {area}")
    menu()

def circle():
    print("Enter the radius of the circle")
    radius = float(input("Radius: "))
    area = math.pi * (radius ** 2)
    print(f"Area of the circle is {area}")
    menu()