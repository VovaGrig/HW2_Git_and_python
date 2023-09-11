### This will be our great calculator. Please contribute by writing one of the functions
def plus(my_string): #numbers addition
    ans = int(my_string.split(' ')[0]) + int(my_string.split(' ')[2])
    return ans
def main(): #accepts input, transmits to corresponding function and returns answer 
    my_string = str(input())
    if my_string.split(' ')[1] == "+":
        ans = plus(my_string)
    elif my_string.split(' ')[1] == "-":
        ans = minus(my_string)
    elif my_string.split(' ')[1] == "*":
        ans = multiplication(my_string)
    elif my_string.split(' ')[1] == "/":
        ans = division(my_string)
    return ans
answer = main()
print(answer)