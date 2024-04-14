import math
def calculator():
    print("""Welcome to the Four Function Calculator!

         1. Addition
         2. Subtraction
         3. Multiplication
         4. Division""")
    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == '1':  
# Addition
       num1 = float(input(" Enter the first number: "))
       num2 = float(input("Enter the second number: "))
       print("Result:", num1 + num2)

    elif choice == '2':  
# Subtraction
       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))
       print("Result:", num1 - num2)

    elif choice == '3':  
# Multiplication
       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))
       print(f"Result: {num1 * num2:.2f}")

    elif choice == '4':  
# Division
       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))
       if num2 == 0:
           print("Error: Cannot divide by zero!")
       else:
           print(f"Result: {num1 / num2:.2f}")

    else:
       print("Invalid choice. Please enter 1, 2, 3, or 4.")

def geometry_functions():

   print("""Welcome to the Geometry Functions!

         1. Volume of a rectangular prism (length, width, height)
         2. Volume of a sphere (radius)
         3. Volume of a cone (radius, height)
         4. Area of a triangle (base, height)
         5. Area of an equilateral triangle (side)
         6. Area of a circle (radius)
         7. Surface area of a sphere (radius)
         8. Surface area of a cone (radius, height)""")
   choice = input("Enter your choice (1-8): ")

   if choice == '1':  
# Volume of a rectangular prism
       length = float(input("Enter the length of the rectangular prism: "))
       width = float(input("Enter the width of the rectangular prism: "))
       height = float(input("Enter the height of the rectangular prism: "))
       print(f"Volume: {length * width * height:.2f}")

   elif choice == '2':  
# Volume of a sphere
       radius = float(input("Enter the radius of the sphere: "))
       print(f"Volume: {(4/3) * math.pi * radius ** 3:.2f}")

   elif choice == '3':  
# Volume of a cone
       radius = float(input("Enter the radius of the cone: "))
       height = float(input("Enter the height of the cone: "))
       print(f"Volume: {(1/3) * math.pi * radius ** 2 * height:.2f}")

   elif choice == '4':  
# Area of a triangle
       base = float(input("Enter the base length of the triangle: "))
       height = float(input("Enter the height of the triangle: "))
       print(f"Area: {0.5 * base * height:.2f}")

   elif choice == '5':  
# Area of an equilateral triangle
       side = float(input("Enter the side length of the equilateral triangle: "))
       print(f"Area: {(math.sqrt(3) / 4) * side ** 2:.2f}")

   elif choice == '6':  
# Area of a circle
       radius = float(input("Enter the radius of the circle: "))
       print(f"Area: {math.pi * radius ** 2:.2f}")

   elif choice == '7':  
# Surface area of a sphere
       radius = float(input("Enter the radius of the sphere: "))
       print(f"Surface area:{4 * math.pi * radius ** 2:.2f}")

   elif choice == '8':  
# Surface area of a cone
       radius = float(input("Enter the radius of the cone: "))
       height = float(input("Enter the height of the cone: "))
       print(f"Surface area: {math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2)):.2f}")

   else:
       print("Invalid choice. Please enter a number between 1 and 8.")

def arithmetic_formulas():

    print("""Welcome to the Arithmetic Formulas!
        1. Pythagorean Theorem (a^2 + b^2 = c^2)
        2. Quadratic formula (ax^2 + bx + c = 0)
        3. Combinations (n choose k)
        4. Permutations (n permute k)
        5. Mean / Average""")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':  
# Pythagorean Theorem
       a = float(input("Enter the length of side 'a': "))
       b = float(input("Enter the length of side 'b': "))
       print("Hypotenuse length (c):", math.sqrt(a ** 2 + b ** 2))
       
    elif choice == '2':
# Quadratic formula
        a = float(input("Enter the coefficient 'a': "))
        b = float(input("Enter the coefficient 'b': "))
        c = float(input("Enter the constant 'c': "))
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            print("No real roots exist.")
        elif discriminant == 0:
            print("Single real root:", -b / (2 * a))
        elif a == 0:
            print("Cannot utilize formula; cannot divide by zero.")
        else:
            print("Two real roots:", (-b + math.sqrt(discriminant)) / (2 * a), "and", (-b - math.sqrt(discriminant)) / (2 * a))

    elif choice == '3':  
# Combinations

       n = int(input("Enter the total number of items (n): "))
       k = int(input("Enter the number of items to choose (k): "))
       print("Combinations:", math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

    elif choice == '4':  
# Permutations

       n = int(input("Enter the total number of items (n): "))
       k = int(input("Enter the number of items to permute (k): "))
       print("Permutations:", math.factorial(n) / math.factorial(n - k))

    elif choice == '5':  
# Mean / Average
       numbers = input("Enter the numbers separated by space: ").split()
       numbers = [float(num) for num in numbers]
       print("Mean / Average:",sum(numbers) /len(numbers))

    else:
       print("Invalid choice. Please enter a number between 1 and 5.")

def main():
   while True:
       print("""Welcome to the Python Calculator!
       Enter one of the four options to begin:

       1. Four Function Calculator
       2. Geometry Functions
       3. Arithmetic Formulas
       4. Exit Program""")

       choice = input("Enter your choice (1-4): ")

       if choice == '1':
           calculator()

       elif choice == '2':
           geometry_functions()

       elif choice == '3':
           arithmetic_formulas()

       elif choice == '4':
           print("Exiting the program. Goodbye!")
           break

       else:
           print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
   main()


