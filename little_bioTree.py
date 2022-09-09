#!/usr/bin/env python

import os
import random
import pathlib
my_wd=os.getcwd()

mydirs=['Topgun', 'Avatar', 'Avengers_infinitywar', 'Suckerpunch', 'FinalDestination', 'JusticeLeague', 'Avengers_endgame', 'TheBatman']


homedir='/home/ec2-user/'
homedirs=list(range(3))
for i in homedirs:
   homedirs[i]=homedir+'/'.join(random.sample(mydirs, 3))

for directory in homedirs:
	os.makedirs(directory)
newdir=random.sample(homedirs, 1)[0]
with open(newdir+'/bestmovie.txt', 'w') as f:
    f.write('This is the best movie ever')
