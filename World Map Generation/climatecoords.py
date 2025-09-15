
import random
import Intialscreator 
import PIL
from PIL import Image, ImageDraw, ImageFont
import climate
import json
import os
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"{filename} loaded.")
    return data

coords = load_json("output.json")
riverlist = load_json("riverdata.json")
windmap = load_json("windmap.json")
# sadly, this is the best i could think of.
# If you have a better idea please tell me.
# this could theoreticlay could take like, 2000 years to run, but most of the time, it will take 1 second.
def generatecent(blolb):
    
    while True:
        centcoords = (random.randint(0, 199), random.randint(0, 199))
        print(centcoords)
        if Intialscreator.is_on_land(blolb, centcoords[0], centcoords[1]):
            print("land!")
            return centcoords
            break
        else:
            print("...")
        
# generatecent('my_blob.png')



def checkwindzone(coord):
    print("checking")
    for i in windmap.keys():
        print(f"Processing windmap key: {i}")
        if coord[1] - 10 < windmap[i][0]:
            print(f"windzone is {i}")
            windzone = i
            break
        else:
            windzone = 'point2'
    return windzone

#now to finally put all our functions in climate.py to good use.
centers = []
#better to wrap this in a function
def nomralizecoords(protocoords,blob,center):
    finalcoords = []
    finalcoords.append((center[0]+10,center[1]))
    finalcoords.append((center[0]+20,center[1]+10))
    for i in protocoords:
        newcoord = []
        for item in range(len(i)):
            coordpos = i[item]
            if i[item] < 0:
                coordpos = (10)
            if i[item] > 200:
                coordpos = 190
            newcoord.append(coordpos)
        newcoord = tuple(newcoord)
        if Intialscreator.is_on_land(blob, newcoord[0], newcoord[1]):
            finalcoords.append(newcoord)
    return finalcoords

def genclimatezone(length,blob,savefolderpath):
    
    coords = load_json("output.json")
    img = Image.open(blob)
    for item in range(length):
        generatecent(img)
        center = generatecent(img)
        centers.append(center)
    print(centers)
    for i in centers:
        name = input("what would you like to name this one?")
        os.mkdir(rf"{savefolderpath}\{name}")

        precipclimate = climate.preciptationgen(i,coords,riverlist)
        Intialscreator.savedata(precipclimate,rf"{savefolderpath}\{name}\precpitaion.json")
        veggies = climate.calctreesveg(precipclimate[0]+precipclimate[1])
        Intialscreator.savedata(veggies,rf"{savefolderpath}\{name}\veg.json")

        windzone = checkwindzone(i)
        print(windzone)
        windpoint = (windzone, windmap[windzone])
        climateitems = climate.climategen(windmap, windpoint, riverlist, coords)
        Intialscreator.savedata(climateitems,rf"{savefolderpath}\{name}\climates.json")

        direction = climateitems[0]
        temp = climateitems[1]
        protocoords = [
        (i[0] + 60, i[1] + 30), 
        (i[0] - 30, i[1] + 60),
        (i[0] + 60, i[1] - 30),
        (i[0] - 30, i[1] - 60),
        ]
        finalcoords = nomralizecoords(protocoords,img,i)
        Intialscreator.savedata(finalcoords,rf"{savefolderpath}\{name}\coords.json")

        
        print(protocoords)
        print(finalcoords)

        t = 1 - ((precipclimate[0] + precipclimate[1] / 2) / 120)
        #divides our  precipitation average by our max, which is 120.
        #  we subtract this from one in order to get a value between 1 and 0.
        #the reason we're inverting this is that if t was 1, we'd be doing the math to get from a tan to pure green.
        #so leaving it like that will cause it to disregard this,actually making divide CLOSER to zero,
        #creating inaccurate data. basically, deserts would look like forests and forests would like deserts.
        r = int(210 * t)
        #we scale each
        g = int(255 + (180 - 255) * t)
        b = int((140 - 0) * t)
        draw = ImageDraw.Draw(img)
        colorgrad = (r,g,b)
        draw.polygon(finalcoords, fill=colorgrad)
    
    img.save('worldmap.png')
    img.show()




        
        

        


        #tommorow, well add support for the climategen function in climate.py. well also make a function
        #called "check windzone" that will set our windzone for drawing. then we will draw our zone and save the data as a folder of json files+.


# checkwindzone((41,20))
genclimatezone(15,'my_blob.png',r'\Stellar\climates',)
