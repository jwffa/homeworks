#Merab Tsitskhvaia-ს ამოცანა

height = int(input("მიუთითე შენი სიმაღლე: "))
unit = input("სანტიმეტრებში(CM) თუ ფუტებში(F):")    
if unit.upper() == "CM":
    result = height * 30.48
    print(f"შენ ხარ {result} სანტიმეტრი")
else:
    result = height / 30.48
    print(f"შენ ხარ {result} ფუტი ") 
