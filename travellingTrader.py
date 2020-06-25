import turtle
from random import randint
import math
import time
import json

wn = turtle.Screen()
wn.tracer(0)
wn.title("TRAVELING TRADER")
wn.setup(width = 800, height = 800)

grid = turtle.Turtle()
wn.addshape("grid2.gif")
wn.addshape("Traveling.gif")
wn.addshape("Caravan.gif")
wn.addshape("Overview.gif")
wn.addshape("Resources.gif")
grid.shape("grid2.gif")
grid.up()
grid.ht()

enemy1 = turtle.Turtle()
enemy1.ht()
enemy1.up()
enemy1.color("red")

enemy2 = turtle.Turtle()
enemy2.ht()
enemy2.up()
enemy2.color("red")

pen1 = turtle.Turtle()
pen1.ht()
pen1.up()

pen2 = turtle.Turtle()
pen2.ht()
pen2.up()

pen3 = turtle.Turtle()
pen3.ht()
pen3.up()

pen4 = turtle.Turtle()
pen4.ht()
pen4.up()

sellButtonPen = turtle.Turtle()
sellButtonPen.ht()
sellButtonPen.up()

buyButtonPen = turtle.Turtle()
buyButtonPen.ht()
buyButtonPen.up()

mouse = turtle.Turtle()
mouse.up()
mouse.ht()

player = turtle.Turtle()
player.up()
player.ht()
player.seth(45)

font = "Courier"

townPrefixes = ['John', 'Daniel', 'Ryan', 'Elias', 'Jack', 'Samantha', 'Matt', 'Claire', 'Kevin', 'Nathan', 'Allen', 'Prakash', 'Alex', 'Sean', 'Rei', 'Dylan', 'Marilyn', 'Elmore', 'James']
townSuffixes = ['port', 'view', 'ford', 'town', 'bury', 'ville', 'burg', 'polis', 'borough', 'ton', 'land', ' City']

#15 goods including food and water
goods = ['leather', 'cotton', 'wool', 'yarn', 'fuel', 'cloth', 'spices', 'pants', 'shoes', 'jackets', 'gold', 'jewelry', 'medicines', 'donkeys', 'horses', 'camels']
allMarketItems = ['food', 'water', 'leather', 'cotton', 'wool', 'yarn', 'fuel', 'cloth', 'spices', 'pants', 'shoes', 'jackets', 'gold', 'jewelry', 'medicines', 'donkeys', 'horses', 'camels']

goodTypes = {'leather': 'high',
         'cotton': 'high',
         'wool': 'high',
         'yarn': 'high',
         'fuel': 'medium',
         'cloth': 'medium',
         'spices': 'medium',
         'pants': 'low',
         'shoes': 'low',
         'jackets': 'low',
         'gold': 'scarce',
         'jewelry': 'scarce',
         'medicines': 'scarce',
            'donkeys':'animal',
            'horses':'animal',
             'camels':'animal'}

averageCosts = {'food':10,
                'water': 5,
            'leather': 30,
             'cotton': 5,
             'wool': 10,
             'yarn': 15,
             'fuel': 40,
             'cloth': 25,
             'spices': 100,
             'pants': 60,
             'shoes': 40,
             'jackets': 100,
             'gold': 10000,
             'jewelry': 5000,
             'medicines': 1000,
            'donkeys':15000,
            'horses':50000,
             'camels':30000}

weights = {'food': 1,
            'water': 1,
            'leather': 1,
             'cotton': 0.05,
             'wool': 0.1,
             'yarn': 0.2,
             'fuel': 1,
             'cloth': 1,
             'spices': 0.1,
             'pants': 1,
             'shoes': 0.5,
             'jackets': 1,
             'gold': 0.1,
             'jewelry': 0.1,
             'medicines': 0.1}

#Next 5 functions are all for initializing the array
def initializeGoods(producedGoods, population, goodTypes):
    goods = {}
    for good in producedGoods:
        sqrtPopulation = population ** (1/2)
        if good == "water" or good == "food" or goodTypes[good] == 'high':
            goods[good] = int(sqrtPopulation * randint(11, 15))
        elif goodTypes[good] == 'medium':
            goods[good] = int(sqrtPopulation * randint(7, 13) / 10)
        elif goodTypes[good] == 'low':
            goods[good] = int(sqrtPopulation / randint(40,60) * 10)
        elif goodTypes[good] == 'scarce':
            goods[good] = int(sqrtPopulation / randint(8, 12))
        elif goodTypes[good] == 'animal':
            goods[good] = math.ceil(sqrtPopulation / randint(80, 120))
    return goods

def initializeConsumptionRates(population, allMarketItems, goodTypes):
    rates = {}
    for good in allMarketItems:
        sqrtPopulation = population ** (1/2)
        if good == "water" or good == "food":
            rates[good] = round(sqrtPopulation * randint(170, 230) / 100,2)
        elif goodTypes[good] == "high":
            rates[good] = round(sqrtPopulation * randint(340, 550) / 100,2)
        elif goodTypes[good] == 'medium':
            rates[good] = round(sqrtPopulation * randint(100, 150) / 1000,2)
        elif goodTypes[good] == 'low':
            rates[good] = round(sqrtPopulation / randint(40,60),2)
        elif goodTypes[good] == 'scarce':
            rates[good] = round(sqrtPopulation / randint(80, 120),2)
        elif goodTypes[good] == 'animal':
            rates[good] = round(sqrtPopulation / randint(200, 250), 2)
    return rates

def produceGoods(producedGoods, initialAmounts, market, timeElapsed):
    for good in market:
        if good in producedGoods:
            startAmount = market[good]
            market[good] = market[good] + int(round(initialAmounts[good] / randint(100,120)*10 * (initialAmounts[good]*2-market[good])/initialAmounts[good]*2)*timeElapsed)
            if market[good] > initialAmounts[good]*2 and startAmount < market[good]:
                market[good] = int(round(2*initialAmounts[good]*randint(850,999) / 1000))
                

def consumeGoods(market, consumptionRates, timeElapsed):
    for good in market:
        if market[good] > 0:
            market[good] = market[good] - int(round(consumptionRates[good] * timeElapsed))
        if market[good] < 0:
            market[good] = 0
    
def getRandomPopulation():
    i = randint(1,3)
    if i == 1:
        return ('small', randint(1000,9999))
    if i == 2:
        return ('medium', randint(10000, 99999))
    if i == 3:
        return ('large', randint(100000, 999999))

def getInitialCosts(averageCosts, allMarketItems, producedGoods, demandedGoods):
    initialCosts = {}
    for item in allMarketItems:
        if item in producedGoods:
            initialCosts[item] = round(averageCosts[item] * randint(700, 800)/1000,2)
        elif item in demandedGoods:
            initialCosts[item] = round(averageCosts[item] * randint(1200,1300)/1000,2)
        else:
            initialCosts[item] = round(averageCosts[item] * randint(900, 1100)/1000, 2)
    return initialCosts

def getCost(goodTypes, good, cities, city):

    if good in cities[city]['goods']['market']:
        numGood = cities[city]['goods']['market'][good]
    else:
        numGood = 0
    goodCost = cities[city]['goods']['initialCosts'][good]
    sqrtPopulation = cities[city]['population']
    cost = 0

    if good == "water" or good == "food" or goodTypes[good] == "high":
        constant = sqrtPopulation * 20
        cost = (constant - numGood)/constant * goodCost
    elif goodTypes[good] == 'medium':
        constant = sqrtPopulation *1.5
        cost = (constant - numGood)/constant * goodCost
    elif goodTypes[good] == 'low':
        constant = sqrtPopulation / 3
        cost = (constant - numGood)/constant * goodCost
    elif goodTypes[good] == 'scarce':
        constant = sqrtPopulation / 7
        cost = (constant - numGood)/constant * goodCost
    elif goodTypes[good] == 'animal':
        constant = sqrtPopulation / 70
        cost = (constant - numGood)/constant * goodCost
    if cost < 0:
        cost = goodCost / 10
    return round(cost * 0.95, 2)

def getProducedGoods(goodTypes, size, goods):
    producedGoods = ['food', 'water']
    arrayLength = 0
    if size == 'small':
        arrayLength = 4
    if size == 'medium':
        arrayLength = 6
    if size == 'large':
        arrayLength = 8
    while not arrayLength == len(producedGoods):
        randNum = randint(0, len(goods) -1)
        if goods[randNum] not in producedGoods:
            producedGoods.append(goods[randNum])
    return producedGoods

