# Generating Climate
## the begining
```
def climategen(windmappoints, windpoint, riverdata=".", coords="."):
    print(".")
    print(f"windmap points {windmappoints}")
    print(f"windpoint : {windpoint}")
    windirection = windpoint[1][1]
    #sets up our wind direction as the second value
    print(f"windirection: {windirection}")
    print(f"{windpoint[0]}")
    keys = list(windmappoints.keys())
    #get the keys of WINDMAPPOINTS
    print(keys)
    print(windpoint[0])
```
We define climate gen with 4 arguments. heres what each one of them does:

| argument | datatype | purpouse |
|---|---|---|
|windmappoints | dictonary | all the positoning on the windmap, as well as the climate tempratures and wind direction for each point|
| windpoint |  list | a point on the windmappoint dictonary you are using, storing data about that point. |
| riverdata | dictionary| *supposed* to contain data about river's. functionaly useless. but alas, i havent gotten rid of it |
|coords| dictonary| contains the postions and mountain type of all the mountains.|

we print a dot to show that the function has started before printing our windmap points and our windpoint. we set our WINDDIRECTION to the 2nd items first item in windpoint. This is because our list looks like this:
```point, [data].``` we print our direction and get the keys for all the windmap points. we print our keys and print the first item of windpoint., which is the tag for what point it is.

## Setting up our last point
```
    if windpoint[0] == "point2":
        #if windpoint is point2, we want to go backwards, since i dont want to have it calculate wind direction based on a windzone 2 zone's away.
        currentindex = 2
        final = True
        #let it know that we are on the final item,
        print(currentindex - 1)
        #print out cirrent item - 1.
        lastpoint = windmappoints[keys[currentindex - 1]]
        #our last point wil be the item before the current index. it should technacily be first point outside of this, but im too lazy to care :| 
        print(lastpoint)
        print(f"last {lastpoint}")
```
if the point is point2 (the last item), we should set our index to two and set final to true. We'll print our current index -1, and set our last point to the key of current index -1, which, in this case, is inbetween. 
```
    else:
        currentindex = keys.index(windpoint[0])
        #if its not point two, we can just get the index of the current item and set last point to one, as well as final to false.
        lastpoint = windmappoints[keys[currentindex + 1]]
        final = False
```
id it isnt point2, we set our index to the number of out current point, and set last point to that item  +1, getting the next item. We also set Final to false.
## setting our climate direction
```
    if windpoint[1][1] != lastpoint[1]:
        climatewinddirection = (f"{windpoint[1][1]}{lastpoint[1]}")
        # if windpoints second items second item is not the same as lasts points second item , we set them togter the reasono that  there's two [1]s is because its removed our key, thus getting straight into out list
    else:
        climatewinddirection = ({windpoint[1][1]})
```
if our windpoints 2nd peice of data(after our y postion of our line inside our second part (the wind direction), isnt equal to lastpoints 2nd peice of data(since lastpoint doesnt include our point number) our climate directions will be the two combined together.
if it is, we set tge winddirection to the wid directon of windpoint.

## making our tempratures:
```
    climatetempratures = []
    climatetempratures.append(list(windpoint[1][2][0]))
    climatetempratures.append(list(lastpoint[2][0]))
    #we append both, to the climate tempratures before geting the final temprature which is going to be our two climate temps added
    climatetempfinal = (climatetempratures[0][0] + climatetempratures[1][0]/2,climatetempratures[0][1] + climatetempratures[1][1] /2)
    print(climatetempratures)
    print(climatetempfinal)
```
we reset our climatetemrpatures, and append windpoints temrpature's , which are inside a tuple, and lastpoints tempratures. 
we then set climatetempfinal the first temrpature pairs first item plus the second temprature pairs first item, and divide it by two,  while we do the same with the second items of both pairs.
we print our tempratures and our final temprature.

