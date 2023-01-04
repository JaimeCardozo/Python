def main():
    msg = input("File named: ")
    msg = msg.lower()
    msg = msg.strip()
    Format = funcion(msg)
    print(Format)
    match Format:
        case  "jpg" | "jpeg":
          print("image/jpeg")
        case "png"| "gif":
          print("image/" + Format)
        case "txt":
          print("text/" + Format)
        case "pdf" | "zip":
          print("application/" + Format)
        case _:
          print("application/octet-stream")  
#change this code: search the position end string and first string last of final doubble
def funcion(msg):
    position_initial = msg.rfind(".")
    position_final = len(msg)
    format = msg[position_initial + 1:position_final]
    return format
main()