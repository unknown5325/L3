import math #импортируем библиотеку

rad = int(input("Введите радиус (см): ")) # Запрашиваем радиус
dlina =  round(2*rad*math.pi, 3) # Длина окружности
pl =  round(math.pi*rad**2, 3) # Площадь окружности
kvad = round(rad*math.sqrt(2), 3) # Длина стороны вписанного квадрата:
trel =  round(rad*math.sqrt(3), 3) # Длина стороны вписанного треугольника
trel_OP =  round(2*rad*math.sqrt(3), 3) # Длина стороны описанного треугольника
kvad_OP =  round(2*rad, 3) # Длина стороны описанного квадрата
vasm =  round(2*rad*(math.sqrt(2)-1), 3) # Длина стороны описанного восьмигольника


print(f"Длина равна: {dlina} см или {dlina/100} м") # Выводим результат
print(f"Площадь равна: {pl} см^2 или {pl/10000} м^2") # Выводим результат
print(f"Длина стороны вписанного квадрата: {kvad} см или {kvad/100} м") # Выводим результат
print(f"Длина стороны вписанного треугольника: {trel} см или {trel/100} м") # Выводим результат
print(f"Длина стороны описанного треугольника: {trel_OP} см или {trel_OP/100} м") # Выводим результат
print(f"Длина стороны описанного квадрата: {kvad_OP} см или{kvad_OP/100} м") # Выводим результат
print(f"Длина стороны описанного восьмиугольника: {vasm} см или {vasm/100} м") # Выводим результат


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