# Matthew Hulle
# Integration Project
# This is an integration of everything that I have learned so far this semester.

print("Hello!")
print("Welcome to my Integration Project.")


print("First, some arithmetic...")
num1 = int(input("Enter a 2-digit number: "))
num2 = int(input("Enter a single-digit number: "))
print("Division: ", num1 / num2)
print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Modulus: ", num1 % num2)


grade = int(input("Now, enter current grade in COP 1500: "))
if (grade >= 91.9):
    print("Fantastic!")
    print("That is an A.")
elif (grade >= 81.9):
    print("Good!")
    print("That is a B.")
elif (grade >= 71.9):
    print("Decent.")
    print("That is a C.")
elif (grade >= 64.9):
    print("Fair.")
    print("That is a D.")
else:
    print("Poor.")
    print("That is an F.")


age = int(input("Now, enter your age: "))
if age >= 19:
    print("You are older than Matt. ")
elif age == 18:
    print("You are the same age as Matt. ")
elif age <= 17:
    print("You are younger than Matt. ")


print("The following code will print your name multiple times.")
name = (input("Enter your name: "))
x = 0
while(x < 5):
    print(name)
    x = x + 1


print("The following code counts down from a number. ")
countdown = int(input("Enter a number to countdown from: "))
while countdown > 0:
    print(countdown)
    countdown = countdown - 1


print("This code finds the sum of 5 user-entered numbers. ")
total = 0
for x in range(5):
    number = int(input("Enter a number: "))
    total += number
print("The total is:", total)


print("This code finds the bigger of 2 numbers. ")
def getBigger(num1, num2):
    if num1 > num2:
        bigger = num1
    else:
        bigger = num2
    return bigger

def main():
    userInput1 = int(input("Enter a number: "))
    userInput2 = int(input("Enter another: "))

    biggerNumber = getBigger(userInput1, userInput2)
    print("The bigger of the two numbers is", biggerNumber)

main()


print("The end. ")





