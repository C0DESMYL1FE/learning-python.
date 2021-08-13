# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:47:17 2021

@author: JAMSHID bek
"""

#07 LIST (RO'YXAT)

# List yordamida bir o'zgaruvchida ko'p qiymatlar saqlashni o'rganamiz.

#         LIST BILAN TANISHAMIZ
# Avvalgi darsimizda biz o'zgaruvchi yaratish, va uning ichida biror
#  qiymatni (matn yoki son) saqlashni o'rgandik. Bunda biz bitta o'zgaruvchiga
#  bitta qiymat berdik xolos. 

# Bugun o'rganadigan navbatdagi mal'umot turi List (ro'yxat) deb ataladi. 
#  Ro'yxat o'z nomi bilan, bitta o'zgaruvchida bir nechta qiymatlarni saqlash 
#  imkonini beradi. Bu qiymatlar List elementlari deyiladi. Ro'yxatda son,
#  matn yoki aralash turdagi elementlarni saqlash mumkin. 

# List quyidagicha yaratiladi:
    
#     mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
#     narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
#     sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
#     ismlar = [] # bo'sh ro'yxat
# Ro'yxat saqlaydigan o'zgaruvchilarni nomlashda -lar  (ko'plik)
# qo'shimchasini qo'shish maqsadga muvofiq bo'ladi (inlgiz tilida -s). 

# Misol uchun: mevalar, uylar, cars, toys, books 

#         LIST ELEMENTLARI
# Ro'yxatdagi har bir element tartib bilan joylashgani sababli, biz istalgan 
# elementga uning tartib raqami (indeksi) bo'yicha murojat qilishimiz mumkin. 

# Dasturlash olamida indeks 0 dan boshlanadi! Ya'ni Listning birinchi 
# elementing tartib raqami (indeksi) 0 ga, ikkinchi elementning indeksi 
# 1 ga teng va hokazo.
        
#         mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
#         print("Birinchi meva: ", mevalar[0])
#         print("Ikkinchi meva: ", mevalar[1])
#         Natija: 
        
#         Birinchi meva: olma 
        
#         Ikkinchi meva: anjir

# Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string 
# metodlarni qo'llashimiz mumkin:

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
#         print("Birinchi meva: ", mevalar[0].title())
#         print("Ikkinchi meva: ", mevalar[1].upper())
#         Natija:
        
#         Birinchi meva: Olma 
        
#         Ikkinchi meva: ANJIR

# List elementlari ustida arifmetik amallar bajarish:
    
#     narhlar = [12000, 18000, 10900, 22000]
#     print(narhlar[2] + narhlar[3])
#     Natija: 32900

# Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat 
# qilish mumkin. Bu usul Listning uzunligini bilmaganda juda asqotadi.
    
#     car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
#     print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 
#     Natija: Volkswagen

#         ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
# Dastur davomida listning tarkibi o'zgarishi, yangi elementlar 
# qo'shilishi, ba'zi elementlar o'chirilishi tabiiy hol. Misol uchun
#  "Bozorlik ro'yxati" degan dasturni tasavvur qilaylik, foydalanuvchi
#  ro'yxatga yangi mahsulotlar qo'shishi, sotib olganlarini esa o'chrishi
#  mumkin. 

#          Elementni o'zgartirish
# Ro'yxatdagi biror elementning qiymatini o'zgartirish uchun, o'sha elementga
#  indeksi bo'yicha murojat qilamiz va yangi qiymat yuklaymiz
    
#     narhlar = [12000, 18000, 10900, 22000]
#     narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
#     narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
#     narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
#     print(narhlar)
#     Natija: [13000, 18000, 11000, 24000]

# Yangi element qo'shish
# .append() metodi
# Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi
#  yordamida ro'yxatning oxiriga qiymat qo'shish:
    
#     mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
#     mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
#     print(mevalar)
#     Natija: ['olma', 'anjir', 'shaftoli', "o'rik", 'tarvuz']

# .append() metodi bo'sh ro'yxatni to'ldrisihda juda qulay usul. Odatda
#  dastur boshida bo'sh ro'yxat yaratilib, dastur davomida ro'yxat foydalanuvchi
#  tomonidan to'ldirib borilishi odatiy hol.
    
#     cars = [] # bo'sh ro'yxat yaratamiz
#     cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
#     cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
#     cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
#     print(cars)
#     Natija: ['Lacetti', 'Nexia 3', 'Cobalt']

#     insert() metodi
# Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() 
# metodidan foydalanamiz. .insert() metodi ichida yangi elementning 
# indeksi va qiymati beriladi:
    
#     cars = ['Lacetti', 'Nexia 3', 'Cobalt']
#     cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
#     print(cars)
#     Natija: ['Malibu', 'Lacetti', 'Nexia 3', 'Cobalt']
    
#     cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
#     print(cars)
#     Natija: ['Malibu', 'Lacetti', 'Damas', 'Nexia 3', 'Cobalt']

#         Elementni o'chirish
# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini 
# yoki qiymatini bilishimiz lozim.

# Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:
    
#     mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#     del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
#     print(mevalar)
#     Natija: ['olma', 'shaftoli', "o'rik", 'anor']

# Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan 
# foydalanamiz. Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan
#      qiymatni yozamiz
    
#     mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#     mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
#     print(mevalar)
#     Natija: ['olma', 'anjir', "o'rik", 'anor']

# .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi 
# qiymatni o'chiradi. Agar ro'yxatning ichida 2 va undan ko'p bir hil 
# qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
    
#     hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
#     hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
#     print(hayvonlar)
#     Natija: ['it', 'sigir', "qo'y", 'quyon', 'mushuk']

#         Elementni sug'urib olish
# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni 
# ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. 
# Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
    
#     bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
#     mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
#     print("Men " + mahsulot + " sotib oldim")
#     print("Olinmagan mahsulotlar: ", bozorlik)
#     Natija:
    
#     Men banan sotib oldim 
    
#     Olinmagan mahsulotlar: ["yog'", 'un', 'piyoz', "go'sht"]

# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat 
# sug'urib olinadi.

#         AMALIYOT
# Quyidagi mashqlarni bajaring:

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini
#  kiriting

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 


# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang
#  (musbat, manfiy, butun, o'nlik). 

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
#  Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa 
#  almashtiring. 

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz
#  eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi 
#  tirik bo'lgan shaxslarning ismini kiriting. 

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib 
# (.pop()), quyidagi ko'rinishda chiqaring:


# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta 
# mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() 
# metodi yordamida o'chrib tashlang. 

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
# metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
# ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

# # !!!AMALIYOT JAVOBLARINI AMALIYOTNI BAJARGACH UNI TEKSHIRIW UCHUNGINQA OCHING!!!

# #ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
# #Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
# print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

# # sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
# print(sonlar)

# # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# sonlar[0] = sonlar[0]+sonlar[-1]
# sonlar[1] = -67.8
# sonlar[4] = sonlar[4] + 37
# del sonlar[5]
# print(sonlar)

# #t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

# #Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
# suhbat qilishni istar edim\n")

# #friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# friends = []
# friends.append('John')
# friends.append('Alex')
# friends.append('Danny')
# friends.append('Sobirjon')
# friends.append('Vanya')
# print(friends)

# #Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# friends.remove('John')
# friends.remove('Alex')
# print(friends)

# #Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.append('Hasan')
# friends.insert(0, 'Husan')
# friends.insert(2, 'Ivan')
# print(friends)

# #Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)