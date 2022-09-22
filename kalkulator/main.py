import time
#from time import sleep
#import time as t

a = 54
b = 82
a + b

print("Sestevek je "+str(a+b))

"""
in tudi to je lahko komentar
"""
if a>b:
    print("a je vecji od b")#<= == is is not in
    #to je komentar
elif a<b:
    print("b je vecji od a")
else:
    print("noben pogoj ni izpoljnen")

while True:
    a += 1
    print("a je :" + str(a))
    #time.sleep(0.1)
    if a > b:
        break

vhod = input("Vnesi najljubso st.:")
print("vasa st. je: " + str(vhod))