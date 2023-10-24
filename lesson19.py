#Rostom Chagunava-ს ამოცანა:

age = int(input("Enter your age: "))
height = int(input("Enter your height: ")) 
weight = int(input("Enter your weight: "))

if age >= 18 and age <= 27 and height >= 160 and height <= 230 and weight >= 55 and weight <= 130:
    print("გილოცავთ, თქვენ ჩაირიცხეთ სავალდებულო სამხედრო სამსახურში!")
else:
    print("სამწუხაროდ თქვენი მონაცემები არ შესაბამება ჩვენს მოთხოვნებს")
