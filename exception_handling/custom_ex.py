# Raising a custom exception
    
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age <= 0 or age > 150:
        raise InvalidAgeError(f"Invalid age: {age} (must be 1 - 150)")
    else:
        print("Valid age")
    
try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError:
    print("Please enter a valid number.")
except InvalidAgeError as e:
    print(e)    