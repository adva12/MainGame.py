

file = open("C:/Users/USER/PycharmProjects/pythonProject/daniel-lesson/test.txt" , "a+")
file.write("2adva")
#file.seek(0)
print(file.read())

try:
    file = open("C:/Users/USER/PycharmProjects/pythonProject/daniel-lesson/test.txt" , "r")
    file.write("2adva")
    print(file.read())

except ValueError as e:
    print(e)

