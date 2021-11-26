from functions.blinds import *

log = open("log.txt", "w+")

data = log.readline()

blindMin = None
blindMax = None
blindCur = None

mode = 0
prev = 0
for i in len(data):
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

def updateLog():
    newData = str(blindMin) + " " + str(blindMax) + " " + str(blindCur) + "\n"
    log.write(newData)

def blindsUp(v=None):
    if not v and blindMin and blindMax:
        return blindsUp(blindMax - blindCur)

    up(v)
    
    print("BLINDS UP")
    
def blindsDown(v=None):
    if not v and blindMin and blindMax:
        return blindsUp(blindCur - blindMin)

    down(v)

    print("BLINDS DOWN")

def setMin():
    global blindMin, blindMax, blindCur

    if blindMin:
        return None

    if not blindMax:
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

    if blindMax:
        return None

    if not blindMin:
        blindMax = blindCur
    else:
        blindMax = blindCur
        if blindMin < 0:
            blindMax -= blindMin
            blindMin = 0
            blindCur = blindMax

    updateLog()

def reset():
    global blindMin, blindMax, blindCur
    
    blindMin = None
    blindMax = None
    blindCur = 0

log.close()