print("Начинаем варить кофе\n"
      "Измельчение кофейных зерен\n"
      "Кипящая вода\n"
      "Смешивание кипяченой воды с измельченными кофейными зернами\n"
      "Налив кофе в чашку\n"
      "Налить немного молока в чашку\n"
      "Кофе готов!")
count_water = int(input("Напишите, сколько мл воды в кофемашине:"))
count_milk = int(input("Напишите, сколько мл молока в кофемашине:"))
count_coffee_beans = int(input("Напишите, сколько кофейных зерен в кофемашине:"))
number = int(input("Напишите, сколько чашек кофе вам понадобится:"))
water = number * 200
milk = number * 50
coffee_beans = number * 15
if water + 200 <= count_water and milk + 50 <= count_milk and coffee_beans + 15 <= count_coffee_beans:
    N = min(count_water // 200, count_milk // 50, count_coffee_beans // 15) - number
    print("Да, я могу приготовить такое количество кофе (даже на", N, "чашек больше)")
elif count_water >= water and count_milk >= milk and count_coffee_beans >= coffee_beans:
    print("Да, я могу приготовить такое количество кофе")
else:
    N = min(count_water // 200, count_milk // 50, count_coffee_beans // 15)
    print("Нет, я могу приготовить только", N, "чашек кофе")
print("На", number, "чашек кофе понядобится:\n" + str(water) + " мл воды\n" + str(milk) + " мл молока\n" +
      str(coffee_beans) + " кофейных зерен")
