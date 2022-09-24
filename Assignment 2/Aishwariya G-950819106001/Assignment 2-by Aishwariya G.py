from numpy import random
a=random.randint(100)
b=random.randint(100)
print("Temperture in celsius =")
print(a)
print("Humidity in percent =")
print(b)
if(a>35):
    if(b>45):
        print("DANGER!!!!")
        print("ALERT Detected for both the temperature and humidity")
    else:
        print("ALERT Detected only for temperature")
elif(a==30):
    print("Temperature reaches the threshold")
else:
    print("SAFE! All are normal")
