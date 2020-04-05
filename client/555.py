import datetime
 
start = datetime.datetime.now()

values = [
    [30, 25, 60, 95],
    [20, 70, 55, 25],
    [10, 20, 50, 55],
    [55, 65, 15, 45],
    [55, 90, 80, 90],
    [85, 55, 60, 90],
    [15, 55, 45, 95],
    [65, 55, 55, 75],
    [70, 35, 55, 55],
    [60, 75, 55, 55],
]

firstColumn = []
for value in values:
    firstColumn.append(value[0])

def change(nb):
    temp = values[nb][len(values[nb])-1]
    for i in reversed(range(1, len(values[nb]))):
        values[nb][i] = values[nb][i-1]
    values[nb][0] = temp

def getSums():
    sums = []
    for i in range(4):
        sums.append(0)

    for iValues, value in enumerate(values):
        for iValue, v in enumerate(value):
            sums[iValue] += v
    
    return sums

successes = []
def shot(nb):
    getSums()
    if getSums() == [555, 555, 555, 555]:
        successes.append(values)
        printResult(values)
    change(nb)
    # if values[nb][0] != firstColumn[nb]:
    #     shot(nb)

def printResult(arr):
    sums = []
    for i in range(4):
        sums.append(0)

    for ar in arr:
        print(str(ar))
        for i, a in enumerate(ar):
            sums[i] += a

    print("-----------------")
    print(str(sums))
    print("-----------------")
    print("-----------------")
    print("-----------------")

for i in range(4):
    print("0: " + str((datetime.datetime.now() - start).total_seconds()))
    shot(0)
    for j in range(4):
        print("1: " + str((datetime.datetime.now() - start).total_seconds()))
        shot(1)
        for k in range(4):
            shot(2)
            for l in range(4):
                shot(3)
                for m in range(4):
                    shot(4)
                    for n in range(4):
                        shot(5)
                        for o in range(4):
                            shot(6)
                            for p in range(4):
                                shot(7)
                                for q in range(4):
                                    shot(8)
                                    for r in range(4):
                                        shot(9)

for success in successes:
    printResult(values)

print(str((datetime.datetime.now() - start).total_seconds()))