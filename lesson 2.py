import datetime
import array as arr

def run():
    print("bar")

def run2(name):
    print(name + "!")

def run3():
    return ("adva parhi")

def run4(num,num2):
    return num + num2

def run5(num,num2=10):
    return num + num2
run()
run2("adva")
print(run3())
print(run4(2,3))
print(run5(2))
print(run5(2,2))

x = 1
def a():
    global y
    y = 7
    print(x)
    print(y)

def b():
    print(y)
a()
b()

print(datetime.datetime.now())

list=[1,2,3,4]
print(list[3])
list.pop(2)
print(list[2])
list.append(3)
print(list[2])
list.insert(0,56)
print(list[0])

for i in list:
    print(i)

print(" bbbbbbb")
for i in range(len(list)):
    print(list[i],end=" ")

print("vvvv")

my_tupel= 1,2,3,4,5
for x in my_tupel:
    print(x)

my_dic={'A':1,'B':22,'C':333,'D':True}
print(my_dic.keys())
print(my_dic.values())
my_dic['A']=4
print(my_dic['A'])
del(my_dic['A'])
print(my_dic.keys())
print(my_dic.values())

for i in range(5):
    print("iteration number: " + str(i+1))
listA = [12,234,33,234,77,8,98,604]
sum = 0
for i in range(len(listA)):
    sum += listA[i]

print(sum)

for i in range(6):
    print(i*"#")

smallest = listA[0]

for i in range(len(listA)):
    if listA[i] < smallest:
        smallest = listA[i]


print(smallest)

a = arr.array("i",[1,2,3,4,5])
for x in a:
    print(x)