class person:
    def __init__(self,name,age,job) -> None:
        self.name = name
        self.age = age
        self.job = job
    
    def sayHI(self):
        print("hi i'm {} ".format(self.name))

    def sayAGE(self):
        print("my age is {} ".format(self.age))

    def sayJOB(self):
        print("my job is {} ".format(self.job))

def call_function_by_name(class_obj, function_name):
    # Get the function object from the class using getattr()
    function = getattr(class_obj, function_name, None)
    
    if function is not None and callable(function):
        function()
    else:
        print(f"Function '{function_name}' does not exist or is not callable in the class.")


p1 = person('behnam',23,'eng')

call_function_by_name(p1,'sayAGE')
