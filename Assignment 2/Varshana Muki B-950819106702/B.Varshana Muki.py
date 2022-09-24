from numpy import random
a=random.randint(100)
b=random.randint(100)
print("Temperature=")
print(a)
print("Humidity")
print(b)
if(a>30):
    if(b>50):
        print("DANGER")
        print("ALERT detected for both temperature")
    else:
         print("ALERT detected for only temperature")
elif(a==30):
      print("Temperature reaches the threshold")
else:
    print("All are normal")
    
        

        
