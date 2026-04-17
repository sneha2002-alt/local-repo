def check_word():
    with open("practice.txt", "r") as f:
        word = "learning"
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")  

def check_line():
    word = "Python"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(f"{word} found at line {line_no}")
                break
        
            line_no += 1
            
    return -1        

check_word()  
check_line()