def getDemandedGoods(goodTypes, size, producedGoods, goods):
    demandedGoods = []
    arrayLength = 0
    if size == 'small':
        arrayLength = 2
    if size == 'medium':
        arrayLength = 4
    if size == 'large':
        arrayLength = 6
    while not arrayLength == len(demandedGoods):
        randNum = randint(0, len(goods) -1)
        if goods[randNum] not in producedGoods and goods[randNum] not in demandedGoods:
            demandedGoods.append(goods[randNum])
    return demandedGoods

def initializeCities(cities, goodTypes, averageCosts, goods, allMarketItems):
    for prefix in townPrefixes:
        townName = prefix + townSuffixes[randint(0, len(townSuffixes)-1)]
        cities[townName] = {}
        populationInfo = getRandomPopulation()
        cities[townName]['population'] = populationInfo[1]
        cities[townName]['size'] = populationInfo[0]
        cityX = randint(30,970)
        cityY = randint(30,970)
        while cityX > 880 and cityY < 80:
            cityX = randint(30,970)
            cityY = randint(30,970)
        cities[townName]['coordinates'] = (cityX, cityY)
        producedGoods = getProducedGoods(goodTypes, populationInfo[0], goods)
        demandedGoods = getDemandedGoods(goodTypes, populationInfo[0], producedGoods, goods)
        initialMarket = initializeGoods(producedGoods,populationInfo[1],goodTypes)
        cities[townName]['goods'] = {}
        cities[townName]['goods']['producedGoods'] = producedGoods
        cities[townName]['goods']['demandedGoods'] = demandedGoods
        cities[townName]['goods']['market'] = initialMarket.copy()
        cities[townName]['goods']['initialAmounts'] = initialMarket.copy()
        cities[townName]['lastVisited'] = -1
        cities[townName]['goods']['initialCosts'] = getInitialCosts(averageCosts, allMarketItems, producedGoods, demandedGoods)
        cities[townName]['goods']['consumptionRates'] = initializeConsumptionRates(populationInfo[1], allMarketItems, goodTypes)
    print(cities)

#draw frame
def drawFrame(cities, playerInfo, turtle, pen):
    x = playerInfo['coordinates'][0] - 40
    x2 = math.ceil(x / 10) * 10
    startX = int(round((x2 - x) * 10))
    y = playerInfo['coordinates'][1] - 40
    y2 = math.ceil(y / 10) * 10
    startY = int(round((y2 - y) * 10))
    turtle.goto(startX, startY)
    drawCities(cities, playerInfo, pen)
    
def drawLongitudes(turtle):
    turtle.color("#E0E0E0")
    for i in range(0, 800, 8):
        turtle.up()
        turtle.goto(-400,i-400)
        turtle.down()
        turtle.goto(400,i-400)
    turtle.up()
    turtle.color("black")

def drawLatitudes(turtle):
    turtle.color("#E0E0E0")
    for i in range(0, 800, 8):
        turtle.up()
        turtle.goto(i-400, -400)
        turtle.down()
        turtle.goto(i-400, 400)
    turtle.up()
    turtle.color("black")


def drawCities(cities, playerInfo, pen):
    pen.color("black")
    x = playerInfo['coordinates'][0]
    y = playerInfo['coordinates'][1]
    for town in cities:
        cityX = cities[town]['coordinates'][0]
        cityY = cities[town]['coordinates'][1]
        if abs(cityX-x) <= 40 and abs(cityY-y) <= 40:
            pen.goto((cityX - x)*10, (cityY - y)*10)
            pen.dot(20)
            pen.goto((cityX - x)*10, (cityY - y)*10 + 14)
            pen.write(town, align = "center", font = (font, 18))

def turnPlayer(playerInfo, player, x, y):
    playerInfo['destinationX'] = x
    playerInfo['destinationY'] = y
    player.seth(player.towards(x,y))
    speed = playerInfo['speed']
    angle = math.radians(player.heading())
    playerInfo['dx'] = math.cos(angle) * speed/20
    playerInfo['dy'] = math.sin(angle) * speed/20

def detectCity(cities, playerInfo):
    x = playerInfo['coordinates'][0]
    y = playerInfo['coordinates'][1]
    for town in cities:
        cityX = cities[town]['coordinates'][0]
        cityY = cities[town]['coordinates'][1]
        if abs(cityX-x) <= 1 and abs(cityY-y) <= 1:
            return town
    return "None"

def drawRectangle(x1, y1, x2, y2, color, text, pen):
    pen.color("black")
    pen.begin_fill()
    pen.goto(x1,y1)
    pen.down()
    pen.goto(x1,y2)
    pen.goto(x2,y2)
    pen.goto(x2,y1)
    pen.goto(x1,y1)
    pen.color(color)
    pen.end_fill()
    pen.up()
    pen.goto((x1+x2)/2, (y2 + y1)/2-6)
    pen.color("black")
    pen.write(text, align = "center", font = (font, 14))

def drawRectangle2(x1, y1, x2, y2, color, text, text2, pen):
    pen.color("black")
    pen.begin_fill()
    pen.goto(x1,y1)
    pen.down()
    pen.goto(x1,y2)
    pen.goto(x2,y2)
    pen.goto(x2,y1)
    pen.goto(x1,y1)
    pen.color(color)
    pen.end_fill()
    pen.up()
    pen.color("black")
    pen.goto((x1+x2)/2, (y2 + y1)/2+3)
    pen.write(text, align = "center", font = (font, 10))
    pen.goto((x1+x2)/2, (y2 + y1)/2-12)
    pen.write(text2, align = "center", font = (font, 10))

def buttonClicked(x1, y1, x2, y2, mouse):
    if mouse.xcor() > x1 and mouse.xcor() < x2 and mouse.ycor() < y1 and mouse.ycor() > y2:
        return True
    return False

def resetMousePosition(mouse):
    mouse.goto(0,0)

def drawMap(cities, playerInfo, wn, player, pen, mouse):
    wn.tracer(0)
    resetMousePosition(mouse)
    drawLongitudes(pen)
    drawLatitudes(pen)
    drawRectangle(300,-330, 380, -380, "white", "Travel", pen2)
    for city in cities:
        cityX = (cities[city]['coordinates'][0]-500)*0.8
        cityY = (cities[city]['coordinates'][1]-500)*0.8
        pen.goto(cityX, cityY)
        pen.dot(5)
        pen.goto(cityX, cityY + 5)
        pen.write(city, align = "center", font = (font, 9))
    
    x = (playerInfo['coordinates'][0]-500)*0.8
    y = (playerInfo['coordinates'][1]-500)*0.8
    player.goto(x,y)
    player.color("blue")
    player.stamp()
    player.color("black")
    pen.goto(x,y+5)
    pen.color('blue')
    pen.write("You", align = "center", font = (font, 20))
    pen.color('black')
    
    while not buttonClicked(300,-330, 380, -380, mouse):
        wn.onclick(mouse.goto)
        wn.update()

    
def initializeBuildings(cities):
    for city in cities:
        numBuildings = int(cities[city]['population']**(1/3))
        buildingCoordinates = []
        height = 100
        yRange = 100
        for i in range(numBuildings):
            if cities[city]['size'] == 'large':
                height = 250
                yRange = 200
            elif cities[city]['size'] == 'medium':
                height = 150
                yRange = 150
            #x,y,width,height
            buildingCoordinates.append([randint(-400,400),-1*i*(yRange/numBuildings)-100,randint(75,125), randint(height/2,height)])
        cities[city]['buildings'] = buildingCoordinates

