# Chatbot Sederhana dengan Python
# Dengan menggunakan regex dan random
# Untuk mengenali input dari user dan memberikan respon yang sesuai
# chatbot.py 

import re
import random

bot_menyapa = ["Hai juga", "Haii juga", "Hallo juga", "Apa kabar?"]
bot_menyapa2 = ["papaiiii", "jumlagi", "sampai jumpa lagi, ya", "byee", "dadahh"]

while True:
    a = input("Pye.User:\t")
    if re.findall(r'halo|hai|haii|halloo|hello|halloww', a, re.I):
        print("Pye.Bot:\t", random.choice(bot_menyapa))
    else:
        print("Pye.Bot:\t", "Maaf, akuu tidak mengerti sama sekalii.")
    if re.findall(r'bye|dadah|pa|pa pa|papaiii|jumlagi', a, re.I):
        print("Pye.Bot:\t", random.choice(bot_menyapa2))
        break