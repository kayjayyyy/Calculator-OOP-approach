# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 7 - Calculator V2 (OOP approach)

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 40)
print("")
print("\033[45m ♥ Welcome to our calculator program! ♥ \033[0m".center(85))

# Ask the name of the user 
name = input("\n\033[033mGood day! What is your name? \033[0m")
print("\n\033[3;33mI hope you are doing well,", name + "!\033[0m")
print("")

from ClassCalc import calculator_program
from User_interface import user_interface

calcu = calculator_program()
ui = user_interface()

def calculator():
    
    print("")
    print("\033[34m Let's get started! \033[0m".center(88, "~"))
    print("\n")

    try:
        math = ui.operations()
                
        first_number = ui.num1()
                
        second_number = ui.num2()
                        
        if math == "a":
            product = calcu.multiplication(first_number, second_number)
            ui.total_product(product)
            
        elif math == "b":
            quotient = calcu.division(first_number, second_number)
            ui.total_quotient(quotient)
        
        elif math == "c":
            sum = calcu.addition(first_number, second_number)
            ui.total_sum(sum)
                          
        elif math == "d":
            difference = calcu.subtraction(first_number, second_number)
            ui.total_difference(difference)
                          
        else:
            print("\n\033[31mError input character!\033[0m")
                 
        while True:
            input_again = ui.ask_again()
            if input_again == "yes":
                calculator()
            else:
                exit()
              
    except ValueError:
        print("INVALID: Error input characters!")

calculator()