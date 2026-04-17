light = input("Enter color of traffic light: ")

match light:
  case "green":
    print("GO")
  case "red":
    print("STOP")
  case "yellow":
    print("LOOK")
  case _:
    print("Wrong color!")  