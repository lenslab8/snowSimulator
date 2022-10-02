import os
import util


#outfile = open('timeRequired.txt', "a")
#outfile.truncate(0)

outfile = open('accuracy.txt', "a")
outfile.truncate(0)

#outfile2 = open('bitErrorRate.txt', "a")
#outfile2.truncate(0)
numberOfPacketsFromEachNode = 1
i = 0
while i < numberOfPacketsFromEachNode:
    # os.pause(10)
    #os.system("snowAndCdma.py")
    # os.system("snowCdmaDelay.py")
    os.system("snowRandom.py")
    i += 1

outfile.close()
#outfile2.close()
