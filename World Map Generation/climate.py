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

def createrivers(coords,IMAGE):
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    for i in coords.items():
        riverlist = []
        print(i)
        if ["mountain", "true"] in i[1]:
            print("approoved")
            ValidCoordsRivers= i[1].copy()
            ValidCoordsRivers.pop()
            print(ValidCoordsRivers)
            print(i[1])
            point = random.choice(ValidCoordsRivers)
            print(point)
            riverlist.append(point)
            for i in range(2):
                print("...")

                newitem = ((riverlist[-1][0] + random.randint(30,40),riverlist[-1][1] + random.randint(30,40)))
                print(newitem)
                if is_on_land(img, newitem[0], newitem[1]) == True and newitem[0] and newitem[1] < 200 :
                    riverlist.append(newitem)
            riverlist = [tuple(pt) for pt in riverlist]

            draw.line(riverlist, fill=Blue, width=3)
    print(f"riverlist: {riverlist}")
    img.save('rivers.png')

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


createwind(r"my_blob.png")



createrivers(coords, r"finalmountains.png")

windpoint = ("point2", windmappoints["point2"])
print(f"windpoint {windpoint}")
climategen(windmappoints, windpoint, riverdata, coords)


