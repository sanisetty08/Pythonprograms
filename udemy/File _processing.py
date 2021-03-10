myfile = open("D:\Pysql\Pythonprograms\Fruits.txt")
print(myfile.read())


####################################################################################################
def foo(character, filepath):
    file = open(filepath)
    content = file.read()
    return content.count(character)


print(foo("a", "D:\Pysql\Pythonprograms\Fruits.txt"))

#####################################################################################################
file = open("D:\Pysql\Pythonprograms\Fruits.txt")
content = file.read()

with open("D:\Pysql\Pythonprograms\snail.txt", "w") as file:
    file.write("snail\n")
    file.write(content[:3])

####################################################################################################
with open("D:\Pysql\Pythonprograms\Fruits.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content + "\Apple")
    file.write(content + "\Apple")
####################################################################################################
import time

while True:
    file = open("D:\Pysql\Pythonprograms\Fruits.txt")
    content = file.read()
    print(content)
    time.sleep(3)
