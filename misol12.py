malumot = {
    "ism": "rasulbek",
    "familiya": "Avliyokulov",
    "yosh": 18
}
kalit = input("kalitni kiriting: ")

try:
    qiymat = malumot[kalit]
    print(f"{kalit} : {qiymat}")
except KeyError:
   
    print(f"{kalit} kaliti'atda mavjud emas.")