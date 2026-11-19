# 19.11.26 Andra Ring


# Ringi pindala ja Turtle
#Kirjuta programm, mis kasutab Turtle graafikat joonistamaks ringi ning arvutab ja kuvab konsoolis
import turtle
try:
    r = int(input("Sisesta raadius: "))
    s = 3.14*r**2
    p = 2*3.14*r
    turtle.circle(r)
    turtle.done()

except valueError:
    print("urrrr")
























#Faili allalaadimine
#Kirjuta programm, mis aitab arvutada, kui kaua kulub aega faili allalaadimiseks.
try:
    kiirus = int(input("sisesta kiirus MB/S: "))
    suurus = int(input("sisesta kiirus MB: "))
    vastus = suurus / kiirus
    if kiirus ==0:
        print("nulliga ei saa jagada!")
    else:
        vastus = suurus / kiirus
    
    print(int(vastus))
except valueError:
    print("mingi jama")



# aia pikkus
# Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
x = int(input("sisesta külg 1: "))
y = int(input("sisesta külg 2: "))
pikkus = (x+y)*2                                                                                                                                                                                                      
print(F"Aia kogupikkus on {pikkus} meetrit")
      





