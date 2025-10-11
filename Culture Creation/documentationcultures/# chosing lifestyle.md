# chosing lifestyle


## setting up path and imports

```
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
```
we import sys so we can append our path to the world generation folder, so later we can import climatecords and initalscreator.
We also import copy for later. We import xml.etree.ElementTree as Et in order
to parse xml, which is needed to edit the lifestyle file.
we import climatecoords for the load json function and random for the random functions. we ask the user for the xml file to parse before we set the path of that as tree and path.     We then set a path for veglists and set vegtree and vegpath using a deep copy function

## setting up a function

```
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
```
first, we set up a function with these arguments
| argument| datatype | purpouse|
|----------|:---------:|---------:|
| precipitation| list|pecipitation of a area, mac and min values|
| rivers |list | list of lists for coords of diffrent rivers.|
| coords| tuple|coords of mountains|
| animals| list|list of animals|





we set both nearbyariver and nearbyamountain to false, for each river point  if it's absolute value  of the point's x - startingpoint x is less than or equal to t  20, we set nearby a river to true, and we stop the loop.

```
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
```
for key in coords, we remove the last item of the list attached to that key, which is the tag. for each point in coord's key, we print our point and if the point's x - startingpoint's x are less or equal to 40, we set nearby a mountain to true and end it.
```
    if nearbyamountain and nearbyariver == True:
        lifestyle = "sedentary"
    else:
        lifestyle = "nomadic"
       ``
```       
if we are nearby a mountain AND nearbya river, we set our lifestyle to sedentary. else, its nomadic.

## the rest

```
    if precipitation[0] > 20 and precipitation[0] < 100 and lifestyle == "sedentary":
        largecities = True
    else:
         largecities = False
    print(lifestyle, largecities)

 
```
if our preciptiation's x is greater than 20, and it's less than hundred, and we are sedentary, we set largecities to True. else, we set it to false. We print our lifestyle and if we have large cities.

```
    if largecities == True:
        animalhusbandry = True
        pass
    else:
        if precipitation[0] > 15 and "cows" in animalsinarea :
            animalhusbandry = True
        else:
            animalhusbandry = False
    print(animalhusbandry)
  ```
    if we do have large cities, we set animalhusbandry to true and we dont check anything else.
   if we dont, if our preciptitation is greater than 15 and cows is in animalsinarea, we set it to True, else, we set it to False.
   We print whenever we have animal husbandry, and finish.
  
  ```
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
    ```
    we then try to find the root tag, which is the lifestyle tag, and we try to find the pastorialists tag and set pastorialsts to it. we also do the same with cities.
    we set our text to the lifestyle, our pastorialsts text to animalhusbandry, and cities text to largecities. we write it all to the tree, and we are finished.

    

