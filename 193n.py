#Data input
x1 = int(input("Введіть номер стовпця першої клітинки (1-8): "))
y1 = int(input("Введіть номер рядка першої клітинки (1-8): "))
x2 = int(input("Введіть номер стовпця другої клітинки (1-8): "))
y2 = int(input("Введіть номер рядка другої клітинки (1-8): "))

# True when column or row is the same
same_column = (x1 == x2)
same_row = (y1 == y2)
#Result output
if same_column == True or same_row == True:
    print("Yes")
else:
    print("No")
