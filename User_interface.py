class user_interface:
    
    def operations(self):
        print("\033[36ma. Multiplication\033[0m".center(85))
        print("\033[36mb. Division\033[0m".center(85))
        print("\033[36mc. Addition\033[0m".center(85))
        print("\033[36md. Subtraction\033[0m".center(85))
        math = input("\n\033[33;3mPlease choose a math operation you want to use (a/b/c/d): \033[0m")
        return math
    
    def num1(self):
        first_number = float(input("\n\033[33;3mEnter your first number: \033[0m"))
        return first_number
        
    def num2(self):
        second_number = float(input("\n\033[33;3mEnter your second number: \033[0m"))
        return second_number
    
    def ask_again(self):
        input_again = input("\nDo you want to calculate again (yes or no)? ")
        return input_again