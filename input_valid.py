# Input validation with exceptions
# Write a program that:

# Asks the user to enter an integer repeatedly until they enter a valid one.

# Print the final integer and the total number of attempts.

count = 0
while True:
    count += 1  
    try:
        n = int(input("Enter a number: "))
        
    except ValueError:
        print("Re-enter valid number") 
      
    else:
        break  
        
        
print(f"The final integer: {n} \nTotal attempts: {count}")        