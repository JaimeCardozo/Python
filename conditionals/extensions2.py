msg = input("File name: ")
msg = msg.lstrip("abcdefghijklmnñopqrstuvwxyz,_-*+")
upper = "abcdefghijklmnñopqrstuvwxyz,_-*+".upper()
msg = msg.lstrip(upper)
msg = msg.replace(".","")
match msg:
    case  "jpg" | "jpeg":
        print("/jpeg")
    case "png"| "gif":
        print("image/" + msg)
    case "pdf" | "txt" | "zip":
        print("application/" + msg)
    case _:
        print("File name is not valid")