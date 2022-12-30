msg = input("File name: ")
msg = msg.lstrip("abcdefghijklmnñopqrstuvwxyz,_-*+")
upper = "abcdefghijklmnñopqrstuvwxyz,_-*+".upper()
msg = msg.lstrip(upper)
print(msg)
#if ".jpg" in msg or ".jpeg" in msg or ".png" in msg:
 #   print("hi")