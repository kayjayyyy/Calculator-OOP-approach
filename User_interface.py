class user_interface:
    
    def operations(self):
        math = input("\n\033[33;3mPlease choose a math operation you want to use (a/b/c/d): \033[0m")
        return math
    
    def num1(self):
        first_number = float(input("\n\033[33;3mEnter your first number: \033[0m"))
        return first_number
        
    def num2(self):
        second_number = float(input("\n\033[33;3mEnter your second number: \033[0m"))
        return second_number
    