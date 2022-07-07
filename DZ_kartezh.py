#1 найти самое большое слово в строке
#2 преобразовать текст в картеж слов с удалением знаков припинания

#1
stroke = ("d", "st", "s", "sta", "stas", "vorobey")
stroke = tuple(stroke)
print(stroke)
print("max", max(stroke))
#2
stas = " ".join(stroke)
print(stas)