### This will be our great calculator. Please contribute by writing one of the functions
def division(num1, num2):
    return num1 / num2

def main(): #accepts input, transmits to corresponding function and returns answer 
    my_string = str(input())
    num1 = my_string.split(' ')[0]
    num2 = my_string.split(' ')[2]
    if my_string.split(' ')[1] == "+":
        ans = plus(num1, num2)
    elif my_string.split(' ')[1] == "-":
        ans = minus(num1, num2)
    elif my_string.split(' ')[1] == "*":
        ans = multiplication(num1, num2)
    elif my_string.split(' ')[1] == "/":
        ans = division(num1, num2)
    return ans
answer = main()
print(answer)
