# Ⅰ. if-else , else-if :-                                                        Ⅱ Ⅲ Ⅳ

male = True
tall = False


if male and tall: 
    #  *(if statement with "and" operator)
    print("you are male and tall")

elif not(male) and tall:
    print("you are not male but you are tall")

elif male and not(tall):
    print("you are male but not tall")

else:
    print("you are neither male nor not tall")



# Ⅱ. if-else with some comparison operators :-

def max_num(num1, num2, num3):
    #     *(def is the keyword for a Function)
    if num1 >= num2 and num1>=num3:
         print(num1)
    elif num2 >= num3 and num2>=num1:
         print(num2)
    else:
         print(num3)


max_num(1,2,3)
