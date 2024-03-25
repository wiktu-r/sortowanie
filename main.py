import random
import time
import numpy as np
import matplotlib.pyplot as plt
def test(tabela):
    czasyWykoania = []
    for i in range(dlugosc):
        temp = 0
        for n in range(iloscTestow):
            tempTable = []
            for x in range(i):
                tempTable.append(tabela[x])

            timeStart = time.perf_counter()
            ###ALGORYTM###
            tempTable.sort()
            ##############
            timeStop = time.perf_counter()
            temp = temp + (timeStop-timeStart)

        czasyWykoania.append(temp/iloscTestow)
    return czasyWykoania
iloscTestow = 5
dlugosc = 20000
dolnyKres = 0
gornyKres = 2000
iloscSkokow = 2

masterTable = []

for x in range(dlugosc):
    masterTable.append(random.randint(dolnyKres, gornyKres))
testowatablica = test(masterTable)
points = np.array(testowatablica)

print(testowatablica)
print(len(testowatablica))


plt.plot(points)
plt.show()


