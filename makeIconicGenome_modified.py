import sys

aHandle = open (sys.argv [1])

lines = aHandle.readlines ()

aMap = {}

id = 0

for aLine in lines:

	aLine = aLine.replace ("\n", "")

	aMap [id] = aLine

	id = id + 1



pfa03=open('pseudo03.fa.txt','w')
bHandle = open (sys.argv [2])

lines = bHandle.readlines ()

genome = ""

for aLine in lines:
	
	aLine = aLine.replace ("\n", "")
	words = aLine.split (" ")
	
	for aWord in words:

		genome = genome + aMap [int(aWord)]
pfa03.write (">pseudo" + sys.argv [2] + "\n" + genome)
pfa03.close()

pfa08=open('pseudo08.fa.txt','w')
cHandle = open (sys.argv [3])

lines = cHandle.readlines ()

genome = ""

for aLine in lines:
	
	aLine = aLine.replace ("\n", "")
	words = aLine.split (" ")
	
	for aWord in words:

		genome = genome + aMap [int (aWord)]
pfa08.write (">pseudo" + sys.argv [3] + "\n" + genome)
pfa08.close()

pfa09=open('pseudo09.fa.txt','w')
dHandle = open (sys.argv [4])

lines = cHandle.readlines ()

genome = ""

for aLine in lines:
	
	aLine = aLine.replace ("\n", "")
	words = aLine.split (" ")
	
	for aWord in words:

		genome = genome + aMap [int (aWord)]
pfa09.write (">pseudo" + sys.argv [4] + "\n" + genome)
pfa09.close()

pfa18=open('pseudo18.fa.txt','w')
eHandle = open (sys.argv [5])

lines = cHandle.readlines ()

genome = ""

for aLine in lines:
	
	aLine = aLine.replace ("\n", "")
	words = aLine.split (" ")
	
	for aWord in words:

		genome = genome + aMap [int (aWord)]
pfa18.write (">pseudo" + sys.argv [5] + "\n" + genome)
pfa18.close()
#print ">pseudo" + sys.argv [2] + "\n" + genome
