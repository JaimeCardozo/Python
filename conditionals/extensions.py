def main():
    msg = input("File named: ")
    msg = msg.lower()
    if funcion(msg):
        print("Go!")

def funcion(msg):
    if msg.rfind(".jpg")!= -1 or msg.rfind(".jpeg")!= -1:
        print("image/jpeg")
    elif msg.rfind(".gif")!= -1:
        print("image/gif")
    elif msg.rfind(".png")!= -1:
        print("image/png")
    elif msg.rfind(".pdf")!= -1:
        print("image/pdf")
    elif msg.rfind(".txt")!=-1:
        print("image/txt")
    elif msg.find(".zip")!=-1:
        print("image/zip")
    else:
        print("application/octet-stream")

main()