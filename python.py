weight = int(input("please enter your weight  "))
char = "k" , "K" , "P" , "p"
unit = input("if your weight is in kg press k  and if your weight is in pounds press p ")
if unit == "k" or unit =="K":{
    print("weight in kg is this ", weight / 2)
}
else :
    weight = weight / 3
    print("weight in pounds is following " , weight) 

