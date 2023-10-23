#Nini Solomonia-ს ამოცანა


list = ["Dato Tkeshelashvili", "Rostom Chagunava", "Soso Valishvili"]

ia_counter = 0

for ia in list:
    for char in ia:
      if char == "i" or char == "a":
        ia_counter += 1

print(ia_counter) 