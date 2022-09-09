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

# print('Help me, I have forgotten what is the best movie ever. The answer is saved in the file bestmovie.txt.\n The file is in one directory in /home/ec2-user/, help me find it, read it and I will give you a surpise')


print('There is a text file called bestmovie.txt hidden somewhere within a directory(ies) in /home/ec2-user. Your mission is to navigate your way through these directories and find bestmovie.txt. Read the file, and tell me what the best movie is!')   
