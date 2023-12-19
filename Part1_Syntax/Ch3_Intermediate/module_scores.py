scores = []

def AddScore(s):
    scores.append(s)

def AddfScore(*s):
    for i in s:
        scores.append(i)

def DelScore():
    scores.clear()

def GetScores():
    return  scores

def GetTotalScore():
    total = 0
    for s in scores:
        total += s
    return total

def GetAvgScore():
    avg = GetTotalScore() / len(scores)
    return round(avg, 2)