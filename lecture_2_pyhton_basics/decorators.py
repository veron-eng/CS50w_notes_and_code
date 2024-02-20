# in python functions are treated as values, they can be passed in and values and can we returned as values 
# decorators, way to take a function and modify it
# its a function and takes in a function and returns a modified version
# functional programing paradim 

def announce(f):
    # so it takes in a function called f
    # typically labelled wrapper as it wraps the function
    def wrapper():
        print("About to run the function....")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello world!")


hello()

# when might this be used: we app only want a certain function to run then use a decorator to wrap the stuff