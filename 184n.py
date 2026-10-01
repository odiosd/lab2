#Data input
n = int(input("Введіть n (кількість частинок по одній стороні): "))
m = int(input("Введіть m (кількість частинок по іншій стороні): "))
k = int(input("Введіть k (скільки частин потрібно відламати): "))

can_break = False

#Devision calculation
if k > 0 and k < n * m:
    if k % n == 0 or k % m == 0:
        can_break = True
#Result output
if can_break == True:
    print("Yes")
else:
    print("No")
