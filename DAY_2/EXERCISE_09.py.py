# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 22:08:05 2021

@author: JAMSHID bek
"""
#09 FOR TAKRORLASH OPERATORI. BATAFSIL: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/09-for-loop
# FntationError: expected an indented block

# Ko'rib turganingizdek for dan keyingi qatorni o'ngga surmaganimiz uchun 
# indentation error (surishda xatolik) degan xabarni oldik.

# Shunigdek, ko'pchilik yo'l qo'yadigan yana bir xato, qo'shimcha qatorlarni 
# surish esdan chiqishi:
    
#     mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
#     for mehmon in mehmonlar:
#         print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")
#     Natija:


# Yuqoridagi kodimizda 4-qatorni o'ngga surmaganimiz uchun, Python
#  bu qatorni tsikl tashqarisida deb qabul qildi va faqatgina 1 marta, 
#  tsikl tugaganidan so'ng bajardi. 

# Huddi shu kabi agar takrorlanishi kerak bo'magan kodni tsikldan so'ng
#  o'ngga surib qo'ysak Python bu qatorni tsiklning tarkibida deb hisoblab, 
#  qayta-qayta bajaradi:
    
#     mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
#     for mehmon in mehmonlar:
#         print(mehmon)
        
#         print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi

# Yuoqirdagi misolda 5-qator o'ngga surilib qolgani uchun Python
#  bu qatorni ham bir necha bor takrorlab, konsolga chiqardi. To'g'ri 
#  kod quyidagicha bo'ladi:
    
#     mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
#     for mehmon in mehmonlar:
#         print(mehmon)
        
#     print(mehmonlar)
#     for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
#     Keling quyidagi misolni ko'ramiz
    
#     sonlar = list(range(1,11))
#     for son in sonlar:
#         print(f"{son} ning kvadrati {son**2} ga teng")
#     Natija:


#     for yordamida yangi ro'yxat ham shakllantirish mumkin:
    
#     sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
#     sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
#     for son in sonlar:  # sonlar dagi har bir son uchun
#         sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
#     ​
#     print(sonlar)
#     print(sonlar_kvadrati)
#     Natija: 
    
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
#     [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#         for va input(): https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/09-for-loop#for-va-input
# for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan 
# olingan qiymatlar bilan to'ldirish mumkin:
    
#     dostlar = [] # bo'sh ro'yxat
#     print("5 ta eng yaqin do'stingiz kim?")
#     for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#         dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
#     print(dostlar)
#     Natija:


# Kodni tahlil qilamiz:

# 1-qatorda bo'sh dostlar ro'yxatini yaratdik

# 2-qatorda ekranga "5 ta eng yaqin do'stingiz kim?" degan xabarni chiqardik

# 3-qatorda tsiklni boshladik. range(5) funktsiyasi 0 dan 5 gacha sonlar 
# ketma-ketligini yaratadi (0,1,2,3,4) tsikl esa n shularning har biriga
#  teng bo'lib chiqquncha davom etadi. 

# 4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan n+1 do'stingizni
#  kiriting deb so'radik. Nima uchun n+1 (n emas)? Sababi n 0 dan 4 gacha 
#  qiymatlarni oladi, foydalanuvchiga tushunarli bo'lishi uchun esa biz
#  "0-do'stingizni ismini kiriting:" deb emas, balki n+1 ya'ni 1-ismni kiriting
#  deb murojat qilyapmiz.

# 5-qatorda shakllangan ro'yxatni konsolga chiqardik.

# for tsikli har qanday dasturlash tilining eng muhim qismlaridan hisoblanadi
#  va biz bu operatoraga hali takror-takror qaytamiz.

#         AMALIYOT: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/09-for-loop#amaliyot
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har 
# bir ismga takrorlanuvchi xabar yozing

# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan 
# xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)


# Kutilgan natija
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir 
# elementining kubini yangi qatordan konsolga chiqaring.


# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar
#  degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) 
# so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga 
# yozing. Ro'yxatni konsolga chiqaring.

 # # !!!AMALIYOT JAVOBLARINI AMALIYOTNI BAJARGACH UNI TEKSHIRIW UCHUNGINQA OCHING!!!

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Ali','Vali','Hasan','Husan','Olim']
for ism in ismlar:
    print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

# Yuoqirdagi tsikl tugaganidan so'ng, 
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)