def goToCity(cities, city, pen, pen2, pen3, pen4, mouse, inventory, animals, weights,allMarketItems, goods, goodTypes,playerInfo, purchasePrice, wn, sellButtonPen, buyButtonPen, sellButtonCoordinates, buyButtonCoordinates):
    
    pen.goto(0,300)
    pen.write(city, align = "center", font = (font, 36))
    drawRectangle(300,-330, 380, -380, "white", "Return", pen)
    drawRectangle(-40,-330, 40, -380, "white", "Market", pen)
    drawRectangle(-380,-330, -300, -380, "white","City", pen)
    pen.width(5)
    for building in cities[city]['buildings']:
        drawBuilding(building, pen)
    pen.width(1)
    while not buttonClicked(300,-330, 380, -380, mouse):
        if buttonClicked(-380,-330, -300, -380, mouse):
            pen1.clear()
            pen2.clear()
        
            drawCityInfo(pen, cities, city, mouse)

            pen1.clear()
            mouse.goto(0,0)
            goToCity(cities, city, pen, pen2, pen3, pen4, mouse, inventory, animals, weights, allMarketItems, goods, goodTypes,playerInfo, purchasePrice, wn, sellButtonPen, buyButtonPen, sellButtonCoordinates, buyButtonCoordinates)

        if buttonClicked(-40,-330, 40, -380, mouse):
            pen1.clear()
            pen2.clear()
        
            goToTradeMenu(pen, pen2, pen3,pen4,cities, city, inventory, animals, weights, allMarketItems, mouse, goods, goodTypes, playerInfo, purchasePrice, sellButtonCoordinates, buyButtonCoordinates, wn, sellButtonPen, buyButtonPen)

            pen1.clear()
            mouse.goto(0,0)
            goToCity(cities, city, pen, pen2, pen3,pen4,mouse, inventory, animals, weights, allMarketItems, goods,goodTypes, playerInfo,purchasePrice, wn, sellButtonPen, buyButtonPen, sellButtonCoordinates, buyButtonCoordinates)
        
        wn.onclick(mouse.goto)
        wn.update()
    updateSpeed(playerInfo, animals)

def drawBuilding(buildingInfo, pen):
    pen.up()
    pen.color("black")
    pen.begin_fill()
    pen.goto(buildingInfo[0] + buildingInfo[2]/2, buildingInfo[1])
    pen.down()
    pen.goto(buildingInfo[0] + buildingInfo[2]/2, buildingInfo[1]+buildingInfo[3])
    pen.goto(buildingInfo[0] - buildingInfo[2]/2, buildingInfo[1]+buildingInfo[3])
    pen.goto(buildingInfo[0] - buildingInfo[2]/2, buildingInfo[1])
    pen.goto(buildingInfo[0] + buildingInfo[2]/2, buildingInfo[1])
    pen.color("white")
    pen.end_fill()
    pen.color("black")
    pen.up()

def waitForClick(x, y, mouse, wn):
    while mouse.xcor() == x and mouse.ycor() == y:
        wn.onclick(mouse.goto)
        wn.update()

#travel
def travelLoop(cities, playerInfo, grid, pen1, wn, mouse): 
    pen1.clear()
    wn.tracer(0)
    drawFrame(cities, playerInfo, grid, pen1)
    wn.update()
    playerInfo['coordinates'] = (playerInfo['coordinates'][0] + playerInfo['dx'], playerInfo['coordinates'][1] + playerInfo['dy'])
    time.sleep(0.01)

def initializeInventory(inventory):
    inventory['water'] += 20
    inventory['food'] += 10
    inventory['leather'] += 20

#working on this
def updateMarket(cities, city, time1, time2):
    timeElapsed = time2 - time1
    consumeGoods(cities[city]['goods']['market'], cities[city]['goods']['consumptionRates'], timeElapsed)
    produceGoods(cities[city]['goods']['producedGoods'], cities[city]['goods']['initialAmounts'], cities[city]['goods']['market'], timeElapsed)

def countCitiesVisited(cities):
    count = 0
    for city in cities:
        if cities[city]['lastVisited'] > 0:
            count += 1
    return count

def updateSpeed(playerInfo, animals):
    if animals['camels'] > 0:
        playerInfo['speed'] = 4
    elif animals['donkeys'] > 0:
        playerInfo['speed'] = 8
    elif animals['horses'] > 0:
        playerInfo['speed'] = 12
    else:
        playerInfo['speed'] = 3

def drawCaravanInfo(pen, timeInt, days , inventory, mouse, playerInfo, animals, weights, cities):
    drawLongitudes(pen)
    drawLatitudes(pen)
    
    drawRectangle(-350,325, -25, -125, "white", "", pen)
    drawRectangle(-350,-200, -25, -310, "white", "", pen)
    drawRectangle(25,325, 350, 190, "white", "", pen)
    drawRectangle(25, 115, 350, -310, "white", "", pen)
    drawRectangle(-380,-330, -300, -380, "white", "Travel", pen)

    mouse.goto(0,0)

    #titles
    pen.goto(-187.5, 340)
    pen.write("Inventory", align = "center", font = (font, 30))
    pen.goto(187.5, 340)
    pen.write("Time", align = "center", font = (font, 30))
    pen.goto(187.5, 130)
    pen.write("Status", align = "center", font = (font, 30))
    pen.goto(-187.5, -185)
    pen.write("Animals", align = "center", font = (font, 30))

    #time
    pen.goto(40,260)
    pen.write(str(timeInt) + ":00", align = "left", font = (font, 30))
    pen.goto(40,215)
    pen.write("Days elapsed: " + str(days), align = "left", font = (font, 20))

    #inventory
    counter = 0
    ownedGoods = []
    ownedAnimals = []
    for good in inventory:
        if inventory[good] > 0:
            ownedGoods.append(good)
    if 'water' not in ownedGoods:
        ownedGoods.append('water')
    if 'food' not in ownedGoods:
        ownedGoods.append('food')
    for animal in animals:
        if animals[animal] > 0:
            ownedAnimals.append(animal)
    if len(ownedAnimals) == 0:
        pen.goto(-335, -210 - 28)
        pen.write("None", align = "left", font = (font, 15))
    for good in ownedGoods:
        counter += 1
        pen.goto(-335, 315 - 28*counter)
        pen.write(good + ": " + str(inventory[good]), align = "left", font = (font, 15))
    counter = 0
    for animal in ownedAnimals:
        counter += 1
        pen.goto(-335, -210 - 28*counter)
        pen.write(animal + ": " + str(animals[animal]), align = "left", font = (font, 15))
        
    #status
    pen.goto(40, 105 - 20)
    pen.write("Health: " + str(playerInfo['health']), align = "left", font = (font, 10))
    pen.goto(40, 105 - 40)
    pen.write("Money: " + str(playerInfo['money']), align = "left", font = (font, 10))
    pen.goto(40, 105 - 60)
    pen.write("Food consumption: " + str(calculateFoodConsumption(animals)) + " pounds per day", align = "left", font = (font, 10))
    pen.goto(40, 105 - 80)
    pen.write("Water consumption: " + str(calculateWaterConsumption(animals)) + " pounds per day", align = "left", font = (font, 10))
    pen.goto(40, 105 - 100)
    pen.write("Speed: " + str(playerInfo['speed']) + " mi/hr", align = "left", font = (font, 10))
    pen.goto(40, 105 - 120)
    pen.write("Capacity used: " + str(calculateWeight(animals, inventory, weights)) + "/" + str(calculateCapacity(animals)) + " pounds", align = "left", font = (font, 10))
    pen.goto(40, 105 - 140)
    pen.write("Cities Visited: " + str(countCitiesVisited(cities)) +"/" + str(len(cities)), align = "left", font = (font, 10))
    
    while not buttonClicked(-380,-330, -300, -380, mouse):
        wn.onclick(mouse.goto)
        wn.update()

def drawCityInfo(pen, cities, city, mouse):
    drawLongitudes(pen)
    drawLatitudes(pen)
    drawRectangle(-330,310, 330, 120, "white", "", pen)
    drawRectangle(-330,70, -35, -310, "white", "", pen)
    drawRectangle(35,70, 330, -310, "white", "", pen)

    drawRectangle(-380,-330, -300, -380, "white", "Travel", pen)
    
    mouse.goto(0,0)
    
    #titles
    pen.goto(0, 325)
    pen.write("City Info", align = "center", font = (font, 30))
    pen.goto(-182.5, 15)
    pen.write("Produced Goods", align = "center", font = (font, 25))
    pen.goto(182.5, 15)
    pen.write("Demanded Goods", align = "center", font = (font, 25))

    #city info
    pen.goto(-315, 310 - 77)
    pen.write("Population: " + str(cities[city]['population']), align = "left", font = (font, 30))
    pen.goto(-315, 310 - 77*2)
    pen.write("Coordinates: " + str(cities[city]['coordinates']), align = "left", font = (font, 30))

    #produced
    counter = 0
    for good in cities[city]['goods']['producedGoods']:
        counter += 1
        pen.goto(-300, 10 - 36*counter)
        pen.write(good, align = "left", font = (font, 20))

    #demanded
    counter = 0
    for good in cities[city]['goods']['demandedGoods']:
        counter += 1
        pen.goto(65, 10 - 36*counter)
        pen.write(good, align = "left", font = (font, 20))

    while not buttonClicked(-380,-330, -300, -380, mouse):
        wn.onclick(mouse.goto)
        wn.update()

