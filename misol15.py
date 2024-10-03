sonlar = input("solar kiriting:  ")
sonlar = list(map(int, sonlar.split(',')))

for i in range(2, len(sonlar)):
    assert sonlar[i] == sonlar[i - 1] + sonlar[i - 2], "kiritilgan sonlar fibananchi emas."
    
print("sonlar fibanachi")