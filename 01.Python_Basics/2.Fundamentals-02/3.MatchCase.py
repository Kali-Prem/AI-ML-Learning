# Match CASE KEYWORD


color = input("enter your colour: ");

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("stop")
    case _:    #Default cases
        print("Wrong colour entered")