#working on this
def goToTradeMenu(pen, pen2, pen3,pen4,cities, city, inventory, animals, weights, allMarketItems, mouse, goods, goodTypes, playerInfo, purchasePrice, sellButtonCoordinates, buyButtonCoordinates, wn, sellButtonPen, buyButtonPen):

    buyButtonCoordinates = {}
    sellButtonCoordinates = {}
    
    mouse.goto(0,0)
    drawRectangle(-40,-330, 40, -380, "white", "Return", pen)
    
    drawRectangle(-400, 400, -180, -400, "white", "", pen)
    drawRectangle(400, 400, 180, -400, "white", "", pen)

    sellButtonCoordinates = {}
    buyButtonCoordinates = {}
    drawShopButtons(sellButtonPen, sellButtonCoordinates, buyButtonCoordinates, cities, city, inventory, animals)
    
    pen.goto(0,325)
    pen.write("Market", align = "center", font = (font, 40))
    pen3.goto(0,250)
    pen3.write("Money: " + str(playerInfo['money']), align = "center", font = (font, 20))
    pen3.goto(0,200)
    pen3.write("Capacity: " + str(calculateWeight(animals, inventory, weights)) + "/" +  str(playerInfo['carryingCapacity']), align = "center", font = (font, 20))

    lastDrawn = []
    buttonInfo = []
    capacityLost = 0
    while not buttonClicked(-40,-330, 40, -380, mouse):
        numGoods = 0
        
        buttonInfo = checkIfButtonClicked(sellButtonCoordinates, buyButtonCoordinates, mouse, buttonInfo)

        if buttonInfo != []:

            if buttonInfo[1] == "buy" and buttonInfo != lastDrawn:

                pen4.clear()
                pen2.clear()
                lastDrawn = buttonInfo
                cost = round(cities[city]['goods']['initialCosts'][buttonInfo[0]] * 1.05,2)
                writeBuyInfo(buttonInfo[0], cost, weights, pen2, animals)

            if buttonInfo[1] == "sell" and buttonInfo != lastDrawn:
                pen4.clear()
                pen2.clear()
                lastDrawn = buttonInfo
                cost = getCost(goodTypes, buttonInfo[0], cities, city)
                writeSellInfo(buttonInfo[0], cost, weights, pen2, animals, purchasePrice)
                
            if buttonInfo[1] == "buy" and buttonClicked(-40, -80, 40, -120, mouse):

                mouse.goto(0,0)
                
                limiter = 'cost'
                maximum = math.floor(playerInfo['money']/cost)

                difference = playerInfo['carryingCapacity'] - calculateWeight(animals, inventory, weights)
                if buttonInfo[0] in inventory:
                    maximum2 = difference / weights[buttonInfo[0]]
                    if maximum2 < maximum:
                        maximum = maximum2
                        limiter = 'capacity'

                maximum3 = cities[city]['goods']['market'][buttonInfo[0]]
                if maximum3 < maximum:
                    maximum = maximum3
                    limiter = 'supply'

                if limiter == 'cost':
                    numGoods = wn.numinput("Choose Quantity", "You have enough money to buy " + str(maximum) + " " + buttonInfo[0], minval=1, maxval=maximum)
                elif limiter == 'capacity':
                    numGoods = wn.numinput("Choose Quantity", "You have enough free capacity to buy " + str(maximum) + " " + buttonInfo[0], minval=1, maxval=maximum)
                else:
                    numGoods = wn.numinput("Choose Quantity", "The market has the supply to sell " + str(maximum) + " " + buttonInfo[0], minval=1, maxval=maximum)

                if numGoods != None:
                    numGoods = math.floor(numGoods)
                else:
                    numGoods = 0
                
                if numGoods > 0:
                    capacityGained = 0
                    if buttonInfo[0] in animals:
                        if buttonInfo[0] == 'horses':
                            capacityGained = numGoods * 250
                        elif buttonInfo[0] == 'camels':
                            capacityGained  = numGoods * 500
                        else:
                            capacityGained  = numGoods * 150
                    pen2.clear()
                    pen3.clear()
                    confirmBuyInfo(buttonInfo[0], cost, weights, pen2, animals, numGoods, capacityGained)
                    buttonInfo = [buttonInfo[0], 'confirmation', 'buy', numGoods, cost]
                    lastDrawn = buttonInfo
            if buttonInfo[1] == "sell" and buttonClicked(-40, -80, 40, -120, mouse):

                mouse.goto(0,0)
                
                limiter = 'quantity'
                maximum = 0

                if buttonInfo[0] in animals:
                    maximum = animals[buttonInfo[0]]
                    maximum2 = 0
                    difference = playerInfo['carryingCapacity'] - calculateWeight(animals, inventory, weights)
                    if buttonInfo[0] == 'horses':
                        maximum2 = math.floor(difference / 250)
                    elif buttonInfo[0] == 'camels':
                        maximum2 = math.floor(difference / 500)
                    else:
                        maximum2 = math.floor(difference / 150)
                    if maximum2 < maximum:
                        maximum = maximum2
                        limiter = 'capacity'
                
                else:
                    maximum = inventory[buttonInfo[0]]

                if limiter == 'quantity':
                    numGoods = wn.numinput("Choose Quantity", "You have " + str(maximum) + " " + buttonInfo[0], minval=1, maxval=maximum)
                else:
                    numGoods = wn.numinput("Choose Quantity", "You have enough free capacity to sell " + str(maximum) + " " + buttonInfo[0], minval=1, maxval=maximum)
                if numGoods != None:
                    numGoods = math.floor(numGoods)
                else:
                    numGoods = 0
                
                
                if numGoods > 0:
                    capacityLost = 0
                    if buttonInfo[0] in animals:
                        if buttonInfo[0] == 'horses':
                            capacityLost = numGoods * 250
                        elif buttonInfo[0] == 'camels':
                            capacityLost = numGoods * 500
                        else:
                            capacityLost = numGoods * 150
                    pen2.clear()
                    pen3.clear()
                    confirmSellInfo(buttonInfo[0], cost, weights, pen2, animals, numGoods, capacityLost)
                    buttonInfo = [buttonInfo[0], 'confirmation', 'sell', numGoods, cost]
                    lastDrawn = buttonInfo
            if buttonInfo[1] == 'confirmation':
                if buttonClicked(-40, -80, 40, -120, mouse):
                    if buttonInfo[2] == "sell":
                        
                        playerInfo['money'] += buttonInfo[3] * buttonInfo[4]
                        playerInfo['money'] = round(playerInfo['money'],2)
                        if buttonInfo[0] in inventory:
                            inventory[buttonInfo[0]] -= buttonInfo[3]
                        else:
                            animals[buttonInfo[0]] -= buttonInfo[3]
                            playerInfo['carryingCapacity'] = calculateCapacity(animals)

                        initial = 0
                        try:
                            initial = cities[city]['goods']['market'][buttonInfo[0]]
                        except:
                            initial = 0
                        cities[city]['goods']['market'][buttonInfo[0]] = initial + buttonInfo[3]

                        sellButtonCoordinates = {}
                        buyButtonCoordinates = {}
                        drawShopButtons(sellButtonPen, sellButtonCoordinates, buyButtonCoordinates, cities, city, inventory, animals)

                        pen2.clear()
                        pen3.clear()
                        pen3.goto(0,250)
                        pen3.write("Money: " + str(playerInfo['money']), align = "center", font = (font, 22))
                        pen3.goto(0,200)
                        pen3.write("Capacity: " + str(calculateWeight(animals, inventory, weights)) + "/" +  str(playerInfo['carryingCapacity']), align = "center", font = (font, 22))
                        pen4.goto(0,0)
                        pen4.write("Success!", align = "center", font = (font, 30))
                        
                        buttonInfo = []
                        lastDrawn = buttonInfo

                    elif buttonInfo[2] == "buy":
                        
                        playerInfo['money'] -= buttonInfo[3] * buttonInfo[4]
                        playerInfo['money'] = round(playerInfo['money'],2)
                        if buttonInfo[0] in inventory:
                            inventory[buttonInfo[0]] += buttonInfo[3]
                        else:
                            animals[buttonInfo[0]] += buttonInfo[3]
                            playerInfo['carryingCapacity'] = calculateCapacity(animals)

                        cities[city]['goods']['market'][buttonInfo[0]] -= buttonInfo[3]

                        sellButtonCoordinates = {}
                        buyButtonCoordinates = {}
                        drawShopButtons(sellButtonPen, sellButtonCoordinates, buyButtonCoordinates, cities, city, inventory, animals)
                        
                        pen2.clear()
                        pen3.clear()
                        pen3.goto(0,250)
                        pen3.write("Money: " + str(playerInfo['money']), align = "center", font = (font, 22))
                        pen3.goto(0,200)
                        pen3.write("Capacity: " + str(calculateWeight(animals, inventory, weights)) + "/" +  str(playerInfo['carryingCapacity']), align = "center", font = (font, 22))
                        pen4.goto(0,0)
                        pen4.write("Success!", align = "center", font = (font, 30))
                        
                        purchasePrice[buttonInfo[0]] = cost
                        
                        buttonInfo = []
                        lastDrawn = buttonInfo
                        
                        
                        
        wn.onclick(mouse.goto)
        wn.update()
    pen3.clear()
    pen4.clear()
    pen2.clear()
    sellButtonPen.clear()
    buyButtonPen.clear()

