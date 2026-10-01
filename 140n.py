#Data input
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

#Number check-up
if a == 0 or b == 0:
    print("Помилка: на нуль ділити не можна")
else:
    a_dil_b = (b % a == 0)  
    b_dil_a = (a % b == 0)  
#Result output
    if a_dil_b == True and b_dil_a == True:
        print("Кожне з чисел є дільником іншого (числа рівні за модулем)")
    elif a_dil_b == True:
        print("Число a є дільником числа b")
    elif b_dil_a == True:
        print("Число b є дільником числа a")
    else:
        print("Жодне з чисел не є дільником іншого")
