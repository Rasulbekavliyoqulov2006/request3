matn = input("matn kiriting: ")

for i in matn:
    if not i.isalpha():
        raise ValueError("faqat harflar bo'lishi kerak.")

print("faqat harflardan iborat.")