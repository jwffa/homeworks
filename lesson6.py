age = int(input("Enter your age: "))
father_age = int(input("Enter your father's name: "))
year = 2023
for i in range(5):
    print(str(year + i) + " წელს მამაშენი იქნება " + str(father_age + i) + " წლის და შენ იქნები " + str(age + i) + 
           " წლის,  ხოლო მამაშენი შენზე უფროსი იქნება " + str(father_age - age) + " წლით ")
