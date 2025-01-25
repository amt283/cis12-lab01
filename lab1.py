import math

def main():

    print("Problem 1: Arithmetic Operations")

    # pi variable used for area and volume
    pi = math.pi

    # variables for calculating area
    circle_radius = 5
    area = pi*(circle_radius ** 2)

    print(f"\nThe area of a circle with a radius of {circle_radius} is {area:.1f}")
    # variables for calculating volume
    sphere_radius = 3
    volume = (4/3)*pi*(sphere_radius**3)

    print(f"The volume of a sphere with a radius of {sphere_radius} is {volume:.1f}")
    # variables for calculating hypotenuse
    side_a = 3
    side_b = 4
    side_c = math.sqrt((side_a**2)+(side_b**2))

    print(f"The hypotenuse of a right-angled triangle with sides {side_a} and {side_b} is {side_c}")

    print("\nProblem 2: String Manipulation")

    # variables for string manipulation
    firstname = "April"
    lastname = "Thompson"
    fullname = firstname+" "+lastname

    print(f"\nHi, my first name is {firstname} and my last name is {lastname}")
    print(f"My full name is {len(fullname)} characters long!")
    print(f"This is my name concatenated: {fullname}")
    print(f"This is my name in UPPERCASE: {fullname.upper()}")
    print(f"This is my name in lowercase: {fullname.lower()}")

    print("\nProblem 3: Variable and Data Types")

    # variables for data types/BMI calculation
    age = 35
    height = 5.08
    weight = 160

    print(f"\nAge variable type: {type(age)}")
    print(f"Height variable type: {type(height)}")
    print(f"Weight variable type: {type(weight)}")

    bmi = (weight/((round(height*12))**2))*703

    print(f"My BMI is: {bmi:.1f}")

main()


