#match methods allow created differents case of bolean
name = input("What's your name? ")
name = name.upper()
match name:
    case "HARRY":
        print("Gryffindor")
    case "HERMAIONE":
        print("Gryffindor")
    case "RON":
        print("Gryffindor")
    case  "DRACO":
        print("Slytherin")
    case _:
        print("Who?")                
