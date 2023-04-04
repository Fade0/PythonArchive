def cw1():
    #Zadanie 1. Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym pomieszczeniu,
    # zakładając prostokątną podłogę i prostokątne panele.
    # Dane wejściowe to długość i szerokość podłogi,
    # (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela oraz ilość paneli w opakowaniu. (10%)

    howManyPanels(4,5)
    howManyPanels(3,6)
    howManyPanels(40,52)

def howManyPanels(length, width):
    surface = length * width
    surfaceArea = surface
    count = 0

    print("Area to cover:", surface)

    basePanelLength = 1.285
    basePanelWidth = 0.192
    panelSurface = basePanelLength * basePanelWidth

    print("Panel Surface:", panelSurface)

    while(surface - panelSurface > 0):
        #print("Panel Surface: " , panelSurface)
        surface = surface - panelSurface
        #print("Surface: ", surface)
        count = count + 1
        #print(count)

    count = count + markup(count)
    count = round(count) +1

    print ("You will need:", count, "panels to cover", surfaceArea, "m^2, including 10% markup")

    return count


def markup(count):
    markupResult = count * 1.1
    print(markupResult)

    return markupResult
