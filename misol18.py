from datetime import datetime, timedelta    #timedelta gptdan organdim

berilgan_sana = "2024-09-30 14:45:12"
sana = datetime.strptime(berilgan_sana, "%Y-%m-%d %H:%M:%S")
new = sana + timedelta(days=7, hours=3, minutes=15)
edit = new.strftime("%A  %d-%B-%Y %H:%M:%S")
print(edit)