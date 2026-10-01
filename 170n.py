#Data input
n = int(input("Введіть трицифрове ціле число: "))

#Negative numbers
m = abs(n)

# Three digit number check
is_three_digit = (100 <= m <= 999)
#Each number transform
if is_three_digit == True:
    d1 = m // 100        
    d2 = (m // 10) % 10  
    d3 = m % 10         
#Result output
    if d1 == d2 and d2 == d3:
        print(3)
    elif d1 == d2 or d1 == d3 or d2 == d3:
        print(2)
    else:
        print(0)
else:
    print("Помилка: число має бути трицифровим")
