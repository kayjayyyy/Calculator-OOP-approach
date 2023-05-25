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
        input_again = str(input("\nDo you want to calculate again (yes or no)? "))
        return input_again
    
    def total_sum(self, sum):
        print("\n\033[32mThe calculated total is: ", sum, "\033[0m")
        
    def total_difference(self, difference):
        print("\n\033[32mThe calculated total is: ", difference, "\033[0m")
        
    def total_product(self, product):
        print("\n\033[32mThe calculated total is: ", product, "\033[0m")
    
    def total_quotient(self, quotient):
        print("\n\033[32mThe calculated total is: ", quotient, "\033[0m")
        