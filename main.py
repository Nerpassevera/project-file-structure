import src.addition
import src.division
import src.multiplication
import src.subtraction

usr_numbers_str = input("Enter two numbers separated by \",\":  ")
usr_numbers_list = usr_numbers_str.split(",")
usr_numbers = [int(usr_number) for usr_number in usr_numbers_list]

print("Addition result:", src.addition.perform_operation(usr_numbers[0], usr_numbers[1]))
print("Division result:", src.division.perform_operation(usr_numbers[0], usr_numbers[1]))
print("Multiplication result:", src.multiplication.perform_operation(usr_numbers[0], usr_numbers[1]))
print("Subtraction result:", src.subtraction.perform_operation(usr_numbers[0], usr_numbers[1]))