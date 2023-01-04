def main():
    msg = input("File named: ")
    msg = msg.lower()
    if funcion(msg):
        print("Go!")
#change this code: search the position end string and first string last of final doubble
def funcion(msg):
    if msg.rfind(".jpg")!= -1 or msg.rfind(".jpeg")!= -1:
        print("image/jpeg")
    elif msg.rfind(".gif")!= -1:
        print("image/gif")
    elif msg.rfind(".png")!= -1:
        print("image/png")
    elif msg.rfind(".pdf")!= -1:
        print("application/pdf")
    elif msg.rfind(".txt")!=-1:
        print("application/txt")
    elif msg.find(".zip")!=-1:
        print("application/zip")
    else:
        print("application/octet-stream")

main()