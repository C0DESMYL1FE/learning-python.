# -*- coding: utf-8 -*-
"""
 Created on Wed Aug  4 21:09:25 2021

 @author: JAMSHID bek
"""
# #04 O'ZGARUVCHILAR. BATAFSIL: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/04-variables
# Pythonda o'zgaruvchilar bilan ishlashni o'rganamiz

#         O'ZGARUVCHI (VARIABLE): https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/04-variables#ozgaruvchi-variable
# O'zgaruvchi —kompyuter xotirasida ma'lum bir qiymatni saqlash uchun 
# ajratilgan joy. Soddaroq qilib tushuntirsak, o'zgaruvchini quti, quti ichidagi
#  narsani esa qiymat deb tasavvur qilish mumkin. Pythonda qiymatlar son, matn,
#  ro'yxat va hokazo ko'rinishida bo'lishi mumkin.


# O'zgaruvchilarni kerakli buyumlar (ma'lumotlat) saqlanadigan, nomlangan 
# qutilarga o'xshatish mumkin
# Quyidagi misolga e'tibor bering, biz 2 ta o'zgaruvchi yaratdik (ism va yosh)
#  va ularga qiymatlar yukladik (Pythonda boshqa tillardagi ka'bi 
# o'zgaruvchilarni avvaldan e'lon qilish yo'q):

#     ism = "Abdulloh"
#     yosh = 25
#     print(ism)
#     print(yosh)
# Natija:

#     Abdulloh

#     25

# O'zgaruvchi (variable) bunday deyilishiga sabab, uning qiymati istalgan 
# vaqt o'zgartirilishi mumkin:

#     ism = "Abdulloh"
#     print(ism)
#     ism="Muhammad"
#     print(ism)
# Natija:

#     Abdulloh
    
#     Muhammad

# Yuqoridagi misolda ism nomli o'zgaruvchiga avval Abdulloh keyin esa
#  Muhammad qiymatlarini berdik.

#        O'ZGARUVCHILARNI NOMLASH: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/04-variables#ozgaruvchilarni-nomlash
# !!!O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:

# O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak

# O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas

# O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar 
# (0-9) va pastki chiziq (_) qatnashishi mumkin

# O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas

# O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi 
# (ism, ISM, va Ism uchta turli o'zgaruvchi)

# Qo'shimcha qoida sifatida: 

# O'zgaruvchi nomini kichik harflar bilan yozing. 

# O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini 
# pastki chiziq (_) bilan ajrating (ism_sharif="Anvar Narzullaev")

# O'zgaruvchiga tushunarli nom bering (y=20 emas yosh=20, d="Korea" emas 
# davlat = "Korea" va hokazo)

# Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va 
# maxsus kalit so'zlarning (keywords) nomini bermang. Kalit so'zlar
#  ro'yhatini ko'rish uchun Spyder konsolida avval help() deb yozing va
#  Enter tugmasini bosing. Keyin esa keywords deb kiritib, yana Enter bosing. 


# Bu so'zlardan o'zgaruvchilarni nomlashda foydalanmang
#         AMALIYOT: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/04-variables#amaliyot
# Quyidagi mashqlarni bajaring:

#     "Hello World!" matnini yangi o'zgaruvchiga 
#     yuklang va print() yordamida konsolga chiqaring

#     xabar deb nomlangan o'zgaruvchiga biror matn yuklang va 
#     konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat 
#     berib uni ham konsolga chiqaring.

#     class deb nomlangan o'zgaruvchi yarating, unga biror qiymat 
#     bering va konsolga chiqaring (siz kutgan natija chiqdimi?)

# Quyidagi kodni bajaring:

#     radius = 5
#     pi = 3.14159
#     aylana_yuzi = pi * radius**2
#     print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)


# !!!AMALIYOT JAVOBLARINI AMALIYOTNI BAJARGACH UNI TEKSHIRIW UCHUNGINQA OCHING!!!
# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() 
# yordamida konsolga chiqaring
matn = "Hello World!"
print(matn)

# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring,
 # keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = "Assalom alaykum"
print(xabar)

# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va 
# konsolga chiqaring (siz kutgan natija chiqdimi?)
# O'zgaruvchini class deb nomlash mumkin emas, sababi class bu maxsus kalit so'z.

#Quyidagi kodni bajaring
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)
