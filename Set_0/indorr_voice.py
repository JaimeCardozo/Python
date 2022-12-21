#This programm convert the letter from capitalize in lowercase
def main():
    sentences = input("write the sentences: ")
    print(lower(sentences))

def lower(sente):
    sente =  sente.swapcase()
    return sente
main()