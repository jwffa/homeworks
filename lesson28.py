import random

quantitynums = int(input("How many numbers do you want in your password? : "))
quantitysymbol = int(input("How many symbols do you want in your password? : "))
quantityletter = int(input("How many letters do you want in your password? : "))

listsymbol = ["#", "!", "@", "%", "*", "$"]
listletter = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
              "g", "k", "l", "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x", "y", "z"]
listnumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

listpass = []

for i in range(1, quantityletter + 1):
    listpass.append(random.choice(listletter))

for i in range(1, quantitynums + 1):
    listpass.append(random.choice(listnumber))

for i in range(1, quantitysymbol + 1):
    listpass.append(random.choice(listsymbol))

random.shuffle(listpass)

randpass = ''.join(listpass)
print(f"Your random pass is: {randpass}")
