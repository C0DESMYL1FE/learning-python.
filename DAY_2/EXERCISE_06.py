# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:35:20 2021

@author: JAMSHID bek
"""

#06 SONLAR. BATAFSIL: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar
Pythonda sonlar bilan ishlashni o'rganamiz
Dasturlash davomida turli sonlar bilan ishlash tabiiy hol. 
Pythonda sonlarning bir necha turlari bor. Keling ular bilan yaqindan tanishaylik.


        INTEGERS — BUTUN SONLAR: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#integers-butun-sonlar
Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (+),
 ayirish (-), ko'paytirish(*), bo'lish (/) kabi arifmetik amalarni 
 bajarish mumkin:

     a = 20  # Sonlar musbat yoko
     b = -30 # manfiy bo'lishi mumkin
    c = a + b
    print(c)
    Natija: -10

Python - operatorlar orasidagi bo'shliqlarni inobatga olmaydi. O'qishga 
qulay bo'lishi uchun yuqoridagi kabi (bo'shliqlar bilan) yozishingiz mumkin.

    # Kvadratning yuzini hisoblaymiz
    kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
    kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
    print(kvdrt_yuzi)
    Natija: 400

        FLOATS — O'NLIK SONLAR: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#floats-onlik-sonlar
Pythonda o'nlik sonlar floating point numbers yoki qisqa qilib floats
 deyiladi. "Floating point numbers" atamasini o'zbek tiliga "suzuvchi nuqtali 
 sonlar" deb tarjima qilish mumkin. Ingliz tilida o'nlik sonlarni yozishda 
 vergul (,) emas nuqta (.) belgisi ishlatiladi, va bu nuqta sonning katta 
 kichikligiga qarab joyi o'zgargani uchun "floating" (suzuvchi) deyiladi.

    pi = 3.14159 # o'nlik son (float)
    radius = 10  # butun son (integer)
    diametr = 2*radius
    print("Aylana uzunligi ", pi*diametr, " ga teng.")
    Natija: Aylana uzunligi 4.712384999999999 ga teng.

        BUTUN SONDAN O'NLIK SONGA: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#butun-sondan-onlik-songa
Avval aytganimizdek ikki butun sonni bo'lish (/) natijasida o'nlik son 
hosil bo'ladi (natija butun bo'lsa ham). 

    a = -20
    b = 40
    c = b/a
    print(c) # natija o'nlik son bo'ladi
    Natija: -2.0

Shuningdek butun va o'nlik sonlar o'rtasidagi har qanday arifmetik
 amallarning natijasi ham o'nlik son bo'ladi.

    a = 2
    b = 3.0
    # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
    print(a+b) 
    print(a*b)
    print(a**b)
    print(2*(a+b))
Natijalar:

    2.0
        
    5.0
    
    6.0
    
    8.0
    
    10.0

        UZUN SONLARNI KIRITISH: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#uzun-sonlarni-kiritish
Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq 
(_) yordamida guruhlash mumkin. Python - son tarkibidagi pastki 
chiziqlarni (_) inobatga olmasdan, uzun sonligicha qabul qiladi.

    aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
    print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")
    Natija: Yer kurrasida 7594000000 ga yaqin odam yashaydi

        KONSTANTA: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#konstanta
Aksar dasturlash tillarida konstant qiymatlar tushunchasi bor. 
Konstantlar o'zgarmas bo'ladi (misol uchun\piπ ning qiymati konstant,
o'zgarmas qiymat). Pythonda konstant tushunchasi yo'q, shuning uchun 
dasturchilar bunday o'zgaruvchilarning nomini katta harflar bilan 
yozadilar (ogohlantirish sifatida). Bu albatta qat'iy qonun emas, 
lekin kelajakda o'zgaruvchilar orasida konstant qiymatlarni ajratish 
uchun yaxshi usul.

PI = 3.14159
raduis = 21.2
        BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#bir-nechta-ozgaruvchiga-qiymat-berish
Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar 
va ularga mos qiymatlar vergul (,) bilan ajratiladi:

x, y, z = 10, -7.25, -30
Yuqoridagi kod x ga 10, y ga -7.25, va z ga -30 qiymatini yuklaydi.

        O'ZGARUVCHI TURINI ALMASHTIRISH: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#ozgaruvchi-turini-almashtirish
Keling quyidagi misolni ko'raylik, maqsadimiz ism va yosh degan ikki 
o'zgaruvchini yangi xabar degan o'zgaruvchiga yuklab, "Jobir 16 yoshda"
 degan matnni konsolga chiqarish:

     ism = 'Jobir'
    yosh = 36
    xabar = ism + ' ' + yosh + ' yoshda'
    print(xabar)
    Natija: TypeError: can only concatenate str (not "int") to str

Afsuski, kutilgan natija o'rniga xatolik chiqdi. Agar xatoni ingliz 
tilidan tarjima qilsak, matn (str) va son (int) ni jamlab bo'lmaydi 
degan ma'no chiqadi. 

Demak Pythonda matn (string) va son (int, float) turidagi o'zgaruvchilarni
 jamlab bo'lmas ekan. Xo'sh, bunga yechim bormi? Albatta. 

Pythonda bir turdagi o'zgaruvchini boshqa turga o'tkazish mumkin, bu 
ingliz tilida typecasting detiladi. Buning uchun Pythonda mahsus funktsiyalar
 bor, keling ular bilan tanishamiz:

str()— int yoki float turidagi sonlarni matnga o'zgartiradi.

int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi.
 Bunda matn butun son ko'rinishida bo'lishi kerak.

float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.

Demak, yuqoridagi kod to'g'ri ishlashi uchun 3-qatorni quyidagicha o'zgartiramiz:

    ism = 'Jobir'
    yosh = 36
    xabar = ism + ' ' + str(yosh) + ' yoshda'
    print(xabar)
    Natija: Jobir 36 yoshda

!!! str(yosh) kodi yosh degan o'zgaruvchining qiymatini matn ko'rinishida 
ko'rsatdi xolos. Asl o'zgaruvchining qiymati sonligicha qoladi. int() va
 float()ham huddi shunday ishlaydi.

        O'ZGARUVCHI TURINI TEKSHIRISH: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#ozgaruvchi-turini-tekshirish
Kodimizda o'zgaruvchilar ko'payib ketdi. Yuqoridagi kabi xatolar 
qilmaslik uchun ba'zida o'zgaruvchinig turini tekshrish talab qilinadi.
 Buning uchun type() funktsiyasidan foydalanamiz:

     ism = 'Jobir'
    yosh = 36
    print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
    print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz
    Natija: 

    <class 'str'>

    <class 'int'>

Kurib turganingizdek, ism nomli o'zgaruvchi'str' ya'ni matn, yosh esa 
'int' son turida ekan.

        INPUT() VA SONLAR: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#input-va-sonlar
Avvalgi darsimizda foydalanuvchidan ma'lumot olish uchun input() 
funktsyasidan foydalanishni o'rgandik. Kelin endi shu funktsiya yordamida 
foydalanuvchidan son olishni ko'raylik. Quyidagi kod foydalanuvchining
 tug'ilgan yilini so'raydi va uning yoshini hisoblab beradi:

     #1 foydalanuvchining tug'ilgan yilini so'raymiz
    t_yil = input("Tug'ilgan yilingizni kiriting: ")
    #2 foydalanuvchi yoshini xisoblaymiz
    yosh = 2020 - t_yil # 
    #3 foydalanuvchi yoshini konsolga chiqaramiz
    print("Siz " + yosh + " yoshda ekansiz")

    Natija: TypeError: unsupported operand type(s) for -: 'int' and 'str'

Kutilgan natija o'rniga xatolik. Lekin xato qayerda? Dastur tug'ilgan 
yilimni so'radi, men 1983 deb kiritdim va shu zaxoti xato ro'y berdi
 va dastur to'xtadi. Xatoni tarjima qilsak son (int) va matn (str) 
 o'rtasida ayirish (-) amalini bajarib bo'maydi deyapti.

Gap shundaki, input() funktsiyasi har qanday kiritilgan qiymatni matn 
(string) ko'rinishida qabul qiladi (garchi biz son kiritgan bo'lsak ham). 
    Keling, konsolda t_yil degan o'zgaruvchining turini tekshirib ko'ramiz.


Ko'rib turganingizdek t_yil o'zgaruvchisi saqlayotgan qiymat str ya'ni
 matn ekan. Kodimizning 2 va 6-qatorlarini o'zgartiramiz:

     #1 foydalanuvchining tug'ilgan yilini so'raymiz va qiymatni int ga aylantiramiz
    t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
    #2 foydalanuvchi yoshini xisoblaymiz
    yosh = 2020 - t_yil # 
    #3 foydalanuvchi yoshini konsolga chiqaramiz
    print("Siz " + str(yosh) + " yoshda ekansiz")
Natija: 

    Tug'ilgan yilingizni kiriting: 1983 

    Siz 37 yoshda ekansiz

Yuqoridagi kodning 2-qatoriga e'tibor bersangiz, biz ikki funktsiyani
 bir biriga joylab yozdik (int(input()). Aslida, ajratib ham yozishimiz 
mumkin edi:

    #1.1 foydalanuvchining tug'ilgan yilini so'raymiz
    t_yil = input("Tug'ilgan yilingizni kiriting: ")
    #1.2 t_yil o'zgaruvchini int ga aylantiramiz
    t_yil = int(t_yil)
    #2 foydalanuvchi yoshini xisoblaymiz
    yosh = 2020 - t_yil # 
    #3 foydalanuvchi yoshini konsolga chiqaramiz
    print("Siz " + str(yosh) + " yoshda ekansiz")
        AMALIYOT: https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar#amaliyot
    Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:

    Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur


    Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga 
    chiqaruvchi dastur


    Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi,
     ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur


# !!!AMALIYOT JAVOBLARINI AMALIYOTNI BAJARGACH UNI TEKSHIRIW UCHUNGINQA OCHING!!!

#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
x = int(input("Istalgan son kiriting:\n>>>"))
print(x, " ning kvadrati ", x**2, " ga teng")
print(x, " ning kubi ", x**3, " ga teng")

# Foydalanuvchining yoshini so'rang, 
# va uning tug'ilgan yilini hisoblab, konsolga chiqaring.
yosh = int(input("Yoshingiz nechida? \n>>>"))
t_yil = 2020-yosh
print("Siz ", t_yil, " da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritshni so'rab, 
# kiritilgan sonlarning yig'indisi, ayirmasi, 
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)