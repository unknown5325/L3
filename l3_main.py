print("Добрый день!")
name = str(input("Добрый день!, Введите имя, по которому к Вам можно обратиться: "))
age = int(input(f"Добрый день! {name}! Введите Ваш возраст, и я посчитаю, сколько Вам осталось до пенсии в годах: "))
pen = 63
ost = pen - age
print(f"Вам осталось {ost} лет до пенсии. Всего доброго!")

'''
import math

spic = (input("Введите список: ")).split()
for i in range(0,len(spic)):
    spic[i] = int(spic[i])
ch = int(input("Введите параметр: "))

print(spic)
sumb = 0
match ch:
    case 0:
            for i in range(0,len(spic)):
                spic[i] = 0
            print(spic)
    case 1:
            for i in range(0,len(spic)):
                spic[i] = spic[i]*2
            print(spic)
    case 2:
            for i in range(0,len(spic)):
                if i%2 == 0:
                    spic[i]= spic[i] + 10
            print(spic)
    case 3:
            for i in range(0,len(spic), 3):
                if spic[i] > 0:
                    spic[i] = math.sqrt(spic[i])
                else:
                    spic[i] = 0
            print(spic)
    case _:
            for i in range(0,len(spic)):
                sumb += spic[i]
            print(sumb)
            '''