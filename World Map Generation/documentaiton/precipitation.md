# Precipitation Function

## Settup
```
def preciptationgen(centre,coords,riverlist):
    preciptitation = ()
    part1preciptation = 0
    print(".")
    roundedcentre = (centre[0] // 100) * 100
    print(roundedcentre)
```
We begin by defining our function and setting our precpitation to a empty tuple, and our precipitations first part to 0.
we print a dot to show that our function is working, and set our rounded center to our first number in our tuple divided by a hundred and multiplied by a hundred
## seting up part 1 precipitation
```
    for i in coords.items():
        print(i[1][1][0])
        if i[1][1][0] > roundedcentre and i[1][1][0] < (roundedcentre + roundedcentre / 2):
            #takes our rounded centre and adds it by a 10th of half the elevation. 
            part1preciptation = roundedcentre / 10 + (i[1][1][0] - roundedcentre / 2) / 10
        else:
            part1preciptation = roundedcentre / 10 + 15.5
```
for each mountains in our coords, we print the mountians secocond points x positon. if said x posiotn is greater than rounded center but less than rounded center 30, suggesting that it is close, we make
part1precpitiation be our center /10 and added by the second point of our mountains x - our center / 2, with that devided by 10.
if it isnt near by, part1precipitaiton is simply a tenth of our center added with 15.5.

## finding river center:

```
    finalx = 0
    finaly = 0
    for i in  riverlist:
        print(f"RIVER {i}")
        finalx = sum(pt[0] for pt in i) / len(i)
        finaly = sum(pt[1] for pt in i) / len(i)
       divisorriver = (finalx,finaly)

```
we initialize our final x and y before making them the avrages of all the x and y's in the rivers.
we set our divisour river to our araveged x and y.
#setting part 2 precipitatipn

```
if divisorriver[0] > roundedcentre and divisorriver[0] < divisorriver[0] + 30:
        part2preciptation = (divisorriver[0] - roundedcentre) / 5
else:
     part2preciptation = 20
     print(f"total precipitation {part1preciptation + part2preciptation}")
     totalprecp = (part1preciptation + part2preciptation)
= preciptitation = ((( (part1preciptation + part2preciptation) / 2) / 3 * 2) + 10, ((part1preciptation + part2preciptation) / 2) / 3 + 15.5)
print(f"inches of rainfall each year: {preciptitation}")
```
If the x of our positon is greater than rounded center and our divisorriver is less than itself + 30:
part 2 precipiation will be our divisor river minus our rounded center / 5.
if not, we set it to twenty.
we set our total prep to the two added
we set our precipitation too the two precipiation halfs divided by 2, divide that by three, multiply by 2, add 1-, and do the same thing with the second 1 except its + 15.5 and no *2.
we print this.
