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
    f.write('Thank you for finding me!!!. \n This is the best movie ever, take some participation points')

print('Help me, I have forgotten what is the best movie ever. The answer is saved in the file bestmovie.txt.\n The file is in one of the three directories in /home/ec2-user/, help me find it, read it and I will give you a surpise')
