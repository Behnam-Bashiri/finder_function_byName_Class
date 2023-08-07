from threading import Thread

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
        return Thread(target=function(), args=())
    else:
        print(f"Function '{function_name}' does not exist or is not callable in the class.")

def threading(objectClass,functionList):
    thread_list = []
    for func in functionList:
        thread_list.append(call_function_by_name(objectClass,func))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

p1 = person('behnam',23,'eng')

threading(p1,['sayAGE','sayJOB'])
