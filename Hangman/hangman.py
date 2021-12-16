import random

print("ВИСЕЛИЦА")
print("Игра скоро будет доступна")
list_version = ['python', 'java', 'javascript', 'php']
random_1 = random.choice(list_version)
random_2 = list(len(list(random_1)) * "-")

print("Угадай слово:")
result_1 = input()
if result_1 == random_1:
    print("Вы выжили!")
else:
    print("Вы проиграли!")
