import random
def sortear_raridade():
    num = random.randint(1,1000)
    if num <= 560:
        return "COMUM"
    elif num <= 910:
        return "RARO"
    elif num <= 985:
        return "EPICO"
    else:
        return "LENDARIO"