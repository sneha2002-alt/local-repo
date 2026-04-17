# Function that always logs its exit
lst = []
def process_data(data):
    total = 0
    try:
        if len(data) == 0:
            raise ValueError("Empty data")
        for val in data:
            total += val
        avg = total / len(data) 
        print("Average: ",avg)
    except ValueError:
        print("Error: Empty data")
    except TypeError:
        print("Error: Invalid number type")
    except ZeroDivisionError:
        print("Error: Division by zero (internal logic error)")
    finally:
        print("Processing done.") 
    

process_data(lst)
         