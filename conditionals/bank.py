#this code take a greeting for give a valur (20, 100, 0) depend of resquest 
msg = input("Greeting: ")
msg = msg.strip()
msg = msg.upper()
if msg.find("HELLO") == 0:
    print("0")
elif msg.find("H") == 0:
    print("20")
else:
    print("100")