def drawShopButtons(sellButtonPen, sellButtonCoordinates, buyButtonCoordinates, cities, city, inventory, animals):
    sellButtonPen.clear()
    
    allItems = dict(inventory)
    allItems.update(animals)
    sellItems = []
    for item in allItems:
        if allItems[item] > 0:
            sellItems.append(item)
    buttonRows1 = []
    counter = 0
    while counter < len(sellItems):
        if counter == len(sellItems)-1:
            buttonRows1.append([sellItems[counter]])
            break
        buttonRows1.append([sellItems[counter], sellItems[counter+1]])
        counter += 2
    drawSellButtons(sellButtonPen, allItems, buttonRows1, sellButtonCoordinates)

    buyButtonPen.clear()

    marketItems = cities[city]['goods']['market']
    buyItems = []
    for item in marketItems:
        if marketItems[item] > 0:
            buyItems.append(item)

    buttonRows2 = []
    counter = 0
    while counter < len(buyItems):
        if counter == len(buyItems)-1:
            buttonRows2.append([buyItems[counter]])
            break
        buttonRows2.append([buyItems[counter], buyItems[counter+1]])
        counter += 2
    drawBuyButtons(buyButtonPen, marketItems, buttonRows2, buyButtonCoordinates)
    
def writeSellInfo(good, cost, weights, pen, animals, purchasePrice):  
    pen.goto(0,100)
    pen.write("Selling " + good, align = "center", font = (font, 16))
    pen.goto(0,50)
    pen.write("Value: " + str(cost) + " per unit", align = "center", font = (font, 16))
    pen.goto(0,0)
    if good in animals:
        
        if good == 'horses':
            capacityLost = 250
        elif good == 'camels':
            capacityLost = 500
        else:
            capacityLost = 150
        pen.write("Capacity lost: " + str(capacityLost)+ " per unit", align = "center", font = (font, 16))
    else:
        pen.write("Weight: " + str(weights[good]) + " per unit", align = "center", font = (font, 16))
    pen.goto(0,-50)
    price = purchasePrice[good]
    if price != -1:
        pen.write("Price last purchased at: " + str(price) + " per unit", align = "center", font = (font, 12))
    drawRectangle2(-40, -80, 40, -120, "white", "Choose", "Amount", pen)

def writeBuyInfo(good, cost, weights, pen, animals):
    pen.goto(0, 100)
    pen.write("Buying " + good, align = "center", font = (font, 16))
    pen.goto(0, 50)
    pen.write("Cost: " + str(cost) + " per unit", align = "center", font = (font, 16))
    if good in animals:
        if good == 'horses':
            capacityGained = 250
        elif good == 'camels':
            capacityGained = 500
        else:
            capacityGained = 150
        pen.goto(0,0)
        pen.write("Capacity gained: " + str(capacityGained)+ " per unit", align = "center", font = (font, 16))
        if good == 'horses':
            speed = 12
        elif good == 'camels':
            speed = 4
        else:
            speed = 8
        pen.goto(0,-50)
        pen.write("Speed: " + str(speed) + " mi/hr", align = "center", font = (font,16))
    else:
        pen.goto(0,0)
        pen.write("Weight: " + str(weights[good]) + " per unit", align = "center", font = (font, 16))
    drawRectangle2(-40, -80, 40, -120, "white", "Choose", "Amount", pen)

def confirmSellInfo(good, cost, weights, pen, animals, numGoods, capacityLost):
    pen.goto(0,100)
    pen.write("Selling " + str(round(numGoods,2)) + " " + good, align = "center", font = (font, 16))
    pen.goto(0,50)
    pen.write("Total Value: " + str(round(numGoods * cost,2)), align = "center", font = (font, 16))
    
    if good in animals:
        pen.goto(0,0)   
        pen.write("Capacity lost: " + str(capacityLost), align = "center", font = (font, 16))
    else:
        pen.goto(0,0)
        pen.write("Total weight: " + str(round(numGoods * weights[good],1)), align = "center", font = (font, 16))
    drawRectangle(-40, -80, 40, -120, "white", "Confirm", pen)

def confirmBuyInfo(good, cost, weights, pen, animals, numGoods, capacityGained):
    pen.goto(0,100)
    pen.write("Buying " + str(round(numGoods,2)) + " " + good, align = "center", font = (font, 16))
    pen.goto(0,50)
    pen.write("Total Cost: " + str(round(numGoods * cost,2)), align = "center", font = (font, 16))
    if good in animals:
        pen.goto(0, 0)
        pen.write("Capacity gained: " + str(capacityGained), align = "center", font = (font, 16))
    else:
        pen.goto(0,0)
        pen.write("Total weight: " + str(round(numGoods * weights[good],1)), align = "center", font = (font, 16))
    drawRectangle(-40, -80, 40, -120, "white", "Confirm", pen)
    
def checkIfButtonClicked(sellButtonCoordinates, buyButtonCoordinates, mouse, buttonInfo):
    for button in sellButtonCoordinates:
        if mouse.xcor() > sellButtonCoordinates[button][0] and mouse.xcor() < sellButtonCoordinates[button][2]:
            if mouse.ycor() < sellButtonCoordinates[button][1] and mouse.ycor() > sellButtonCoordinates[button][3]:
                return [button, "sell"]
    for button in buyButtonCoordinates:
        if mouse.xcor() > buyButtonCoordinates[button][0] and mouse.xcor() < buyButtonCoordinates[button][2]:
            if mouse.ycor() < buyButtonCoordinates[button][1] and mouse.ycor() > buyButtonCoordinates[button][3]:
                return [button, "buy"]
    return buttonInfo
    
#add coordinates
def drawSellButtons(pen, allItems, buttonRows, sellButtonCoordinates):
    y = 302
    pen.goto(-290, 330)
    pen.write("Sell", align = "center", font = (font, 30))
    for row in buttonRows:
        if len(row) == 1:
            sellButtonCoordinates[row[0]] = [-380, y, -300, y-50]
            drawRectangle2(-380, y, -300, y-50, "white", row[0], allItems[row[0]], pen)
        else:
            sellButtonCoordinates[row[0]] = [-380, y, -300, y-50]
            sellButtonCoordinates[row[1]] = [-280, y, -200, y-50]
            drawRectangle2(-380, y, -300, y-50, "white", row[0], allItems[row[0]], pen)
            drawRectangle2(-280, y, -200, y-50, "white", row[1], allItems[row[1]], pen)
        y -= 78

def drawBuyButtons(pen, allItems, buttonRows, buyButtonCoordinates):
    y = 302
    pen.goto(290, 330)
    pen.write("Buy", align = "center", font = (font, 30))
    for row in buttonRows:
        if len(row) == 1:
            buyButtonCoordinates[row[0]] = [300, y, 380, y-50]
            drawRectangle2(300, y, 380, y-50, "white", row[0], allItems[row[0]], pen)
        else:
            buyButtonCoordinates[row[0]] = [300, y, 380, y-50]
            buyButtonCoordinates[row[1]] = [200, y, 280, y-50]
            drawRectangle2(300, y, 380, y-50, "white", row[0], allItems[row[0]], pen)
            drawRectangle2(200, y, 280, y-50, "white", row[1], allItems[row[1]], pen)
        y -= 78
    
