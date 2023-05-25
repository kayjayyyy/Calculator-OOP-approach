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

# Import class and ui
from ClassCalc import calculator_program
from User_interface import user_interface

# Assign the object
calcu = calculator_program()
ui = user_interface()

def calculator():
    
    # Lets get started banner
    print("")
    print("\033[34m Let's get started! \033[0m".center(88, "~"))
    print("\n")

    try:
        # Ask the user for mathematical operation to be used
        math = ui.operations()
        
        # Ask the user to input first number        
        first_number = ui.num1()
        
        # Ask the user to input second number        
        second_number = ui.num2()
        
        # Af a; multiplication and print the product               
        if math == "a":
            product = calcu.multiplication(first_number, second_number)
            ui.total_product(product)
        
        # If b; division and print the quotient    
        elif math == "b":
            quotient = calcu.division(first_number, second_number)
            ui.total_quotient(quotient)
        
        # If c; addition and print the sum
        elif math == "c":
            sum = calcu.addition(first_number, second_number)
            ui.total_sum(sum)
        
        # If d; subtraction and print the difference                 
        elif math == "d":
            difference = calcu.subtraction(first_number, second_number)
            ui.total_difference(difference)
        
        # Else, display error                 
        else:
            print("\n\033[31mError input character!\033[0m")
                
        while True:
            # Ask the user if they want to calculate again
            input_again = ui.ask_again()
            
            # If yes, return to calculator
            if input_again == "yes":
                calculator()
            
            # If no, break and exit
            else:
                exit()
              
    except ValueError:
        print("INVALID: Error input characters!")

    # Outro and border line
    print("\n")
    print("\033[3mThank you for supporting our program!".center(85))
    print("")
    print("\033[35m※ \033[0m" * 40)
    print("")

calculator()