def main(): 
    msg = input("what time is it? ")
    msg = msg.strip()
    msg = msg.replace(" ","")
    time = convert(msg)
    if time>=7 and time <= 8:
        print("breakfast time")
    elif time>=12 and time <= 13:
        print("lunch time")
    elif time >=18 and time<= 19:
        print("dinner time")

def convert(time):
    position = time.find(":")
    hour = float(time[0:position])
    minutes = float(time[position+1:len(time)])
    return float(hour + minutes/60)

main()    