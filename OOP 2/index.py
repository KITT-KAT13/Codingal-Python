class IOstring():
    #constructor
    def __init__(self):
        self.str1 = ""

    # function to get string from user
    def get_string(self):
        self.str1 = input("Enter a string: ")    

    def print_string(self):
        print("Result is:", self.str1.upper())

str1 = (IOstring())

str1.get_string()
str1.print_string()
