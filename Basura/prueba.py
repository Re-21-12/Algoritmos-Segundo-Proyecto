
code = input('ingresa: ')
def ingresa(ingresa):
  myfile = open("myfile.txt", "r")
  myline = myfile.readline()
  while myline:
    print(myline)
    myline = myfile.readline()
    if code in myline:
      print("si")
    else:
      print("no")
      myfile =  open("myfile.txt", "a")
      myfile.write("\n"+ code)
        
  myfile.close()   
