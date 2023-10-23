#Giorgi Chkhetiani-ს ამოცანა

list = ["Barcelona", "Ajax", "Argentinaa"]

if len(list[1]) < len(list[0]) < len(list[2]):
    print("average is Barcelona - " + str(len(list[0])))
elif len(list[0]) < len(list[1]) < len(list[2]):
    print("average is Ajax - " + str(len(list[1])))
elif len(list[0]) < len(list[2]) < len(list[1]): 
    print("average is Argentinaa - " + str(len(list[2])))
elif len(list[1]) < len(list[2]) < len(list[0]): 
    print("average is Argentinaa - " + str(len(list[2])))
elif len(list[2]) < len(list[1]) < len(list[0]):
    print("average is Ajax - " + str(len(list[1])))
elif len(list[2]) < len(list[0]) < len(list[1]):
    print("average is Barcelona - " + str(len(list[0]))) 
