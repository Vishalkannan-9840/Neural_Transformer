import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multi(n1 , n2):
    return n1 * n2
def divi(n1 ,n2):
    return n1 / n2
continue_1=False
while continue_1 is False:
        first_number=int(input("Please enter a First Number : "))
        math_operator=input("please enter a mathematical operator +, -, *, / : ")
        second_number=int(input("Please enter the second number : "))
        operation={"+":add,
                     "-":sub,
                     "*":multi,
                     "/":divi}
        operant=operation[math_operator]
        result=operant(first_number,second_number)
        print(result)
        continue_1=input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ").lower()
        while continue_1=="y":
            first_number=result
            math_operator = input("please enter a mathematical operator +, -, *, / : ")
            second_number = int(input("Please enter the second number : "))
            operation = {"+": add,
                         "-": sub,
                         "*": multi,
                         "/": divi}
            operant = operation[math_operator]
            result = operant(first_number, second_number)
            print(result)
            continue_1 = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ").lower()

            if continue_1=="n":
                continue_1=False