a,b=map(int,input("start va stopni kiriting: ").split())
son = float(input(f"son kiriting ({a} dan {b}) orasida : "))

if son < a or son > b:
    raise Exception(f"son {a} dan {b} orasida bolish kerak")

print("togri!")