# # 1-misol
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# res = map(lambda x: x ** 2, numbers)
# print(list(res))
from itertools import count


# # 2-misol
# hariflar = ["A", "a", "B", "b", "C", "c", "D", "d"]
# result = filter(lambda x: x.isupper(), hariflar)
# print(list(result))

# # 3-misol
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# country_codes = list(map(lambda x: x[:4], phone_numbers))
# print(country_codes)

# # 4-misol
# names = ['alfred', 'tabitha', 'william', 'arla']
# result = map(lambda x: x.capitalize(), names)
# print(list(result))

# # 5-misol
# def raqamlar(numbers):
#     return numbers >= 76
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# result = filter(raqamlar, scores)
# print(list(result))

# # 6-misol
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# result = filter(lambda x: x.lower() == x.lower()[::-1], words)
# print(list(result))

# # 7-misol
# def sozlar_uzunligi(sozlar):
#     return len(sozlar)
#
# sozlar = ['apple', 'banana', 'cherry']
# result = map(sozlar_uzunligi, sozlar)
# print(list(result))

# # 8-misol
# list1 = ['apple', 'banana', 'cherry']
# list2 = ['orange', 'lemon', 'pineapple']
#
# result = [x + y for x, y in zip(list1, list2)]
# print(result)

# # 9-misol
# list1 = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# list2 = ['Sobir', 'Bakir', 'Jalil', 'Toxir']
#
# result = list(map(lambda x, y: x + y, list1, list2))
# print(result)

# # 10-misol
# def count_occurrences_with_map(my_list, element):
#     occurrences = list(map(lambda x: 1 if x == element else 0, my_list))
#     return sum(occurrences)
#
# my_list = [1, 2, 3, 4, 2, 2, 5, 6]
# element = 2
#
# result = count_occurrences_with_map(my_list, element)
#
# print(f"Element {element}, ro'yxatda {result} marta uchraydi.")

# # 11-misol
# I1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# I2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = list(filter(lambda x: x in I2, map(lambda x: x, I1)))
#
# print(list(set(result)))

# # 12-misol
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# result = map(lambda x: programming_languages[x], range(0, len(programming_languages), 2))
# print(list(result))

# # 13-misol
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# result = map(lambda x: programming_languages[x], range(5, len(programming_languages), 1))
# print(list(result))

# # 14-misol
# from collections import namedtuple
#
# talabalar = [
#     ("Abdulaziz", "Orifjonov", 170),
#     ("Azizov", "Muhammadali", 120),
#     ("Kamoronbek", "Muhammadov", 130),
#     ("Sardorbek", "Karimov", 116),
#     ("Abdurahmon", "Abdubannobov", 125)
# ]
#
# baland = None
# eng_baland_ball = 0
#
# ortacha = None
# ortacha_ball = 0
#
# Talabalar = namedtuple("Talabalar", ["name", "firstname", "ball"])
# for i in talabalar:
#     talaba = Talabalar(*i)
#     print(f"Name: {talaba.name}, Firstname: {talaba.firstname}, Ball: {talaba.ball}")
#     ball = talaba.ball
#     if ball > eng_baland_ball:
#         eng_baland_ball = ball
#         baland = talaba
# print(f"Eng Yuqori Ballga ega talaba: Name {baland.name}, Firsname: {baland.firstname}, Ball: {baland.ball}")

# # 15-misol
# def kvadratlar():
#     for i in range(21):
#         yield i
#
# for i in kvadratlar():
#     print(i ** 2)

# # 16-misol
# def uzunlik(matn):
#     def sozlar():
#         return len(matn)
#     return sozlar
#
# closure = uzunlik("Men Orifjonov Abdulaziz man")
# print(closure())

# # 17-misol
# def Salomlashish(ism):
#     def Javob(salomlashish="Salom"):
#         print(f"{salomlashish} {ism}!")
#     return Javob
#
# closure = Salomlashish("Abdulaziz Orifjonov")
# print(closure())