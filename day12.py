print("Start the project again. TT")
# Function
"""
def greeting(person_name):
    return "Hello " + person_name

def calc_price(num_apple, apple_price = 35):
    return num_apple * apple_price
print(calc_price(4, 50))
"""


# Args // Kwargs
def add(*args):
    result = 0
    for element in args:
        result += element
    return result


