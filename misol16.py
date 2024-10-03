sonlar = input("sonlar kiriting:  ")
sonlar = list(map(int, sonlar.split(',')))

for i in range(1, len(sonlar)):
    assert sonlar[i] > sonlar[i - 1], "o'sish tartibida emas."

print("o'sish tartibida")