def drawHealthBar(pen, health, inventory):
    drawRectangle(-200, -335, 200, -375, "black", "", pen)
    difference = 396 * health / 100
    drawRectangle(-198, -337, -198 + difference, -373, "white", "", pen)
    pen.goto(0,-364)
    pen.color("red")
    pen.write("Health: " + str(health), align = "center", font = (font, 18, "bold"))
    pen.color("black")

def endGame(pen):
    pen.goto(0,0)
    pen.write("YOU DIED", align = "center", font = (font, 60, "bold"))

def calculateFoodConsumption(animals):
    return 3 + animals['camels'] * 9 + animals['donkeys']*8 + animals['horses']*15

def calculateWaterConsumption(animals):
    return 4 + animals['camels'] * 7 + animals['donkeys']*20 + animals['horses']*30

def calculateCapacity(animals):
    return 50 + animals['camels'] * 500 + animals['donkeys']*150 + animals['horses']*250

def calculateWeight(animals, inventory, weights):
    weight = 0
    for good in inventory:
        weight += round(inventory[good] * weights[good],2)
    return weight

def consumeResources(animals, inventory, playerInfo):
    
    if inventory['water'] >=0:
        inventory['water'] -= calculateWaterConsumption(animals)/2
    if inventory['food'] >= 0:
        inventory['food'] -= calculateFoodConsumption(animals)/2
    inventory['water'] = round(inventory['water'], 1)
    inventory['food'] = round(inventory['food'], 1)
    if inventory['water'] <= 0:
        playerInfo['health'] -= 10
        inventory['water'] = 0
    else:
        playerInfo['health'] += 5
    if inventory['food'] <= 0:
        playerInfo['health'] -= 10
        inventory['food'] = 0
    else:
        playerInfo['health'] += 5
    if playerInfo['health'] >= 100:
        playerInfo['health'] = 100
    if playerInfo['health'] <= 0:
        playerInfo['health'] = 0

'''
title + play + tutorial + load
save + load
'''

def initializeEnemy(enemy):
    random = randint(1,4)
    enemy.st()
    if random == 1:
        enemy.goto(randint(-400,400), -400)
    elif random == 2:
        enemy.goto(randint(-400,400), 400)
    elif random == 3:
        enemy.goto(400, randint(-400,400))
    else:
        enemy.goto(-400, randint(-400,400))
    return randint(25,35)/10

def updateEnemyLocation(enemy, enemySpeed, playerInfo):
    enemy.seth(enemy.towards(0,0))
    angle = math.radians(enemy.heading())
    dx = math.cos(angle) * enemySpeed/20
    dy = math.sin(angle) * enemySpeed/20
    enemy.forward(enemySpeed/20)
    enemy.goto(enemy.xcor() + (dx - playerInfo['dx'])*10, enemy.ycor() + (dy - playerInfo['dy'])*10)

def hideEnemies(enemy1, enemy2):
    enemy1.ht()
    enemy2.ht()

def showEnemies(enemy1, enemy2, enemies):
    if "1" in enemies:
        enemy1.st()
    if "2" in enemies:
        enemy2.st()

def detectAttack(enemy1, enemy2, enemies, inventory, playerInfo):
    enemy = "none"
    if abs(enemy1.xcor()) <= 2 and abs(enemy1.ycor()) <= 2 and "1" in enemies:
        enemy = 1
        enemy1.ht()
    elif abs(enemy2.xcor()) <= 2 and abs(enemy2.ycor()) <= 2 and "2" in enemies:
        enemy = 2
        enemy2.ht()
    else:
        return ["none", 0, enemy, 0]
    ownedGoods = []
    for good in inventory:
        if inventory[good] > 0:
            ownedGoods.append(good)
    if len(ownedGoods) >= 1:
        good = ownedGoods[randint(0,len(ownedGoods)-1)]
        numGood = math.ceil(inventory[good] * randint(20,30) / 100)
        inventory[good] -= numGood
    else:
        good = "food"
        numGood = 0
        
    healthLoss = randint(20,30)
    playerInfo['health'] -= healthLoss
    if playerInfo['health'] <= 0:
        playerInfo['health'] = 0

    

    return [good, numGood, enemy, healthLoss]

def detectOutrun(enemy):
    if enemy.xcor() < -410 or enemy.xcor() > 410 or enemy.ycor() < -410 or enemy.ycor() > 410:
        return True
    return False

def waterWarning(pen):
    pen.goto(-100,-325)
    pen.color("red")
    pen.write("Out of water!", align = "center", font = (font, 14, "bold"))
    pen.color("black")

def foodWarning(pen):
    pen.goto(100,-325)
    pen.color("red")
    pen.write("Out of food!", align = "center", font = (font, 14, "bold"))
    pen.color("black")

def saveData(purchasePrice, inventory, animals, playerInfo, cities, timeInt, timeCounter, days, enemies, enemy1Speed, enemy2Speed, outOfWater, outOfFood, cityExitCounter, justLeftCity):
    saveDict = {}
    saveDict['purchasePrice'] = purchasePrice
    saveDict['inventory'] = inventory
    saveDict['animals'] = animals
    saveDict['playerInfo'] = playerInfo
    saveDict['cities'] = cities
    saveDict['timeInt'] = timeInt
    saveDict['timeCounter'] = timeCounter
    saveDict['days'] = days
    saveDict['enemies'] = enemies
    saveDict['enemy1Speed'] = enemy1Speed
    saveDict['enemy2Speed'] = enemy2Speed
    saveDict['outOfWater'] = outOfWater
    saveDict['outOfFood'] = outOfFood
    saveDict['cityExitCounter'] = cityExitCounter
    saveDict['justLeftCity'] = justLeftCity
    saveDict['enemy1Coordinates'] = [enemy1.xcor(), enemy1.ycor()]
    saveDict['enemy2Coordinates'] = [enemy2.xcor(), enemy2.ycor()]
    with open('gameSave.txt', 'w') as saveFile:
        json.dump(saveDict, saveFile)

def drawCitiesVisited(pen, cities, mouse):

    drawLongitudes(pen)
    drawLatitudes(pen)

    mouse.goto(0,0)
    
    drawRectangle(-380, 325, -240, -310, "white", "", pen)
    drawRectangle(-230, 325, 30, -310, "white", "", pen)
    drawRectangle(40, 325, 380, -310, "white", "", pen)
    drawRectangle(-380,-330, -300, -380, "white", "Travel", pen)

    pen.goto(-310, 340)
    pen.write("City", align = "center", font = (font, 30))
    pen.goto(-100, 340)
    pen.write("Demanded Goods", align = "center", font = (font, 25))
    pen.goto(210, 340)
    pen.write("Produced Goods", align = "center", font = (font, 25))

    y = 300
    for city in cities:
        demanded = "Unknown"
        produced = "Unknown"

        if cities[city]['lastVisited'] != -1:
            demanded = str(cities[city]['goods']['demandedGoods'])
            demanded = demanded[1:len(demanded)-1]
            demanded = demanded.replace("'", "");
            produced = str(cities[city]['goods']['producedGoods'])
            produced = produced[1:len(produced)-1]
            produced = produced.replace("'", "");

        pen.goto(-310, y)
        pen.write(city, align = "center", font = (font, 12))
        pen.goto(-100, y)
        pen.write(demanded, align = "center", font = (font, 7))
        pen.goto(210, y)
        pen.write(produced, align = "center", font = (font, 7))
        y -= 33
    
    while not buttonClicked(-380,-330, -300, -380, mouse):
        wn.onclick(mouse.goto)
        wn.update()
    

