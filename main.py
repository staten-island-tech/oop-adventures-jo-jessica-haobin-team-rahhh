#put tutorital here
#after tutorial, put fight 
import os
from tutorial import tut
from finalboss import thebossbattle


os.system('cls')



tut.tutorial_part1()


if tut.tutorial_part2() >= 100:
    a = thebossbattle.chancetochangeclass()
    thebossbattle.createboss()
    thebossbattle.fightboss(a)

    

# 1 + 1 = 3
# 1 - 1 + 1 - 1 = 3 - 1 - 1
# 0 + 0 = 1
# 1 = 100%
# two failing grades == a passing grade


