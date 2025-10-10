import sys
import copy
sys.path.append(r"Stellar\World Map Generation")
import Intialscreator
import xml.etree.ElementTree as ET
import climatecoords
import random
cultutrename = input("what do you want to parse?")
tree = ET.parse(rf'Stellar\culture\{cultutrename}lifestyle.xml')
path = rf'Stellar\culture\{cultutrename}lifestyle.xml'
#i realized that instead of keeping everything in one file,
#i would just keep 3 files per culture. This is because im lazy and i dont want to have
#to convert lists to xml, so ill just keep lists as json files since i can easily do that.

veglists = r'plants.xml'
vegtree = ET.parse(veglists)
vegpath = copy.deepcopy(veglists)



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

    #lets check if they're good at animal husbandry.

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


def makefoodstats(preciptiation,veg):
    print(preciptiation)
    #find cooking methods
    precipavrage = ((preciptiation[0] + preciptiation[1]) / 2)
    print(precipavrage)
    if precipavrage < 15:
       cookingmethods = ["smoking","baking"]
    elif 15 <= precipavrage <= 23:  # include 23
        cookingmethods = ["smoking", "boiling"]
    else:  # everything above 23
       cookingmethods = ["stove baking","boiling"]
    print(cookingmethods)
    staplecrops = []
    vegtreelevel = 0
    for i in veg:
        vegitem = vegtree.find(f".//{i}")
        #was unsure about this command at first, worked the way i heard it would.
        #my only grevience at first was that it showed the location of it in memory,
        #but i managed to get around that by only printing the
        print(vegitem.tag)
        vegtreelevel = int(vegitem.text)
        print(vegtreelevel)
        if vegtreelevel >= 40 and cookingmethods[0] == "smoking":
           staplecrops.append(i)
           print("success")
        elif vegtreelevel >= 40 and vegtreelevel <= 70 and cookingmethods[1] == "boiling":
             staplecrops.append(i)
             print("success")
        else:
           print("none")
    
    print(staplecrops)
    datatosave = [staplecrops,cookingmethods]
    Intialscreator.savedata(datatosave,r"foodstats.json")


    

precipitation = climatecoords.load_json(r"precpitaion.json")
rivers = climatecoords.load_json(r"riverdata.json")
coords = climatecoords.load_json(r"output.json")
veg = climatecoords.load_json(r"veg.json")
#i forgot to test this so i thought there was a function in intialscreator called
#load data, but there wasnt. So i used the load json onw in clmiate coords 
print(veg)
makefoodstats(precipitation,veg)
sedornom(precipitation,rivers,coords,(100, 66),["cows"])


def namegen():
    constanats = ['p','t','k','b','d','f','g','zj','th']
    vowels = ['a','e','i','o','u','ae']
    constantstructures = ['cv','cvc','vc']
    structure = random.choice(constantstructures)
    #we will set up three things, our counstanats, our vowels, and our structures.
    #we'll then set up a length for how many of these structures are in the word:
    wordlength = random.randint(1,3)
    word = []
    for i in range(wordlength):
        for i in structure:
            print(i)
            if i == 'c':
                word.append(random.choice(constanats))
            elif i == 'v':
                word.append(random.choice(vowels))
    word = ''.join(word)
    print(word)

namegen()
