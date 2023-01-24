class Demo:
    def decorator(self, print_name):
        def wrapper(self):
            print_name()
            print("age")
        return wrapper


    @decorator
    def print_name(self):
        print("name")

    

d = Demo()
d.print_name()
    
    





