""" string1 = input("enter a string to reverse: ")
newstring = " "
for i in string1:
    newstring = i+newstring
print(newstring) """


color = input("enter color name: ")
color = color.lower();
print(color)
if color=="voilet" or color=="indigo" or\
color=="blue" or color=="green" or\
color=="yellow" or color=="orange" or\
color=="red":
    print("its a rainbow color")
else:
    print("its not a rainbow color")