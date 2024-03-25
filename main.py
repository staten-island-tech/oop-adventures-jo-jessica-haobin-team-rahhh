
import os
from tutorial import tut
from finalboss import thebossbattle


os.system('cls')



tut.tutorial_part1()


if tut.tutorial_part2() >= 100:
    a = thebossbattle.chancetochangeclass()
    thebossbattle.createboss()
    thebossbattle.fightboss(a)

    



