import random

print("ВИСЕЛИЦА")
print("Игра скоро будет доступна")
list_version = ['python', 'java', 'javascript', 'php']
random_1 = random.choice(list_version)
example_1 = random_1[0] + random_1[1] + random_1[2] + '-' * (len(random_1) - 3)
print("Угадай слово " + example_1 + ":")
result_1 = input()
if result_1 == random_1:
    print("Вы выжили!")
else:
    print("Вы проиграли!")
