import turtle

def validate(angle):
    if(angle >= 0 and angle <= 360):
        print(angle, "is an angle.")
        return angle
    else:
        print(angle, "is not an angle.")
        return -1

def readfile(fileName):
    f = open(fileName,"r")
    dic = {"angle": 0, "iters": 0, "axiom": "", "set1temp": "", "set2temp": ""}
    li = []
    for line in range(0,5):
        li.append(f.readline().split())
    dic["angle"] = ",".join(li[0])
    dic["iters"] = ",".join(li[1])
    dic["axiom"] = ",".join(li[2])
    print(li[3])
    set1key = str(li[3]).replace("[","").replace("]","").replace("'","").replace(",","")
    set1 = set1key[0:-(len(set1key)-1)]
    dic["key1"] = set1[:len(set1key)-1]
    dic[set1] = dic.pop("set1temp")
    set1value = str(li[3]).replace("[","").replace("]","").replace("'","").replace(",","")
    set1v = set1value[4:]
    set2key = str(li[4]).replace("[","").replace("]","").replace("'","").replace(",","")
    set2 = set2key[0:-(len(set2key)-1)]
    dic["key2"] = set2[:len(set2key)-1]
    dic[set1] = dic.pop("set2temp")
    set2value = str(li[4]).replace("[","").replace("]","").replace("'","").replace(",","")
    set2v = set2value[4:]
    print("The key is " + set1 + " and the value is " + set1v)
    print("The key is " + set2 + " and the value is " + set2v)
    dic["set1"] = set1v
    dic["set2"] = set2v
    if (validate(int(dic["angle"])) == -1):
        dic["angle"] = 90
    return dic

def rules(dic):
    #Dictionary: angle, iters, axiom, key1, set1, key2, set2
    result = dic["axiom"]
    for i in range(int(dic["iters"])):
        #Check each character and replace with the substitutions
        if result.count(dic["key1"]) > 0:                                       #Checks if key1 count is > 0
            result = result.replace(dic["key1"], "1")                           #Changes key1's into 1
            if result.count(dic["key2"]) > 0:
                result = result.replace(dic["key2"], dic["set2"])               #Changes key2's into set2
                result = result.replace(dic["key1"], "3")                       #Changes key1 from set2 into 3
            result = result.replace("1",dic["set1"])                            #Changes 1 into set1
            if result.count("3") > 0:
                result = result.replace("3",dic["key1"])                        #Changes 3's back into key1
    print(result)
    return result

def drawLsystem(t, dic, s):
    for i in s:
        if i == 'F':
            t.forward(10)
        if i == '+':
            t.right(int(dic["angle"]))
        if i == '-':
            t.left(int(dic["angle"]))

def main():
    hilbert = "hilbertcurve.txt"
    dragon = "dragoncurve.txt"
    arrow = "arrowheadcurve.txt"
    peanogosper = "peanogospercurve.txt"
    sierpinskitriangle = "sierpinskitrianglecurve.txt"

    t = turtle.Turtle()
    wn = turtle.Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, readfile(hilbert), rules(readfile(hilbert)))
    #drawLsystem(t, readfile(dragon), rules(readfile(dragon)))
    #drawLsystem(t, readfile(arrow), rules(readfile(arrow)))
    #drawLsystem(t, readfile(peanogosper), rules(readfile(peanogosper)))
    #drawLsystem(t, readfile(sierpinskitriangle), rules(readfile(sierpinskitriangle)))
    wn.exitonclick()
main()
