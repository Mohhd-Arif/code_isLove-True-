arrayLength = int(input("enter the length of array "));

arrayElements= input ("enter elements seperated by space");
output = 0

for element in arrayElements.split():
    output+=int(element)

print(output)
