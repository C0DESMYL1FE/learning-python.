# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:21:24 2021

@author: JAMSHID bek
"""

#05 STRING (MATN) BATAFSIL: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string
# STRING ma'lumot turi va uning ustida amallar

#         STRING VA UNICODE: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#string-va-unicode
# STRING (matn) —Pythondagi eng mashxur ma'lumot turlaridan biri. Avvalgi
#  darsda ko'rganimizdek, o'zgaruvchiga matn yuklash uchun matn qo'shtirnoq
#  (" ") yoki birtirnoq (' ') ichida yozilishi kerak.

# shahar = "Қўқон"
# viloyat = 'Фарғона'
# Pythonda matnlar Unicode jadvalidagi istalgan belgilaridan iborat bo'lishi
#  mumkin (jumladan o'zbek, arab, hind, xitoy alifbosidagi harflar yoki turli 
#          emoji-smayliklar). 

#     matn = "Men yangi 📱 oldim"
#     print(matn)
#     Natija: Men yangi 📱 oldim


# UNICODE jadvalidagi harf va belgilarga misol
#         STRING USTIDA AMALLAR: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#string-ustida-amallar
# Matnlarni qo'shish operatori (+)
# Matnlarni qo'shish uchun + operatoridan foydalanmiz:

#     ism = 'Ahmad'
#     print("Mening ismim " + ism)
#     Natija: Mening ismim Ahmad

#     ism = 'Ahad'
#     familiya = 'Qayum'
#     print(ism + familiya)
#     Natija: AhadQayum

# Yuqoridagi kodda ism va familiya orasiga bo'shliq belgisini qo'shmaganimiz 
# uchun ikki matn qo'shilib yozildi. Buni to'g'rilash uchun, 3-qatorni 
# quyidagicha yozamiz:
    
#     ism = 'Ahad'
#     familiya = 'Qayum'
#     print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz
#     Natija: Ahad Qayum

#         f-string: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#f-string
# Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish 
#       uchun f-string usulidan  f"{matn1} {matn2}" ham foydalansak bo'ladi:

#     ism = "Ahad"
#     familiya = 'Qayum'
#     ism_sharif = f"{ism} {familiya}"
#     print(ism_sharif)
#     Bu usul yordamida uzun matnlarni ham yasash mumkin:
    
#     ism = "James"
#     familiya = 'Bond'
#     print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
#     Natija: Salom, mening ismim Bond. James Bond!

#         Mahsus belgilar: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#mahsus-belgilar
# Matnga bo'shliq qo'shish uchun \t belgisidan, yangi qatordan boshlash
#  uchun \n belgisidan foydalanamiz:
    
#     print('Hello World!')
#     print('Hello \tWorld!')
#     print('Hello \nWorld!')
# Natija:
    
#     Hello World! 
    
#     Hello    World! 

#     Hello 

#     World!

#         STRING METODLARI: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#string-metodlari
# Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami 
# mavjud. Bunday amallar to'plami metodlar deb ataladi. 

# Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida 
# yoziladi. Keling shunday metodlarning ba'zilari bilan tanishaylik.

#         upper() va lower() metodlari: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#upper-va-lower-metodlari
# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 
    
#     ism = 'Ahad'
#     familiya = 'Qayum'
#     ism_sharif = f"{ism} {familiya}"
#     print(ism_sharif.upper())
#     Natija: AHAD QAYUM

# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
    
#     ism = 'Ahad'
#     familiya = 'Qayum'
#     ism_sharif = f"{ism} {familiya}"
#     print(ism_sharif.lower())
#     Natija: ahad qayum
        
#         title() va capitalize() metodlari: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#title-va-capitalize-metodlari
# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 
    
#     ism_sharif = 'james bond'
#     print(ism_sharif.title())
#     Natija: James Bond

# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
    
#     ism_sharif = 'james bond'
#     print(ism_sharif.capitalize())
#     Natija: James bond

# Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga
#  ham qo'llash mumkin (aslida o'zgaruvchi ham matnning 
#  (yoki boshqa ma'lumotning) manzili xolos)
    
#     print('james bond'.upper())
#     Natija: JAMES BOND

#         strip(), rstrip() va lstrip() metodlari: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#strip-rstrip-va-lstrip-metodlari
# Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.

# lstrip() — matn boshidagi bo'shliqni,

# rstrip() – matn oxiridagi bo'shliqni,

# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
    
#     meva = "     olma     "
#     print("Men " + meva.lstrip() + " yaxshi ko'raman")
#     print("Men " + meva.rstrip() + " yaxshi ko'raman")
#     print("Men " + meva.strip() + " yaxshi ko'raman")
#     print("Men " + meva + " yaxshi ko'raman")
#     Men olma      yaxshi ko'raman 
    
#     Men       olma yaxshi ko'raman 
    
#     Men olma yaxshi ko'raman 
    
#     Men       olma      yaxshi ko'raman

# Matnlar bilan ishlaydigan metodlar ko'p. Ularning ba'zilari bilan
#  kelajakda yana tanishamiz, to'liq ro'yhatni esa quyidagi sahifada 
#  ko'rishingiz mumkin.

# Metodlar o'zgaruvchi ichidagi asl matnni o'zgartirmaydi!

#         INPUT —FOYDALANUVCHI BILAN MULOQOT: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#input-foydalanuvchi-bilan-muloqot
# Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida 
# berayotgan edik. Keling endi qiymatni o'zimiz emas, balki dastur 
# foydalanuvchilariga kiritish imkonini beramiz. 

# Buning uchun input() funktsyasidan foydalanamiz. 
    
#     ism = input("Ismingiz nima?")
#     print("Assalom alaykum, " + ism)
# Yuqoridagi dastur, avval 1-qatorda foydalanuvchining ismini so'raydi.
#  Foydalanuvchi ismini kiritib, Enter tugmasini bosgach, foydalanuvchi
#  kiritgan matnism degan o'zgaruvchiga yuklanadi va dasturining 2-qatori bajaradi:

# Natija:
    
#     Ismingiz nima?anvar
    
#     Assalom alaykum, anvar

# Keling yuqoridagi kod va uning natijasini chiroyliroq ko'rinishga keltiramiz.
    
#     ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
#     print("Assalom alaykum, " + ism.title())

#         AMALIYOT: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string#amaliyot
# Quyidagi mashqlarni bajaring:

#     Quyidagi o'zgaruvchilarni yarating: 

#     kocha="Bog'bon"

#     mahalla="Sog'bon"

#     tuman="Bodomzor" 

#     viloyat="Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:

#     Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini 
# foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan 
# keyin yangi qatordan yozing

# Yuqoridagi matnni f-string yordamida, yangi, manzil deb 
# nomlangan o'zgaruvchiga yuklang

# manzilga biz yuqorida o'rgangan title(), upper(), lower() ,
#  capitalize() metodlarini qo'llab ko'ring.

# !!!AMALIYOT JAVOBLARINI AMALIYOTNI BAJARGACH UNI TEKSHIRIW UCHUNGINQA OCHING!!!
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")   

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      tuman + " tumani,\n" + viloyat + " viloyati")

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())