import json
import random
import PIL
import Intialscreator
from Intialscreator import is_on_land
from PIL import Image, ImageDraw, ImageFont
import xml.etree.ElementTree as ET
# i was bored, so i felt like commenting this code.
#redefine these colours again, since we dont need to import them.
Red= (201, 26, 26)
Blue= (50, 147, 168)

#opens up our tree
tree = ET.parse(r'C:\Users\adena\OneDrive\Desktop\Stellar World Creator\World Map Generation\plants.xml')

with open("output.json", 'r', encoding='utf-8') as f:
    json1 = f.read()  # read file content as a string
print(json1)
coords = json.loads(json1)  
print(coords)

windmappoints = {"point1" : [],
                 "inbetween" : [],
                 "point2": []
}

directions = ["east", "west", "north", "south"]
def createwind(IMAGE):
    global windmappoints
    windmappoints = {"point1": [], "inbetween": [], "point2": []}
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    cx = width // 2
    cy = height // 2
    
    windmappoints["point1"].append(random.randint(1,cy))
    windmappoints["point1"].append(random.choice(directions))
    winter1 = (w := random.randint(1, 8), random.randint(w, 17))

    print(f"winter:{winter1}")
    windmappoints["point1"].append(((winter1),((winter1[0] * 9/5) + 32),((winter1[1] * 9/5) + 32))) # (1, 2)
    
    print(windmappoints)

    #I usally do RUP: repeat until painfull. We only do this 3 times, so its fine I guess. But for a longer one, like that check for the mountain range coords, I decided that i shouldnt be doing
    #that in these cases.
    
    winter2 = (w := random.randint(35, 46), random.randint(w, 60))
    windmappoints["point2"].append(random.randint(windmappoints["point1"][0]+15,height - 1))
    windmappoints["point2"].append(random.choice(directions))
    windmappoints["point2"].append(((winter2),((winter2[0] * 9/5) + 32),((winter2[1] * 9/5) + 32))) # (1, 2)
    
    winter3 = (w := random.randint(17, 30), random.randint(w, 35))
    windmappoints["inbetween"].append((windmappoints["point2"][0]-windmappoints["point1"][0]))
    windmappoints["inbetween"].append(random.choice(directions))
    windmappoints["inbetween"].append(((winter3),((winter3[0] * 9/5) + 32),((winter3[1] * 9/5) + 32))) # (1, 2)


    print(windmappoints)

    linecoords = [((1,windmappoints["point1"][0]),(width - 1,windmappoints["point1"][0])),((1,windmappoints["point2"][0]),(width - 1,windmappoints["point2"][0])),]
    print(linecoords)
    draw.line(linecoords[0], fill=Red, width=3)
    draw.line(linecoords[1], fill=Red, width=3)
    font = ImageFont.load_default()
    draw.text((0, windmappoints["point1"][0]), str(windmappoints["point1"]), fill=Blue, font=font)
    draw.text((0, (windmappoints["point1"][0] + windmappoints["inbetween"][0] // 2)), str(windmappoints["inbetween"]), fill=Blue, font=font)
    draw.text((0, windmappoints["point2"][0]), str(windmappoints["point2"]), fill=Blue, font=font)
    

    img.save('windmap.png')
    img.show()
    #(::( Jerry recently picked up a job gaurding this show function. Its his first Summer Job! Wish Him Luck

riverdata = {
}
riverlist = []

#BUT I WILL CERTAINLY BE FIXING THIS! The old solution litteraly made the code run so long... so i think i should seperate the two for loops.
def createrivers(coords,IMAGE):
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    for i in coords.items():
        riverlist = []
        print(i)
        if ["mountain", "true"] in i[1]:
            print("approoved")
            
            ValidCoordsRivers= i[1].copy()
            ValidCoordsRivers.pop()
            print(f"...l...{ValidCoordsRivers}")
            print(i[1])
            for itempoint in range(3):
                point = random.choice(ValidCoordsRivers)
                print(point)
                riverlist.append([point])
                print(f"point:{point}")
            for item in range(len(riverlist)):
                addtooriverlist = []
                for i in range(5):
                   #again, you might be wondering why im putting a for loop in a for loop again. Remember, this is about SPEED, not readability.
                   # we are litteraly running one line of code in the first one, so it should be fine.
                   print("second part started....")
                   print(riverlist[item][-1][0])
                   newitem = ((riverlist[item][-1][0] + random.randint(30,40),riverlist[item][-1][1] + random.randint(30,40)+ 4))
                   print(newitem)
                   if newitem[0]  < width - 1  and  newitem[1] < height - 1:
                    if is_on_land(img, newitem[0], newitem[1]) == True:
                      addtooriverlist.append(tuple(newitem))
                   if addtooriverlist:  # only add if non-empty
                    riverlist[itempoint].extend(addtooriverlist)
                    print(f"river list{riverlist}")

            for i in riverlist:
                i = [tuple(pt) for pt in i]
                # print(f"testing: {i}")
                draw.line(i, fill=Blue, width=3)
    
            # old code from last time:
            # riverlist = [tuple(pt) for pt in riverlist]
            #  #checks if each item in riverlist is a tuple
            # draw.line(riverlist, fill=Blue, width=3)
            # riverdata[i[0]] = riverlist



    print(f"riverlist: {riverdata}")
    img.save('rivers.png')
    img.show()


def climategen(windmappoints, windpoint, riverdata=".", coords="."):
    print(".")
    print(f"windmap points {windmappoints}")
    print(f"windpoint : {windpoint}")
    # now it says what these values are: FINALY!
    windirection = windpoint[1][1]
    #sets up our wind direction as the second value
    print(f"windirection: {windirection}")
    print(f"{windpoint[0]}")
    keys = list(windmappoints.keys())
    #get the keys of WINDMAPPOINTS
    print(keys)
    print(windpoint[0])
    if windpoint[0] == "point2":
        #if windpoint is point2, we want to go backwards, since i dont want to have it calculate wind direction based on a windzone 2 zone's away.
        currentindex = 2
        #our current index is 2, since point2 is the 2nd index but 3rd item. I WILL NEVER, EVER UNDERSTAND WHY MOST PROGRAMMING LANGUAGES START AT 0. If someone is reading this, 
        #which i doubt, PLEASE explain this. I understand it, but it makes no sense why its like that.
        # i know that the 1rst item in a list 0, and the 2nd is 1, but WHY?
        final = True
        #let it know that we are on the final item,
        print(currentindex - 1)
        #print out cirrent item - 1.
        lastpoint = windmappoints[keys[currentindex - 1]]
        #our last point wil be the item before the current index. it should technacily be first point outside of this, but im too lazy to care :| 
        print(lastpoint)
        print(f"last {lastpoint}")

    else:
        currentindex = keys.index(windpoint[0])
        #if its not point two, we can just get the index of the current item and set last point to one, as well as final to false.
        lastpoint = windmappoints[keys[currentindex + 1]]
        final = False
    
    if windpoint[1][1] != lastpoint[1]:
        climatewinddirection = (f"{windpoint[1][1]}{lastpoint[1]}")
        # if windpoints second items second item is not the same as lasts points second item , we set them togter the reasono that  there's two [1]s is because its removed our key, thus getting straight into out list
    else:
        climatewinddirection = ({windpoint[1][1]})
        #if their the same, we just set it to one of them
    print(climatewinddirection)
    climatetempratures = []
    climatetempratures.append(list(windpoint[1][2][0]))
    climatetempratures.append(list(lastpoint[2][0]))
    print(climatetempratures    )
    #we append both, to the climate tempratures before geting the final temprature which is going to be our two climate temps added
    climatetempfinal = (climatetempratures[0][0] + climatetempratures[1][0]/2,climatetempratures[0][1] + climatetempratures[1][1] /2)
    print(climatetempratures)
    print(climatetempfinal)

def preciptationgen(centre,coords,riverlist):
    preciptitation = ()
    part1preciptation = 0
    print(".")
    roundedcentre = (centre[0] // 100) * 100
    print(roundedcentre)
    for i in coords.items():
        print(i[1][1][0])
        if i[1][1][0] > roundedcentre and i[1][1][0] < (roundedcentre + roundedcentre / 2):
            #takes our rounded centre and adds it by a 10th of half the elevation. 
            part1preciptation = roundedcentre / 10 + (i[1][1][0] - roundedcentre / 2) / 10
        else:
            part1preciptation = roundedcentre / 10 + 15.5
            #if i didnt add this here the climates would probaly be unlivable. Imagine living in a place with 0.01 - 0.2 rainfall. NOT FUN!
    
    print(part1preciptation)
    print(riverlist)
    finalx = 0
    finaly = 0
    for i in  riverlist:
        print(f"RIVER {i}")
        finalx = sum(pt[0] for pt in i) / len(i)
        finaly = sum(pt[1] for pt in i) / len(i)
        print("dizisor river")
    divisorriver = (finalx,finaly)
    print(divisorriver)
    if divisorriver[0] > roundedcentre and divisorriver[0] < divisorriver[0] + 30:
        #checks if its greater than the centre, but not too far away
        # if so, we use the river to decide how much rain we get
        part2preciptation = (divisorriver[0] - roundedcentre) / 5
        # we take the distance from the centre and divide it by 5
    else:
        part2preciptation = 20
        #if we arent nearby any rivers, we just give 20 inches.
        print(f"total precipitation {part1preciptation + part2preciptation}")
    totalprecp = (part1preciptation + part2preciptation)
        #we add these two together 
    preciptitation = ((( (part1preciptation + part2preciptation) / 2) / 3 * 2) + 10, ((part1preciptation + part2preciptation) / 2) / 3 + 15.5)
        # we then take half of this divided by 3, multipled by 2, and add 10. 
        #For the second value, we add the two values together and repeat the last process, but without the multipling by 2., and adding 10.
    print(f"inches of rainfall each year: {preciptitation}")


veglist = []
def calctreesveg(precipation):
    treelevel = precipation * 3
    print(f"treelevel: {treelevel}")
    for category in tree.getroot():
       print(f"{category.tag.capitalize()}:")
    # Loop through all items inside each category
       for plant in category:
           print(f"  {plant.tag}: {plant.text}")
           if int(plant.text) <= treelevel:
               veglist.append(plant.tag)
               print(f"added {plant.tag} to veglist") 
    print(f"veggies: {veglist}")

createwind(r"my_blob.png")

print(coords)
createrivers(coords, r"finalmountains.png")
preciptationgen((45,12),coords,riverlist)

# # createwind(r"my_blob.png")



windpoint = ("point2", windmappoints["point2"])
print(f"windpoint {windpoint}")
climategen(windmappoints, windpoint, riverdata, coords)

# totalprecp = 35.5  # You can adjust this value as needed

# calctreesveg(totalprecp)

# calctreesveg(totalprecp)
