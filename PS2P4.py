firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print ("Hello  " + lastname + " " + firstname)

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

print("Select operation.")
print("1.Add")
print("2.Multiply")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "*", num2, "=", multiply(num1, num2))

        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
