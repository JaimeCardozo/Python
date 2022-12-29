msg = input("find ")
msg = msg.strip()
msg = msg.upper()
print(msg)
msg = msg.find("H")
print(msg)
if msg == 0:
    print("H is first position")