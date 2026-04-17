def read_file(filename):
    f = None
    try:
        f = open(filename, "r")
        data = f.read()
        print(data)
        
    except FileNotFoundError:
        print("File not found")
        
    finally:
        if f is not None:
            f.close()

read_file("p.txt")                