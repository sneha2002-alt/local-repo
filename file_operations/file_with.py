with open("practice.txt", "r") as f:
    data = f.read()
    print(data)
new_data = data.replace("python", "Java")
print(new_data)   
    
with open("practice.txt", "w") as f:
    data = f.write(new_data)    