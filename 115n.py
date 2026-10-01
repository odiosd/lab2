#Number input
a = int(input("Введіть число a (від 1 до 1000): "))
b = int(input("Введіть число b (від 1 до 1000): "))

# Number check-up
a_ok = 1 <= a <= 1000
b_ok = 1 <= b <= 1000

#Comparing numbers and result output
if a_ok == True and b_ok == True:
    if a > b:
        print("Найбільше число:", a)
    elif b > a:
        print("Найбільше число:", b)
    else:
        print("Числа рівні:", a)
else:
    print("Помилка: числа повинні бути від 1 до 1000")




