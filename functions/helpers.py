from functions.blinds import *

inf = -1000000000

blindMin = inf
blindMax = inf
blindCur = 0

def loadLog():
    global blindMin, blindMax, blindCur, log
    
    log = open("log.txt", "r")

    data = log.read()

    mode = 0
    prev = 0
    for i in range(len(data)):
        if data[i] == " " or data[i] == "\n":
            if mode == 0:
                blindMin = int(data[prev:i])
                prev = i + 1
                mode += 1
            elif mode == 1:
                blindMax = int(data[prev:i])
                prev = i + 1
                mode += 1
            else:
                blindCur = int(data[prev:i])
                prev = i + 1
                mode += 1

    log.close()
    
    print("Load: ")
    print(blindMin, end = " ")
    print(blindMax, end = " ")
    print(blindCur)

def updateLog():
    global log

    log = open("log.txt", "w")

    newData = str(blindMin) + " " + str(blindMax) + " " + str(blindCur) + "\n"
    
    log.write(newData)

    log.close()
    
    print("Upload: ")
    print(blindMin, end = " ")
    print(blindMax, end = " ")
    print(blindCur)

def getMin():
    loadLog()
    return blindMin

def getMax():
    loadLog()
    return blindMax

def getCur():
    loadLog()
    return blindCur
    
def blindsUp(v=None):
    global blindMin, blindMax, blindCur

    loadLog()
    
    if blindCur == blindMax:
        print("TOP")
        return None
    
    if (not v or v > blindMax - blindCur) and blindMin != inf and blindMax != inf:
        return blindsUp(blindMax - blindCur)
    elif not v:
        return None

    up(v)

    blindCur += v

    updateLog()
    
    print("BLINDS UP")
    
def blindsDown(v=None):
    global blindMin, blindMax, blindCur

    loadLog()
    
    if blindCur == blindMin:
        print("BOTTOM")
        return None
    
    if (not v or v > blindCur - blindMin) and blindMin != inf and blindMax != inf:
        return blindsDown(blindCur - blindMin)
    elif not v:
        return None

    down(v)

    blindCur -= v

    updateLog()

    print("BLINDS DOWN")

def setMin():
    global blindMin, blindMax, blindCur

    loadLog()

    if blindMin != inf:
        return None

    if blindMax == inf:
        blindMin = 0
        blindCur = 0
    else:
        blindMin = blindCur
        if blindMin < 0:
            blindMax -= blindMin
            blindMin = 0
            blindCur = 0

    updateLog()

def setMax():
    global blindMin, blindMax, blindCur

    loadLog()

    if blindMax != inf:
        return None

    blindMax = blindCur

    updateLog()

def reset():
    global blindMin, blindMax, blindCur
    
    loadLog()
    
    blindMin = inf
    blindMax = inf
    blindCur = 0
    
    updateLog()