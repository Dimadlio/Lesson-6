n=int(input("Введите общее количество чисел: "))
quantity=0
while (n>0):
    a=int(input("Введите число: "))
    n-=1
    if a==0:
        quantity+=1
print("Чисел равных нулю: ",quantity)