def gameLoop(enemy1, enemy2, grid, font, wn, goodTypes, averageCosts, goods, allMarketItems, pen1, pen2, pen3, pen4, sellButtonPen, buyButtonPen, mouse, player, townPrefixes, townSuffixes, weights):

    load = False

    tutorialScreens = ['Overview', 'Traveling', 'Resources', 'Caravan']
    drawLongitudes(pen1)
    drawLatitudes(pen1)

    pen1.goto(0,200)
    pen1.write("Traveling Trader", align = "center", font = (font, 60))
    drawRectangle(-100,125,100,25,"white", "New Game", pen1)
    drawRectangle(-100, 0,100,-100,"white", "Load", pen1)
    drawRectangle(-100,-125,100,-225,"white", "Tutorial", pen1)

    while not buttonClicked(-100,125,100,25, mouse) and not buttonClicked(-100, 0,100,-100, mouse) and not buttonClicked(-100,-125,100,-225, mouse):
        wn.onclick(mouse.goto)
        wn.update()

    if buttonClicked(-100,-125,100,-225, mouse):
        pen1.clear()
        pen2.clear()
        
        #tutorial
        for screen in tutorialScreens:
            mouse.goto(0,0)
            pen1.goto(0, 310)
            pen1.write(screen, align = "center", font = (font, 40))
            
            pen2.goto(0,-105)
            pen2.shape(screen + ".gif")
            pen2.st()
            
            drawRectangle(-100,-200,100,-300, "white", "Continue", pen1)

            while not buttonClicked(-100,-200,100,-300, mouse):
                wn.onclick(mouse.goto)
                wn.update()
            pen1.clear()
            pen2.clear()
        #restart
        mouse.goto(-1000, -1000)

        pen2.shape("classic")
        pen2.ht()
        
        gameLoop(enemy1, enemy2, grid, font, wn, goodTypes, averageCosts, goods, allMarketItems, pen1, pen2, pen3, pen4, sellButtonPen, buyButtonPen, mouse, player, townPrefixes, townSuffixes, weights)

    if buttonClicked(-100, 0,100,-100, mouse):
        load = True

    grid.st()
    player.st()
    cityExitCounter = 0
    justLeftCity = False

    timeInt = 1
    timeCounter = 0
    days = 0

    cities = {}

    purchasePrice = {'food': -1,
                 'water': -1,
                 'leather': -1,
                 'cotton': -1,
                 'wool': -1,
                 'yarn': -1,
                 'fuel': -1,
                 'cloth': -1,
                 'spices': -1,
                 'pants': -1,
                 'shoes': -1,
                 'jackets': -1,
                 'gold': -1,
                 'jewelry': -1,
                 'medicines': -1}
    
    inventory = {'food': 0,
                 'water': 0,
                 'leather': 0,
                 'cotton': 0,
                 'wool': 0,
                 'yarn': 0,
                 'fuel': 0,
                 'cloth': 0,
                 'spices': 0,
                 'pants': 0,
                 'shoes': 0,
                 'jackets': 0,
                 'gold': 0,
                 'jewelry': 0,
                 'medicines': 0}
    animals = {'donkeys':0,
               'horses':0,
                'camels':0}

    playerInfo = {'coordinates': (randint(100,900), randint(100,900)), 'speed': 3, 'dy': 0, 'dx': 0, 'destinationX':0, 'destinationY':0, 'money': 1000, 'health': 100, 'carryingCapacity': 50}

    buyButtonCoordinates = {}
    sellButtonCoordinates = {}

    initializeInventory(inventory)
    initializeCities(cities, goodTypes, averageCosts, goods, allMarketItems)
    initializeBuildings(cities)

    drawRectangle(300,-330, 380, -380, "white", "Map", pen2)
    drawRectangle(300,-260, 380, -310, "white", "Save", pen2)
    drawRectangle(-380,-330, -300, -380, "white","Caravan", pen2)
    drawRectangle(-380,-260, -300, -310, "white", "Cities", pen2)

    enemies = "none"
    enemy1.ht()
    enemy2.ht()
    enemy1Speed = 0
    enemy2Speed = 0
    saveCounter = -1

    outOfWater = False
    outOfFood = False

    if load == True:
        loadDict = {}
        with open('gameSave.txt', 'r') as saveFile:
            loadDict = json.load(saveFile)
        purchasePrice = loadDict['purchasePrice']
        inventory = loadDict['inventory']
        animals = loadDict['animals']
        playerInfo = loadDict['playerInfo']
        cities = loadDict['cities']
        timeInt = loadDict['timeInt']
        timeCounter = loadDict['timeCounter']
        days = loadDict['days']
        enemies = loadDict['enemies']
        enemy1Speed = loadDict['enemy1Speed']
        enemy2Speed = loadDict['enemy2Speed']
        outOfWater = loadDict['outOfWater']
        outOfFood = loadDict['outOfFood']
        cityExitCounter = loadDict['cityExitCounter']
        justLeftCity = loadDict['justLeftCity']
        enemy1.goto(loadDict['enemy1Coordinates'][0], loadDict['enemy1Coordinates'][1])
        enemy2.goto(loadDict['enemy2Coordinates'][0], loadDict['enemy2Coordinates'][1])
        
        mouse.goto(playerInfo['destinationX'],playerInfo['destinationY'])
        
    showEnemies(enemy1, enemy2, enemies)
    drawHealthBar(pen2, playerInfo['health'], inventory)

    if outOfWater == True:
        waterWarning(pen4)
    if outOfFood == True:
        foodWarning(pen4)
    
    while True:
        
        timeCounter += 1
        if timeCounter >= 20:
            timeCounter = 0
            timeInt += 1
            if timeInt == 12 or timeInt == 24:
                consumeResources(animals, inventory, playerInfo)

                if inventory['water'] == 0 and outOfWater == False:
                    outOfWater = True
                    waterWarning(pen4)

                if inventory['food'] == 0 and outOfFood == False:
                    outOfFood = True
                    foodWarning(pen4)
                
                drawHealthBar(pen2, playerInfo['health'], inventory)
                if playerInfo['health'] == 0:
                    player.ht()
                    pen1.clear()
                    pen2.clear()
                    pen4.clear()
                    enemy1.ht()
                    enemy2.ht()
                    endGame(pen1)
                    wn.update()
                    drawRectangle(-175, -40, -25, -100, "white", "Play Again", pen1)
                    drawRectangle(25, -40, 175, -100, "white", "Exit Game", pen1)
                    mouse.goto(-400,-400)
                    while not buttonClicked(25, -40, 175, -100, mouse):  
                        wn.onclick(mouse.goto)
                        wn.update()
                        if buttonClicked(-175, -40, -25, -100, mouse):
                            grid.ht()
                            pen1.clear()
                            pen2.clear()
                            mouse.goto(-400,-400)
                            wn.update()
                            gameLoop(enemy1, enemy2, grid, font, wn, goodTypes, averageCosts, goods, allMarketItems, pen1, pen2, pen3, pen4, sellButtonPen, buyButtonPen, mouse, player, townPrefixes, townSuffixes, weights)
                            pass
                    wn.bye()
                    break
            if timeInt > 24:
                timeInt = 1
                days += 1
                
        if justLeftCity == True:
            cityExitCounter += 1
            if cityExitCounter >= 20:
                justLeftCity = False
                cityExitCounter = 0

        travelLoop(cities, playerInfo, grid, pen1, wn, mouse)
        wn.onclick(mouse.goto)

        if "1" in enemies:
            updateEnemyLocation(enemy1, enemy1Speed, playerInfo)
            if detectOutrun(enemy1):

                if enemies == "1 and 2":
                    enemies = "2"
                else:
                    enemies = "none"

        if "2" in enemies:
            updateEnemyLocation(enemy2, enemy2Speed, playerInfo)
            if detectOutrun(enemy2):

                if enemies == "1 and 2":
                    enemies = "1"
                else:
                    enemies = "none"

        if enemies != "none":
            
            attack = detectAttack(enemy1, enemy2, enemies, inventory, playerInfo)
            if attack[0] != "none":
                if enemies == "1 and 2":
                    if attack[2] == 1:
                        enemies = "2"
                        enemy1Speed = 0
                    elif attack[2] == 2:
                        enemies = "1"
                        enemy2Speed = 0
                elif enemies == "1":
                    enemies = "none"
                    enemy1Speed = 0
                else:
                    enemies = "none"
                    enemy2Speed = 0
                player.ht()
                x = mouse.xcor()
                y = mouse.ycor()
                mouse.goto(0,0)
                drawRectangle(-200, 200, 200, -200, "white", "", pen3)
                pen3.goto(0, 125)
                pen3.write("You have been attacked by bandits!", align = "center", font = (font, 13))
                pen3.goto(0, 65)
                pen3.write("You took " + str(attack[3]) + " damage.", align = "center", font = (font, 24))
                pen3.goto(0, 25)
                pen3.write(str(attack[1]) + " " + attack[0] + " were/was stolen from your caravan.", align = "center", font = (font, 10))
                drawRectangle(-50, -70, 50, -130, "white", "close", pen3)
                while not buttonClicked(-50, -70, 50, -130, mouse):
                    wn.onclick(mouse.goto)
                    wn.update()
                mouse.goto(x,y)
                pen3.clear()
                player.st()
                drawHealthBar(pen2, playerInfo['health'], inventory)
                attack = ["none", 0, "none", 0]
                if playerInfo['health'] == 0:
                    mouse.goto(0,0)
                    enemy1.ht()
                    enemy2.ht()
                    player.ht()
                    pen1.clear()
                    pen2.clear()
                    pen4.clear()
                    endGame(pen1)
                    wn.update()
                    drawRectangle(-175, -40, -25, -100, "white", "Play Again", pen1)
                    drawRectangle(25, -40, 175, -100, "white", "Exit Game", pen1)
                    while not buttonClicked(25, -40, 175, -100, mouse):
                        if buttonClicked(-175, -40, -25, -100, mouse):
                            grid.ht()
                            pen1.clear()
                            pen2.clear()
                            mouse.goto(-400,-400)
                            wn.update()
                            gameLoop(enemy1, enemy2, grid, font, wn, goodTypes, averageCosts, goods, allMarketItems, pen1, pen2, pen3, pen4, sellButtonPen, buyButtonPen, mouse, player, townPrefixes, townSuffixes, weights)
                            pass
                        wn.onclick(mouse.goto)
                        wn.update()
                    mouse.goto(0,0)
                    wn.bye()
                    break
                
        if randint(1,200) == 1 and enemies == "none":
            enemy1Speed = initializeEnemy(enemy1)
            enemies = "1"

            if randint(1,4) == 1:
                enemy2Speed = initializeEnemy(enemy2)
                enemies = "1 and 2"
            
        
        if buttonClicked(300,-330, 380, -380, mouse):
            
            hideEnemies(enemy1, enemy2)
            grid.ht()
            player.ht()
            pen1.clear()
            pen2.clear()
            pen4.clear()
            
            drawMap(cities, playerInfo, wn, player, pen1, mouse)
            
            mouse.goto(playerInfo['destinationX'],playerInfo['destinationY'])
            
            pen1.clear()
            drawRectangle(300,-330, 380, -380, "white", "Map", pen2)
            drawRectangle(300,-260, 380, -310, "white", "Save", pen2)
            drawRectangle(-380,-330, -300, -380, "white", "Caravan", pen2)
            drawRectangle(-380,-260, -300, -310, "white", "Cities", pen2)
            
            drawHealthBar(pen2, playerInfo['health'], inventory)
            player.goto(0,0)
            player.clearstamps()
            player.st()
            grid.st()
            showEnemies(enemy1, enemy2, enemies)
            if outOfWater == True:
                waterWarning(pen4)
            if outOfFood == True:
                foodWarning(pen4)

        if buttonClicked(300,-260, 380, -310, mouse):
            
            saveCounter = 0
            drawRectangle(300,-260, 380, -310, "white", "Saved!", pen2)
            saveData(purchasePrice, inventory, animals, playerInfo, cities, timeInt, timeCounter, days, enemies, enemy1Speed, enemy2Speed, outOfWater, outOfFood, cityExitCounter, justLeftCity)

            mouse.goto(playerInfo['destinationX'],playerInfo['destinationY'])

        if saveCounter >= 0:
            saveCounter += 1
            if saveCounter == 60:
                saveCounter = -1
                drawRectangle(300,-260, 380, -310, "white", "Save", pen2)
        
        if buttonClicked(-380,-330, -300, -380, mouse):

            hideEnemies(enemy1, enemy2)
            grid.ht()
            player.ht()
            pen1.clear()
            pen2.clear()
            pen4.clear()
            
            drawCaravanInfo(pen1, timeInt, days , inventory, mouse, playerInfo, animals, weights, cities)
            
            mouse.goto(playerInfo['destinationX'],playerInfo['destinationY'])

            pen1.clear()
            drawRectangle(300,-330, 380, -380, "white", "Map", pen2)
            drawRectangle(300,-260, 380, -310, "white", "Save", pen2)
            drawRectangle(-380,-330, -300, -380, "white", "Caravan", pen2)
            drawRectangle(-380,-260, -300, -310, "white", "Cities", pen2)
            drawHealthBar(pen2, playerInfo['health'], inventory)
            player.goto(0,0)
            player.st()
            grid.st()
            showEnemies(enemy1, enemy2, enemies)
            if outOfWater == True:
                waterWarning(pen4)
            if outOfFood == True:
                foodWarning(pen4)

        #working on this
        if buttonClicked(-380,-260, -300, -310, mouse):

            hideEnemies(enemy1, enemy2)
            grid.ht()
            player.ht()
            pen1.clear()
            pen2.clear()
            pen4.clear()
            
            drawCitiesVisited(pen1, cities, mouse)
            
            mouse.goto(playerInfo['destinationX'],playerInfo['destinationY'])

            pen1.clear()
            drawRectangle(300,-330, 380, -380, "white", "Map", pen2)
            drawRectangle(300,-260, 380, -310, "white", "Save", pen2)
            drawRectangle(-380,-330, -300, -380, "white", "Caravan", pen2)
            drawRectangle(-380,-260, -300, -310, "white", "Cities", pen2)
            drawHealthBar(pen2, playerInfo['health'], inventory)
            player.goto(0,0)
            player.st()
            grid.st()
            showEnemies(enemy1, enemy2, enemies)
            if outOfWater == True:
                waterWarning(pen4)
            if outOfFood == True:
                foodWarning(pen4)
        
        turnPlayer(playerInfo, player, mouse.xcor(), mouse.ycor())
        
        city = detectCity(cities, playerInfo)
        if justLeftCity == True:
            city = "None"
        if city != "None":

            hideEnemies(enemy1, enemy2)
            enemies = "none"
            enemy1Speed = 0
            enemy2Speed = 0
            grid.ht()
            player.ht()
            pen1.clear()
            pen2.clear()
            pen4.clear()

            x = mouse.xcor()
            y = mouse.ycor()

            newTime = days + timeInt/24
            updateMarket(cities, city, cities[city]['lastVisited'], newTime)
            
            goToCity(cities, city, pen1, pen2, pen3,pen4,mouse, inventory, animals, weights,allMarketItems, goods,goodTypes, playerInfo, purchasePrice,wn, sellButtonPen, buyButtonPen, sellButtonCoordinates, buyButtonCoordinates)
        
            cities[city]['lastVisited'] = newTime

            mouse.goto(playerInfo['destinationX'],playerInfo['destinationY'])
            
            pen1.clear()
            drawRectangle(300,-330, 380, -380, "white", "Map", pen2)
            drawRectangle(300,-260, 380, -310, "white", "Save", pen2)
            drawRectangle(-380,-330, -300, -380, "white", "Caravan", pen2)
            drawRectangle(-380,-260, -300, -310, "white", "Cities", pen2)
            drawHealthBar(pen2, playerInfo['health'], inventory)

            if outOfWater == False:
                if inventory['water'] == 0:
                    outOfWater = True
                    waterWarning(pen4)
            elif inventory['water'] > 0:
                outOfWater = False
            else:
                waterWarning(pen4)
                
            if outOfFood == False:
                if inventory['food'] == 0:
                    outOfFood = True
                    foodWarning(pen4)
            elif inventory['food'] > 0:
                outOfFood = False
            else:
                foodWarning(pen4)
                
            player.st()
            grid.st()
            drawFrame(cities, playerInfo, grid, pen1)
            player.seth(0)
            player.shape("square")
            player.shapesize(1/2,1/2)
            player.color("red")
            waitForClick(x,y,mouse,wn)
            player.shapesize(1,1)
            player.shape("classic")
            player.color("black")
            justLeftCity = True
            

gameLoop(enemy1, enemy2, grid, font, wn, goodTypes, averageCosts, goods, allMarketItems, pen1, pen2, pen3, pen4, sellButtonPen, buyButtonPen, mouse, player, townPrefixes, townSuffixes, weights)







