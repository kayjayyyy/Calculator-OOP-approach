from User_interface import user_interface

class NewInterface(user_interface):
    
    def total_power(self, power):
        print("\n\033[32mThe calculated total is: ", power, "\033[0m")
        
    def total_modulo(self, total):
        print("\n\033[32mThe calculated total is: ", total, "\033[0m")