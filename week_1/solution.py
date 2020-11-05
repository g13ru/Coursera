#рисуем лестницу
import sys

maximum_heigh = int(sys.argv[1])

for step in range(maximum_heigh):
    step = step + 1
    print(' '*(maximum_heigh - step)+(step*'#'))
