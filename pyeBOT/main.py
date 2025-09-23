# Chatbot Sederhana dengan Python (sebelumnya project bernama Genesis Core) 
# yang diubah menjadi pyeBOT dan berkemungkinan besar akan dirubah kemabli suata saat nanti
# Dengan menggunakan regex dan random
# Untuk mengenali input dari user dan memberikan respon yang sesuai
# pyeBOT.py (sebelumnya chatbot.py)

import re
import random
from datetime import datetime # <-- IMPORT BARU untuk fitur waktu

# [DATABASE RESPONS VERSI YANG SUDAH DIUPGRADE] 

# List lama yang sudah ditambah variasinya
list_sapaan = [
    "Hai juga", "Haii juga", "Hallo juga, ada yang bisa aku bantu?", "Apa kabar?",
    "Wassup! Ada yang bisa kubantu?", "Yo, ada apa nih?", "Haloo, koneksi ke server Pye.Bot berhasil!"
]
list_perpisahan = [
    "papaiiii", "Sampai jumpa lagi, ya!", "byee", "Okee, dadahh",
    "Okee, cabut dulu ya!", "Nanti kita ngobrol lagi!", "See ya!", "Disconnecting... have a great day!"
]
list_kabar_baik = [
    "Alhamdulillah, aku baik dan semangat!", "Aku baik! Semoga kamu juga ya.", "Baik, makasih udah nanya.",
    "Lagi on fire nih, siap bantu kamu!", "Sistem berjalan optimal. Aku baik!", "Baik dong, kan aku program hehe. Kamu gimana?"
]
list_terima_kasih = [
    "Sama-sama!", "Masamaa!", "Siap, santai aja.",
    "Santuyy", "No worries!", "Siap, dengan senang hati!"
]
list_identitas = [
    "Aku Pye.Bot, asisten virtual yang dibuat olehmu.", "Kenalin, aku Pye.Bot!",
    "Aku Pye.Bot, sebuah AI sederhana dengan mimpi besar, dibuat oleh seorang calon AI Engineer.",
    "Aku ini kumpulan kode yang jadi temen ngobrolmu."
]
list_jokes = [
    "Kenapa nyamuk bunyinya nging? Soalnya dia minum darah, coba kalo minum bensin bunyinya bremmm.",
    "Hewan apa yang paling kaya? Ber-uang.",
    "Pocong apa yang paling disukai ibu-ibu? Pocongan harga!",
    "Kenapa keyboard selalu sabar? Karena dia punya banyak 'kesabaran' (keys-sabar-an).",
    "Server apa yang jago bela diri? Server-Kwon Do."
]

# --- [KATEGORI BARU] ---

# Kategori Waktu & Tanggal (Cerdas & Kontekstual)
def get_time_responses():
    sekarang = datetime.now()
    jam = sekarang.hour
    if 5 <= jam < 11: # Pagi
        return ["Selamat pagi! Sekarang jam " + sekarang.strftime('%H:%M'), "Pagi! Waktunya ngopi sambil ngoding nih."]
    elif 11 <= jam < 15: # Siang
        return ["Selamat siang, jangan lupa makan ya! Udah jam " + sekarang.strftime('%H:%M'), "Siang! Lagi produktif atau ngantuk nih? hehe"]
    elif 15 <= jam < 19: # Sore
        return ["Udah sore nih, bentar lagi istirahat. Sekarang jam " + sekarang.strftime('%H:%M'), "Sore! Semangat selesaikan kerjaan hari ini!"]
    else: # Malam
        return ["Selamat malam! Waktunya istirahat atau lanjut project? Sekarang jam " + sekarang.strftime('%H:%M'), "Udah malem nih di Malang, jangan begadang ya kecuali lagi ngejar deadline."]

# List-list baru
list_kemampuan = [
    "Aku bisa jawab sapaan, kasih jokes receh, dan ngasih tau waktu. Coba aja!",
    "Kamu bisa tanya 'apa kabar', 'kamu siapa', atau minta 'jokes' biar gak tegang.",
    "Kemampuanku masih terbatas, tapi aku terus belajar berkat kamu."
]
list_motivasi = [
    "Pasti bisa! Semangat terus, bro!",
    "Jangan nyerah, error itu bagian dari proses belajar. Kamu lebih hebat dari error itu!",
    "Istirahat dulu kalo capek, besok kita lanjut lagi! Keren udah usaha sejauh ini."
]
list_pujian_kreator = [
    "Tentu aja aku keren, kan yang bikin kamu!",
    "Aku ada karena kehebatan coding-mu.",
    "Aku mungkin cuma program, tapi kreatorku orang hebat."
]
list_bingung = [
    "Waduh, aku belum ngerti soal itu.", "Maaf, otakku belum nyampe. Coba tanya yang lain.",
    "Wah, itu di luar jangkauan memoriku saat ini.",
    "Bisa coba tanya pakai kalimat lain? Mungkin aku lebih ngerti.",
    "Hmm... Error 404: Jawaban tidak ditemukan di databasemarku."
]


print("Pye.Bot:\tHai! Aku Pye.Bot. Ngobrol yuk!")

# --- Logic Utama Chatbot (Struktur Asli + Tambahan) ---
while True:
    user_input = input("Pye.User:\t").lower()

    # 1. Cek Sapaan
    if re.findall(r'halo|hai|hallo|hello|woi|p', user_input):
        print("Pye.Bot:\t", random.choice(list_sapaan))

    # 2. Cek pertanyaan "siapa kamu?"
    elif re.findall(r'kamu siapa|siapa kamu|ini siapa', user_input):
        print("Pye.Bot:\t", random.choice(list_identitas))

    # 3. Cek pertanyaan "apa kabar?"
    elif re.findall(r'apa kabar|gimana kabar|piye kabare', user_input):
        print("Pye.Bot:\t", random.choice(list_kabar_baik))
    
    # 4. Cek permintaan jokes/candaan
    elif re.findall(r'jokes|canda|ngelawak|lucu', user_input):
        print("Pye.Bot:\t", random.choice(list_jokes))

    # 5. Cek ucapan terima kasih
    elif re.findall(r'makasih|terima kasih|thanks|nuwun', user_input):
        print("Pye.Bot:\t", random.choice(list_terima_kasih))

    # <-- BLOK BARU: Kemampuan Bot -->
    elif re.findall(r'kamu bisa apa|bisa apa aja|help|bantuan', user_input):
        print("Pye.Bot:\t", random.choice(list_kemampuan))

    # <-- BLOK BARU: Waktu & Tanggal -->
    elif re.findall(r'jam berapa|sekarang jam|waktu|tanggal', user_input):
        print("Pye.Bot:\t", random.choice(get_time_responses())) # Memanggil fungsi

    # <-- BLOK BARU: Motivasi -->
    elif re.findall(r'semangat|capek nih|pusing|lelah', user_input):
        print("Pye.Bot:\t", random.choice(list_motivasi))
        
    # <-- BLOK BARU: Pujian Kreator -->
    elif re.findall(r'kamu keren|bot pintar|hebat kamu', user_input):
        print("Pye.Bot:\t", random.choice(list_pujian_kreator))

    # Blok Perpisahan (tetap di dekat akhir)
    elif re.findall(r'bye|dadah|papai|udah dulu|keluar', user_input):
        print("Pye.Bot:\t", random.choice(list_perpisahan))
        break # Perintah untuk menghentikan loop

    # Blok terakhir jika tidak ada yang cocok sama sekali
    else:
        print("Pye.Bot:\t", random.choice(list_bingung))
