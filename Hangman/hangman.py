import random

print("ВИСЕЛИЦА")
print("Игра скоро будет доступна")
list_version = ['python', 'java', 'javascript', 'php']
random_1 = random.choice(list_version)
random_2 = list(random_1)
random_3 = list(len(random_1) * "-")
print("Угадай слово:")
for i in range(10):
    result_1 = str(input("Введите одну из букв:"))
    if result_1 in random_2:
        if random_2.count(result_1) >= 2:
            ind = random_2.index(result_1)
            random_3[ind] = result_1
            random_2[ind] = "-"
        ind = random_2.index(result_1)
        random_3[ind] = result_1
    else:
        print("В слове такой буквы нет, попробуйте снова!")
    print(''.join(random_3))
print("Спасибо за игру!")
print("Посмотрим, насколько хорошо вы справились на следующем этапе)")
