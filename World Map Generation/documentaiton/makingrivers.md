# Creating Rivers:

## setting up our function
```
def createrivers(coords,IMAGE):
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    width, height = img.size


```
We set up 2 arguments. Coords and our image. We add our draw varible, and then grab our width and higth from the overall size.

## Setting Up The Inital Loop p1
```
    for i in coords.items():
        riverlist = []
        print(i)
        if ["mountain", "true"] in i[1]:
            print("approoved")
            
            ValidCoordsRivers= i[1].copy()
            ValidCoordsRivers.pop()
            print(f"...l...{ValidCoordsRivers}")
            print(i[1])
```
afterwards, we check each item in the coords: If these coords contain the ``["mountain", "true"]`` tag, then we print that we're using them.
we make a copy of the coords for THAT mountain, so that way we can edit them for later. We remove ``["mountain", "true"]`` tage before printing 
out coords two times, one with the tag and one without it.


## Setting Up The Inital Loop p2

```
            for itempoint in range(3):
                point = random.choice(ValidCoordsRivers)
                print(point)
                riverlist.append([point])
                print(f"point:{point}")
                addtooriverlist = []
```
We run this loop three times, creating 3 more lists.
```
            for item in range(len(riverlist)):
                addtooriverlist = []
                for i in range(5):
                   print("second part started....")

                   newitem = ((riverlist[item][-1][0] + random.randint(30,40),riverlist[item][-1][1] + random.randint(30,40)+ 4))
                   print(newitem)
                   if newitem[0]  < width - 1  and  newitem[1] < height - 1:
                    if is_on_land(img, newitem[0], newitem[1]) == True:
                      addtooriverlist.append(tuple(newitem))
                   if addtooriverlist:  # only add if non-empty
                    riverlist[itempoint].extend(addtooriverlist)
                    print(f"river list{riverlist}")

```

 For each item in the length of riverlist, we reset the ADDTOORIVERLIST list. We print our check before before setting our new item to the  list aligning with out current item in range's last items first number plus number in the range of 30,40, and then the our current ranges last items second number, creating a new tuple. if the first item of this tuple is less than the width of this image and the second item of this tuple is less than the height, we check if its on land. If so, we append our new item tuple to ADDTOORIVERLIST. if addtoriverlist isnt empty, we add addtooriverlist to riverlist, adn then print this out.
 ## drawing and adding
```
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

```

 we print our final river before  converting and 
drawing each point. we then print our data a gain and save our pictuere, as well as draw it.
