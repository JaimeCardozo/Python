def main():
    msg = input("File named: ")
    msg = msg.lower()
    Format = funcion(msg)
    print(Format)
    match Format:
        case  "jpg" | "jpeg":
          print("/jpeg")
        case "png"| "gif":
          print("image/" + Format)
        case "pdf" | "txt" | "zip":
          print("application/" + Format)
        case _:
          print("File name is not valid")     
#change this code: search the position end string and first string last of final doubble
def funcion(msg):
    position_initial = msg.rfind(".")
    position_final = len(msg)
    format = msg[position_initial + 1:position_final]
    return format
main()