
import sys
sys.path.append(r"C:\Users\adena\OneDrive\Desktop\Stellar World Creator\World Map Generation")
import Intialscreator 
import xml.etree.ElementTree as ET

cultutrename = input("what do you want to parse?")
tree = ET.parse(rf'C:\Users\adena\OneDrive\Desktop\Stellar World Creator\Culture Creation\{cultutrename}.xml')
path = rf'C:\Users\adena\OneDrive\Desktop\Stellar World Creator\Culture Creation\{cultutrename}.xml'

def sedornom(precipitation,rivers,coords,startingpoint,animalsinarea):
    #it feels like i have to use 1,000,000,000 arguments for everything!


    nearbyariver = False
    nearbyamountain = False

    #sedentary or nomadic?
    for point in (p for river in rivers for p in river):
        if abs(point[0] - startingpoint[0]) <= 20:
                #if the number turned positive is less than twenty units away:
                nearbyariver = True
                break

        
    for key in coords:
        print(key)
        coords[key].pop()
    #removes the mountain tags.

    for point in coords[key]:
        print(point)
        if abs(point[0] - startingpoint[0]) <= 40:
            # if the number turned positive is less than twenty units away:
            nearbyamountain = True
            break


    if nearbyamountain and nearbyariver == True:
        lifestyle = "sedentary"
    else:
        lifestyle = "nomadic"
    
    #it couldnt have been THAT easy. 
    #So lets try to decide if they could handle large cities in their current condition.
    #for example
    if precipitation[0] > 20 and precipitation[0] < 100 and lifestyle == "sedentary":
        largecities = True
    else:
         largecities = False
    print(lifestyle, largecities)

    #lets check if they could be good at animal husbandry.

    if largecities == True:
        animalhusbandry = True
        pass
    else:
        if precipitation[0] > 15 and "cows" in animalsinarea :
            animalhusbandry = True
        else:
            animalhusbandry = False
    print(animalhusbandry)
    #loading our tags
    lifestyletag = tree.find('lifestyle')
    pastorialists  = tree.find("pastorialists")
    cities  = tree.find("cities")
    #changing our tags
    lifestyletag.text = f"{lifestyle}"
    pastorialists.text = f"{animalhusbandry}"
    cities.text = f"{largecities}"
    #writing it all
    tree.write(path)
    #This was so easy. all i had to do was check some precipitation and mountain coords.


    


    

precipitation = Intialscreator.loadata(r"precpitaion.json")
rivers = Intialscreator.loadata(r"riverdata.json")
coords = Intialscreator.loadata(r"Stellar World Creator\output.json")
     
sedornom(precipitation,rivers,coords,(86, 38),["cows"])
