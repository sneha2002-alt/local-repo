# Safe integer division
def safe_divide(a, b):
    try:
        result = a/b
        print(result)
        return result
        
    except ZeroDivisionError:
        print("Division by zero not allowed")
        return None
    
try:    
    num1 = int(input("Enter 1st number:"))     
    num2 = int(input("Enter 2nd number:"))  
    safe_divide(num1, num2)  

except ValueError:
    print("provide numbers only")

   
  
 

    



 
       

