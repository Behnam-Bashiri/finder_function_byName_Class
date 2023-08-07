def function_one():
    print("This is function one.")

def function_two():
    print("This is function two.")

def call_function_by_name(function_name):
    # Get the function object from the globals dictionary
    function = globals().get(function_name)
    
    # Alternatively, if the functions are defined in the local scope, you can use locals()
    # function = locals().get(function_name)
    
    if function is not None and callable(function):
        function()
    else:
        print(f"Function '{function_name}' does not exist or is not callable.")

# Example usage:
function_name_to_call = "function_one"
call_function_by_name(function_name_to_call)

function_name_to_call = "function_two"
call_function_by_name(function_name_to_call)

function_name_to_call = "nonexistent_function"
call_function_by_name(function_name_to_call)
