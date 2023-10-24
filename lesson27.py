import random

goeli = ["tsitskhvaia", "tyeshelashvili", "helios", "sartania", "solomonia",
                "janezashvili", "molodini", "chagunava"]


for i in range(len(goeli)):
    correctanswer = random.choice(goeli)
    print(correctanswer, "Your answer is correct and you have 1 point")
    goeli.remove(correctanswer)
