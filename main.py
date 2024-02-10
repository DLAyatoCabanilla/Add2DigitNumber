# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.
# The last line of your program should print the result.
# Example 1 Input
# 39
# Example 1 Output
# 12
# Example 2 Input
# 43
# Example 2 Output
# 7


two_digit_number = input("Name any 2 digit number and I will add them together: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
num1 = two_digit_number[0]
num2 = two_digit_number[1]
num3 = int(num1) + int(num2)
print(f"Adding {num1} and {num2} together from {two_digit_number} will result to {num3}")

#or the code below

# two_digit_number = input()
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# # Add the two integers together
# two_digit_number = first_digit + second_digit
# print(two_digit_number)