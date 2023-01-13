def main():
    students = []
    #students.append(student("Harry","Gryffindor", "Stag"))
    number = int (input("Number students: "))
    for i in range(number):
       name = input("Digit name: ")
       house = input("Digit house: ")
       patronous = input("Digit patronus: ")
       student={
        "name": name,
        "house": house,
        "patronus": patronous 
        }
       students.append(student) 
    
    for student in students:
        print(student["name"],student["house"],student["patronus"],sep=", ")

main()    