import time

print "Dobrodosli v kalkulatorju! Nalagam:",
i = 10
while True:
    print ".",
    i -= 1
    time.sleep(0.1)
    if i < 1:
        break
while True:
print("\nOpcije:")
print("1) +")¸
print("2) -")
ukaz = input("Vnesi st. ukaza: ")
a = input("vnsei stevilo a: ")
b = input("vnesi stevilo b: ")
if ukaz == 1:
    #sestevanje
    print("rezultat je: " + str(a + b))
elif ukaz == 2:
    #odstevanje 
    print("rezultat je: " + str(a -b))
else:
    print("Neveljaven ukaz!")