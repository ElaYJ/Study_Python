income = 0
waterPrice = 0; electricPrice = 0; gasPrice = 0

def setIncome(ic):
    global income
    income = ic

def getIncome():
    return income

def setWaterPrice(wp):
    global waterPrice
    waterPrice = wp

def setElectricPrice(ep):
    global electricPrice
    electricPrice = ep

def setGasPrice(gp):
    global gasPrice
    gasPrice = gp

def getUtilityBill():
    result = waterPrice + electricPrice + gasPrice
    return result

def getUtilityBillRate():
    result = getUtilityBill() / getIncome() * 100
    return round(result, 2)

def formatedNumber(n):
    return format(n, ',')


