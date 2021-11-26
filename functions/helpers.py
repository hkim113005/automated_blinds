from functions.blinds import *

blindMin = 0
blindMax = 200
blindCur = 100

def blindsUp(v=0):
    if v == 0 and blindMin and blindMax:
        return blindsUp(blindMax - blindCur)

    up(v)
    
    print("BLINDS UP")
    
def blindsDown(v=0):
    if v == 0 and blindMin and blindMax:
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

def reset():
    global blindMin, blindMax, blindCur
    
    blindMin = None
    blindMax = None
    blindCur = 0
