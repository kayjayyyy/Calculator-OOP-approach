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

calculator = calculator_program()
ui = user_interface()

def calcu():
    
    print("\033[36m Let's get started! \033[0m".center(88, "~"))
    print("\n")
    
    # Print the math operation choices
    print("\033[36ma. Multiplication\033[0m".center(85))
    print("\033[36mb. Division\033[0m".center(85))
    print("\033[36mc. Addition\033[0m".center(85))
    print("\033[36md. Subtraction\033[0m".center(85))
