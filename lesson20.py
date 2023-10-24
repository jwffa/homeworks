#Nino Goglichadze-ს ამოცანა:

#TRIANGLE
side_a = int(input("Enter a side's size: "))
side_b = int(input("Enter b side's size: "))
side_c = int(input("Enter c side's size: "))

if (side_a + side_b >= side_c) and (side_c + side_b >= side_a) and (side_a + side_c >= side_b):
    print("ამ სამკუთხედის დახაზვა შესაძლებელია <3 ")
    print("პერიმეტრი უდრის " + str(side_b + side_a + side_c) + "-ს") 
else:
    print("სამკუთხედი არ შეიკრება :( )")
