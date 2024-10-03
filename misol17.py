from datetime import datetime

sana ="2024-09-30 14:45:12"

sana = datetime.strptime(sana, "%Y-%m-%d %H:%M:%S")

edit = sana.strftime("%d/%B/%Y, soat %I:%M:%S %p")

print(edit)