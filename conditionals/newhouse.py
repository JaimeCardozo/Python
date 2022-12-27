#match methods allow created differents case of bolean
name = input("What's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermaione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case  "Draco":
        print("Slytherin")
    case _:
        print("Who?") 