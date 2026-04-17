# Multiple except clauses
def read_user_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("File doesn't exist")     
        
    except PermissionError:
        print("Permission denied") 
        
    except Exception as e:
        print("Unexpected error:", e) 
        
read_user_file("practice.txt") 
read_user_file("nonexistent.txt")              