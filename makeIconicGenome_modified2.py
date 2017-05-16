import sys

aHandle = open (sys.argv [1])

lines = aHandle.readlines ()

aMap = {}

id = 0

for aLine in lines:

	aLine = aLine.replace ("\n", "")

	aMap [id] = aLine

	id = id + 1



pfa08=open('pseudo08.fa.txt','w')
bHandle = open (sys.argv [2])

lines = bHandle.readlines ()

genome = ""

for aLine in lines:
	
	aLine = aLine.replace ("\n", "")
	words = aLine.split (" ")
	
	for aWord in words:

		genome = genome + aMap [int(aWord)]
        #print genome
pfa08.write (">pseudo" + sys.argv [2] + "\n" + genome)
pfa08.close()
