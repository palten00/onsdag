import random #importerar funktionen random
meny = 0 # ger meny ett värde


while meny != 2: # så länge meny inte är 2 så loopas den
    print("tryck på 1 för att slå tärningen") # skriver ut i konsolen
    print("tryck på 2 för att avsluta") #skriver ut i konsolen
    
    try:
        meny = int(input("välj en siffra för att fortsätta "))
        
    except:
        print("du måste välja 1 eller 2")
    if meny == 1:
        print(random.randint(1,6))
    
