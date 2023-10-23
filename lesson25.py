#რატი მურღულიას ამოცანა



name1 = input("Enter your name: ")
name2 = input("Enter your name: ")
list = [name1]
list1 = [name2]

name1_a_counter = 0
for element in list:
    for char in element:
        if char == "a":
           name1_a_counter += 1
print(name1_a_counter)


name2_a_counter = 0
for element1 in list1:
    for char1 in element1:
        if char1 == "a":
           name2_a_counter += 1
print(name2_a_counter)

if name1_a_counter > name2_a_counter:
    print("პირველ სახელში არის მეტი a")
else:
    print("მეორე სახელში არის მეტი a")
