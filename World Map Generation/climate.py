import json
import random
import PIL
import Intialscreator
from Intialscreator import is_on_land
from PIL import Image, ImageDraw, ImageFont
Red= (201, 26, 26)
Blue= (50, 147, 168)
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
                addtooriverlist = []
                for item in range(6):
                    print()
                    print("...")

                    newitem = ((riverlist[itempoint][-1][0] + random.randint(30,40),riverlist[itempoint][-1][1] + random.randint(30,40)+ 4))
                    print(newitem)
                    if newitem[0]  < width - 1  and  newitem[1] < height - 1:
                        if is_on_land(img, newitem[0], newitem[1]) == True:
                            addtooriverlist.append(tuple(newitem))
                if addtooriverlist:  # only add if non-empty
                    riverlist[itempoint].extend(addtooriverlist)
                    print(f"river lisyt{riverlist}")
                
            for i in riverlist:
                i = [tuple(pt) for pt in i]
                print(f"testing: {i}")
                draw.line(i, fill=Blue, width=3)
    
            
            # riverlist = [tuple(pt) for pt in riverlist]
            #  #checks if each item in riverlist is a tuple
            # draw.line(riverlist, fill=Blue, width=3)
            # riverdata[i[0]] = riverlist



    print(f"riverlist: {riverdata}")
    img.save('rivers.png')
    img.show()


def climategen(windmappoints, windpoint, riverdata=".", coords="."):
    print(".")
    print(windmappoints)
    print(windpoint)

    windirection = windpoint[1][1]
    print(f"windirection: {windirection}")
    print(f"{windpoint[0]}")
    keys = list(windmappoints.keys())
    print(keys)
    print(windpoint[0])
    if windpoint[0] == "point2":
        currentindex = 2
        final = True
        print(currentindex - 1)
        lastpoint = windmappoints[keys[currentindex - 1]]
        print(lastpoint)
        print(f"last {lastpoint}")

    else:
        currentindex = keys.index(windpoint[0])
        lastpoint = windmappoints[keys[currentindex + 1]]
        final = False
    
    if windpoint[1][1] != lastpoint[1]:
        climatewinddirection = (f"{windpoint[1][1]}{lastpoint[1]}")
    else:
        climatewinddirection = ({windpoint[1][1]})
    print(climatewinddirection)
    climatetempratures = []
    climatetempratures.append(list(windpoint[1][2][0]))
    climatetempratures.append(list(lastpoint[2][0]))
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
            #takes our rounded centre and adds it by a 10th of half the elevation
            part1preciptation = roundedcentre / 10 + (i[1][1][0] - roundedcentre / 2) / 10
        else:
            part1preciptation = roundedcentre / 10 +30
    
    print(part1preciptation)
    print(riverlist)
    finalx = 0
    finaly = 0
    for i in  riverlist:
        print(f"RIVER {i}")
        finalx = sum(pt[0] for pt in i) / len(i)
        finaly = sum(pt[1] for pt in i) / len(i)
    divisorriver = (finalx,finaly)
    if divisorriver[0] > roundedcentre and divisorriver[0] < divisorriver[0] + 30:
        part2preciptation = (divisorriver[0] - roundedcentre) / 5
    else:
        part2preciptation = 10
        print(part1preciptation + part2preciptation)
        preciptitation = ((( (part1preciptation + part2preciptation) / 2) / 3 * 2) + 10, ((part1preciptation + part2preciptation) / 2) / 3 + 10)
    print(f"inches of rainfall each year: {preciptitation}")



createrivers(coords, r"finalmountains.png")
preciptationgen((123,123),coords,riverlist)

# createwind(r"my_blob.png")



# windpoint = ("point2", windmappoints["point2"])
# print(f"windpoint {windpoint}")
# climategen(windmappoints, windpoint, riverdata, coords)
