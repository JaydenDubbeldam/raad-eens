import random
import webbrowser
score = 0

for raden in range(0, 20):
    
    getal = random.randint(1,1000)
    
    for vraag in range(0, 10):
        print()
        invoer = int(input("Gok een getal tussen de 1 en de 1000? "))
        
        if invoer > getal:
            print("Lager!")
        elif invoer < getal:
            print("Hoger!")
        if invoer == getal:
            print("Geraden!")
            score = score + 1
            break
        elif invoer > getal - 20 and invoer < getal + 20:
            print("Je poten staan in de fik! Bel de brandweer!")
        elif invoer > getal - 50 and invoer < getal + 50:
            print("De thermostaat slaat op hol, want je bent warm!")
        
        print(getal)

    print()      
    print("Het getal was", getal)
    print("Je hebt momenteel", score, "punt(en) gescoord!")
    print()
    invoer2 = input("Wil je nog een getal raden? Ja of Nee! ").lower()
    if invoer2 == "nee" and raden < 19:
        print("Eindscore:", score, "punt(en)")
        break
    
    rick = ()
    if raden == 19:
        print("Je bent aan het einde gekomen van je gratis proefversie koop een account op onze site voor oneindig games!")
        while rick != "ja":
            rick = input("Wil je naar onze site? ").lower()
            if rick == "ja":
                webbrowser.open('https://www.youtube.com/watch?v=iik25wqIuFo')
            