print('''Welcome to python class''')
age = 30
print("Manju age now is:",age)
#Print single quote along with line
print("'Hello have data with single quote'")
#Print doble quote along with line
print('"Hello have data with double quote"')
#Print doble and single quote along with line
print('''"Hello this line ' contain single and " quote ""''')
print()
Name ='Manjunatha M C'
age ='30'
print(Name ,"Has age of :",age)
print(2*6)
print(67-80)
#At the end what you want to print with parameter end but by default its \n new line
print("Manjunatha has age of:",end=" ")
print("32")
print("Manjunatha has age of:") #y default it took as newline \n
print("32")

""" Formatting: Output Python also supports various formatting options to 
control how the output is presented. For example:"""
Name = "Manjunatha M C"
Age =32
print("{} has age of : {}".format(Name,Age))
#Using f-strings (formatted string literals):
print(f"{Name} has age of :{Age}")
print("{} has age of : {}".format(Age,Name))
with open("output.txt", "w") as f:
    print("""The open() function is used to open a file. 
    You can specify the file path and the mode (read, write, append, etc.).""", file=f)
file_path = 'output.txt'
#Used for read all the content from the file
with open(file_path,'r') as f:
    content = f.read()
    print("data from the output file")
    print(content)
#used for read line from file
with open(file_path,'r') as f:
    content =f.readline()
    print("Reading single line from the output file")
    print(content)
#reading file line by line
with open(file_path,'r') as x:
    for line in x:
        print(line)




