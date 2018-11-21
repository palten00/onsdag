import random 
meny = 0


while meny != 2:
    print("tryck på 1 för att slå tärningen")
    print("tryck på 2 för att avsluta")
    
    try:
        meny = int(input("välj en siffra för att fortsätta "))
        
    except:
        print("du måste välja 1 eller 2")
    if meny == 1:
        print(random.randint(1,6))
    
