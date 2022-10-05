word = str(input('ingrese una palabra: '))
def word_s(word):
    with open("myfile.txt", "r") as f:
        lines = f.readlines()
        print(lines)
        #contar lineas
    for line in lines:
        print(line.rstrip())
         #buscando un elemento
    if (word +"\n") in lines:
        print(lines.index(word+"\n"))
    else:
        return "no se encuentra"

if word_s(word) == "no se encuentra":
    with open("myfile.txt", "a+") as f:
            f.write(word + "\n")
            print(word)
  
        

    
